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
import Generator as sg

# constants
NO_OF_ITERATIONS = 20
NO_OF_VARIANTS_PER_ITERATION = 5
NO_OF_MUTATIONS_PER_VARIANT = 10

def inputInt(prompt, errorMessage = ""):
    """
    Function used to get user rating.
    """
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

if __name__ == "__main__":
    # create generator
    generator = sg.SongGenerator(bach.bach)

    # compose song and play it
    generator.generateSong()

    # rate the song
    rating = inputInt("Rate from 0 to 10: ", "Invalid input. Must be an integer from 0 to 10")

    for iterationId in range(NO_OF_ITERATIONS):

        # mutate song
        generator.mutateSong(rating)

        # compose song and play it
        generator.generateSong()

        # rate the song
        if iterationId < NO_OF_ITERATIONS - 1:
            rating = inputInt("Rate from 0 to 10: ", "Invalid input. Must be an integer from 0 to 10")
    
    # Final song
    print("Final song generated!")
    generator.playSong()
