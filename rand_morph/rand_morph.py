from random import randint, choice
import tomllib

with open("rand_morph/config.toml", "rb") as f:
    config = tomllib.load(f)

VOWEL_LIST = config["VOWELS"].split(" ")
CONSONANT_LIST = config["CONSONANTS"].split(" ")
LONG_VOWEL_RATE = config["LONG_VOWEL_RATE"]
DIPHTHONG_RATE = config["DIPHTHONG_RATE"]
MAX_LENGTH = config["MAX_LENGTH"]
MORPH_NUM = config["MORPH_NUM"]
MELODY_LIST = config["MELODIES"].split(" ")
DIPHTHONG_LIST = config["DIPHTHONGS"].split(" ")

# generate a random morpheme
def rand_morph():
    morpheme = ""
    syll_num = randint(1, MAX_LENGTH)
    count = 0
    melody = choice(MELODY_LIST)

    while count < syll_num:
        consonant = CONSONANT_LIST[randint(0, len(CONSONANT_LIST) - 1)]
        diphthong_chance = 100 * DIPHTHONG_RATE

        morpheme += consonant

        if diphthong_chance > randint(0, 100):
            vowel = DIPHTHONG_LIST[randint(0, len(DIPHTHONG_LIST) - 1)]
            new_vowel = ""

            for glyph in vowel:
                if melody == "H":
                    glyph += "́"
                elif melody == "L":
                    glyph += "̀"
                
                new_vowel += glyph
            
            vowel = new_vowel
        else:
            vowel = VOWEL_LIST[randint(0, len(VOWEL_LIST) - 1)]
            long_vowel_chance = 100 * LONG_VOWEL_RATE

            if melody == "H":
                vowel += "́"
            elif melody == "L":
                vowel += "̀"

            if long_vowel_chance > randint(0, 100):
                morpheme += vowel

        morpheme += vowel

        count += 1
    
    return morpheme

if __name__ == "__main__":
    count = 0

    while count < MORPH_NUM:
        print(rand_morph())

        count += 1