"""

    TINLML02
    Thijs Dregmans
    https://github.com/tdregmans/TINLML02-persoonlijk-verslag

    main.py
    Last edited: 2024-05-22 (YYYY-MM-DD)
    Version: 1.0

    back.py and muser.py come from: https://wiztech.nl/hr/ti/tinlab_ml/progs/music

"""

# import modules
import muser as ms
from playsound import playsound
import random
from time import gmtime, strftime

# constants
NO_OF_ITERATIONS = 20
NO_OF_VARIANTS_PER_ITERATION = 5
NO_OF_MUTATIONS_PER_VARIANT = 10

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
        self.muser = ms.Muser()
        self.paths = []
        self.song = base
    
    def generateSong(self):

        now = strftime("%Y%m%d%H%M%S", gmtime())
        filename = f"song{now}.wav"
        self.muser.generate(self.song, filename)

        self.paths.append(filename)
        self.playSong()
    
    def playSong(self, path=None):
        if path == None:
            path = self.paths[-1]
        playsound(path)

    def mutateSong(song, feedbackLastSong=rating.MID, noOfMutationsPerVariant = NO_OF_MUTATIONS_PER_VARIANT):

        ...

        # todo
        s = list(song)
        for mutation in range(noOfMutationsPerVariant):
            randomTrack = list(random.choice(s))
            randomTrack[random.randint(0, len(randomTrack))] = (random.choice(POSSIBLE_NOTES), random.choice(POSSIBLE_NOTE_VALUES))

        print(song)
        print(s)
        return s