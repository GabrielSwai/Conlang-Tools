from random import randint
import webbrowser

PHOIBLE_URL = "https://phoible.org/inventories/view/"
SUFFIX_URL = "#tipa"
NUM_LANGS = 3_020
tab_num = 1

def rand_inventory(n):
    return PHOIBLE_URL + str(n) + SUFFIX_URL

if __name__ == "__main__":
    for i in range(tab_num):
        inventory_num = randint(1, NUM_LANGS)
        webbrowser.open(rand_inventory(inventory_num))