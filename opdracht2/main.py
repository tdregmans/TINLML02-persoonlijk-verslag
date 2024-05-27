"""

    TINLML02
    Thijs Dregmans
    https://github.com/tdregmans/TINLML02-persoonlijk-verslag

    main.py
    Last edited: 2024-05-27 (YYYY-MM-DD)
    Version: 1.0

    back.py and muser.py come from: https://wiztech.nl/hr/ti/tinlab_ml/progs/music

"""

# import given files
import bach
import Generator as sg

# constants
NO_OF_ITERATIONS = 4
NO_OF_MUTATIONS_PER_VARIANT = 2
NO_OF_RATINGS = 2

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

def rateSong(noOfRatings = NO_OF_RATINGS):
    ratings = []
    for ratingId in range(noOfRatings):
        ratings.append(inputInt(f"Rate part {ratingId + 1}/{noOfRatings} from 0 to 10: ", "Invalid input. Must be an integer from 0 to 10"))
    return ratings

def autoRateSong(noOfRatings = NO_OF_RATINGS):
    ratings = []
    for ratingId in range(noOfRatings):
        ratings.append(print(generator.getFitness()))
    return ratings

if __name__ == "__main__":
    # simple bach
    simpleBach = [bach.bach[0]]
    # create generator
    generator = sg.SongGenerator(simpleBach)

    # compose song and play it
    generator.generateSong()

    # rate the song
    rating = rateSong()

    # optional: Use automatic fitness-function to rate the song
    # rating = autoRateSong()

    for iterationId in range(NO_OF_ITERATIONS):

        # mutate song
        generator.mutateSong(rating)

        # compose song and play it
        generator.generateSong()

        # rate the song
        if iterationId < NO_OF_ITERATIONS - 1:
            rating = rateSong()
    
    # Final song
    print("Final song generated!")
    generator.playSong()
