from random import randint
import tomllib

with open("rand_morph/config.toml", "rb") as f:
    config = tomllib.load(f)

VOWEL_LIST = config["VOWELS"].split(" ")
CONSONANT_LIST = config["CONSONANTS"].split(" ")
LONG_VOWEL_RATE = config["LONG_VOWEL_RATE"]
MAX_LENGTH = config["MAX_LENGTH"]
MORPH_NUM = config["MORPH_NUM"]

# generate a random morpheme
def rand_morph():
    morpheme = ""
    syll_num = randint(1, MAX_LENGTH)
    count = 0

    while count < syll_num:
        consonant = CONSONANT_LIST[randint(0, len(CONSONANT_LIST) - 1)]
        vowel = VOWEL_LIST[randint(0, len(VOWEL_LIST) - 1)]

        morpheme += consonant
        morpheme += vowel

        long_vowel = randint(0, int(100 * LONG_VOWEL_RATE))

        if long_vowel > randint(0, 100):
            morpheme += vowel

        count += 1
    
    return morpheme

if __name__ == "__main__":
    count = 0

    while count < MORPH_NUM:
        print(rand_morph())

        count += 1