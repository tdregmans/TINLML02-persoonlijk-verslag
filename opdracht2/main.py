"""

    TINLML02
    Thijs Dregmans
    https://github.com/tdregmans/TINLML02-persoonlijk-verslag

    main.py
    Last edited: 2024-05-22 (YYYY-MM-DD)
    Version: 1.0

    back.py and muser.py come from: https://wiztech.nl/hr/ti/tinlab_ml/progs/music

"""

# import given files
import bach
import muser as ms
import random
import copy

# constants
NO_OF_ITERATIONS = 20
NO_OF_VARIANTS_PER_ITERATION = 5
NO_OF_MUTATIONS_PER_VARIANT = 10

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

def inputInt(prompt, errorMessage = ""):
    while True:
        s = input(prompt)

        try:
            i = int(s)
            
            if i >= 0 and i <= 10:
                return i
            else:
                raise ValueError
            
        except ValueError:
            print(errorMessage)

def mutateSong(song, noOfMutationsPerVariant = NO_OF_MUTATIONS_PER_VARIANT):
    s = list(copy.copy(song))
    for mutation in range(noOfMutationsPerVariant):
        randomTrack = list(random.choice(s))
        randomTrack[random.randint(0, len(randomTrack))] = (random.choice(POSSIBLE_NOTES), random.choice(POSSIBLE_NOTE_VALUES))

    print(song)
    print(s)
    return s

# create base file
# happens automatically by importing bach file can found as 'song.wav'


muser = ms.Muser ()


for iterationId in range(NO_OF_ITERATIONS):
    print(f"Iteration {iterationId}")
    filename = "song.wav"

    # randomly mutate bach 5 times
    mutations = []
    for variantId in range(NO_OF_VARIANTS_PER_ITERATION):
        mutations.append(mutateSong(bach.bach, NO_OF_MUTATIONS_PER_VARIANT))

    # rate mutation
    for variantId in range(NO_OF_VARIANTS_PER_ITERATION):
        # create song
        muser.generate(mutations[variantId])
        
        i = inputInt(f"Rate {filename} from 0 to 10: ", "Invalid input. Must be an integer from 0 to 10")


# create 5 files based on the base with random mutations

# rate 5 new files

# again, create 5 files based on the rating

