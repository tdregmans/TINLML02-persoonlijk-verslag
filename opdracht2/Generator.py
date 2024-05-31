"""

    TINLML02
    Thijs Dregmans
    https://github.com/tdregmans/TINLML02-persoonlijk-verslag

    Generator.py
    Last edited: 2024-05-27 (YYYY-MM-DD)
    Version: 1.0

    back.py and muser.py come from: https://wiztech.nl/hr/ti/tinlab_ml/progs/music

"""

# import modules
import muser as ms
from playsound import playsound
import random
import numpy as np
from time import gmtime, strftime

# constants
NO_OF_MUTATIONS_PER_VARIANT = 3

# notes
"""
# Possible notes notation 
Possible notes notation is based on example source code tomita: https://tomita.readthedocs.io/en/latest/_modules/tomita/legacy/pysynth.html

'song' is a Python list (or tuple) in which the song is defined,
the format is [['note', value]]

Notes are 'a' through 'g' of course,
optionally with '#' or 'b' appended for sharps or flats.
Finally the octave number (defaults to octave 4 if not given).
An asterisk at the end makes the note a little louder (useful for the beat).
'r' is a rest.

Note value is a number:
1=Whole Note; 2=Half Note; 4=Quarter Note, etc.
Dotted notes can be written in two ways:
1.33 = -2 = dotted half
2.66 = -4 = dotted quarter
5.33 = -8 = dotted eighth

"""

POSSIBLE_NOTES = [
    "c", "d", "e", "f", "g", "a", "b",
    "c#", "d#", "e#", "f#", "g#", "a#", "b#",
    "cb", "db", "eb", "fb", "gb", "ab", "bb",
    "c2", "d2", "e2", "f2", "g2", "a2", "b2",
    "c#2", "d#2", "e#2", "f#2", "g#2", "a#2", "b#2",
    "cb2", "db2", "eb2", "fb2", "gb2", "ab2", "bb2",
    "c3", "d3", "e3", "f3", "g3", "a3", "b3",
    "c#3", "d#3", "e#3", "f#3", "g#3", "a#3", "b#3",
    "cb3", "db3", "eb3", "fb3", "gb3", "ab3", "bb3",
    "c*", "d*", "e*", "f*", "g*", "a*", "b*",
    "c#*", "d#*", "e#*", "f#*", "g#*", "a#*", "b#*",
    "cb*", "db*", "eb*", "fb*", "gb*", "ab*", "bb*",
    "c2*", "d2*", "e2*", "f2*", "g2*", "a2*", "b2*",
    "c#2*", "d#2*", "e#2*", "f#2*", "g#2*", "a#2*", "b#2*",
    "cb2*", "db2*", "eb2*", "fb2*", "gb2*", "ab2*", "bb2*",
    "c3*", "d3*", "e3*", "f3*", "g3*", "a3*", "b3*",
    "c#3*", "d#3*", "e#3*", "f#3*", "g#3*", "a#3*", "b#3*",
    "cb3*", "db3*", "eb3*", "fb3*", "gb3*", "ab3*", "bb3*",
    "r"]
POSSIBLE_NOTE_VALUES = [1, 2, 4, -2, -4, -8]

# rating
class rating:
    BAD = 2
    MID = 5
    TOP = 8

class SongGenerator:
    def __init__(self, base):
        # music creator
        self.muser = ms.Muser()

        # operational storage
        self.paths = []
        self.songs = []
        self.ratings = []
        
        # working song
        self.song = []
        for track in base:
            self.song.append(list(track))

    def generateSong(self):
        # create filename
        now = strftime("%Y%m%d%H%M%S", gmtime())
        filename = f"song{now}.wav"
        # generate song
        self.muser.generate(self.song, filename)
        # add song path to paths and play the song
        self.paths.append(filename)
        self.songs.append(self.song)
        self.playSong()
    
    def playSong(self, path=None):
        if path == None:
            path = self.paths[-1]
        playsound(path)
    
    def getFitness(self):
        # fitness of a song is defined as the standard deviation of all note lengths
        trackFitnessSum = 0
        for track in self.song:
            noteValues =  list(map(float, np.array(self.song[0]).T[1]))
            trackFitnessSum += np.std(np.array(noteValues))
        return trackFitnessSum # Problem when using autoFitness: The whole song is rated; while instead parts of the song should be rated, so crossover is possible!!!!

    def mutateSongRandom(self, noOfMutationsPerVariant = NO_OF_MUTATIONS_PER_VARIANT):
        # mutate existing song
        for mutation in range(noOfMutationsPerVariant):
            randomTrackId = random.randint(0, len(self.song) - 1)
            randomNoteId = random.randint(0, len(self.song[randomTrackId]) - 1)

            newRandomNote = (random.choice(POSSIBLE_NOTES), random.choice(POSSIBLE_NOTE_VALUES))

            self.song[randomTrackId][randomNoteId] = newRandomNote
    
    def crossoverTraits(self):
        # use self.ratings and self.songs to create a new song out of the best
        
        noOfRatingsPerSong = len(self.ratings[0]) # assume that the noOfRatings stay constant

        # find highest rating with id
        highestRatingId = (-1, -1) # reprents the (songId, ratingId) of the highest rating ever
        highestRating = -1
        for songId in range(len(self.songs) - 1):
            for ratingId in range(len(self.ratings[songId]) - 1):
                if self.ratings[songId][ratingId] > highestRating:
                    highestRating = self.ratings[songId][ratingId]
                    highestRatingId = (songId, ratingId)

        # find the lowest rating in the last song
        lowestRatingId = (-1, -1) # reprents the (songId, ratingId) of the lowest rating ever
        lowestRating = -1
        for ratingId in range(len(self.ratings[-1]) - 1):
            if self.ratings[-1][ratingId] < lowestRating or lowestRating == -1:
                songId = len(self.ratings) - 1
                lowestRating = self.ratings[songId][ratingId]
                lowestRatingId = (songId, ratingId)
        
        # crossover the song-part of the best ever, with the worst in the last song
        # WARNING! THIS PART OF THE FUNCTION ONLY WORKS WHEN NO_OF_RATINGS = 2
        songId = len(self.ratings) - 1
        for trackId in range(len(self.song) - 1):
            # seperate track into 2 parts
            # WARNING! THIS ONLY WORKS WHEN NO_OF_RATINGS = 2
            # trackPart1 = self.song[trackId][:(len(self.song[trackId])//2)]
            # trackPart2 = self.song[trackId][(len(self.song[trackId])//2):]

            songWithHighestRating = self.songs[highestRatingId[0]]
            if highestRatingId[1] == 0:
                highestRatedTrackPart = songWithHighestRating[trackId][:(len(self.song[trackId])//2)]
            else:
                highestRatedTrackPart = songWithHighestRating[trackId][(len(self.song[trackId])//2):]

            if lowestRatingId == 0:
                self.song[trackId][:(len(self.song[trackId])//2)] = highestRatedTrackPart
            else:
                self.song[trackId][(len(self.song[trackId])//2):] = highestRatedTrackPart




    def mutateSong(self, ratings, feedbackLastSong=rating.MID, noOfMutationsPerVariant = NO_OF_MUTATIONS_PER_VARIANT):

        if len(self.paths) <= 1:
            # store ratings 
            self.ratings.append(ratings)
            
            # mutate only existing song
            self.mutateSongRandom()
        else:
            # store ratings 
            self.ratings.append(ratings)
            # crossover between the highest rated tracks
            self.crossoverTraits()

            # and introduce random mutations
            self.mutateSongRandom()