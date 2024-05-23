"""

    TINLML02
    Thijs Dregmans
    https://github.com/tdregmans/TINLML02-persoonlijk-verslag

    muser.py
    Last edited: 2024-05-23 (YYYY-MM-DD)
    Version: 1.0

    source: https://wiztech.nl/hr/ti/tinlab_ml/progs/music

"""

import glob as gl
import os
import tomita.legacy.pysynth as ps

import shutil as su

class Muser:
    def generate (self, song, songFileName):
        for trackIndex, track in enumerate (song):
            ps.make_wav (
                track,
                bpm = 130,
                transpose = 1,
                pause = 0.1,
                boost = 1.15,
                repeat = 0,
                fn = self.getTrackFileName (trackIndex),
            )

        if len (song) > 1:
            ps.mix_files (
                *[self.getTrackFileName (trackIndex) for trackIndex in range (len (song))],
                songFileName
            )
        else:
            su.copy ('track_000.wav', songFileName)

        for fileName in gl.glob ('track_*.wav'):
            os.remove (fileName)

    def getTrackFileName (self, trackIndex):
        return f'track_{str (1000 + trackIndex) [1:]}.wav'
