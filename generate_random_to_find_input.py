# Generating random strings until a given string is generated

import string
import random

def random_string(len_st):
    possible = string.ascii_letters+string.digits
    rand_st = "".join(random.choice(possible) for i in range(len_st))
    return rand_st

def generate_random_until_input_found(inp):
    len_st = len(inp)
    step = 0
    while True:
        step += 1
        rand_st = random_string(len_st)
        print("random string: ", rand_st)
        if inp == rand_st:
            print("{0} found after {1} steps".format(inp, step))
            break

if __name__ == "__main__":
    generate_random_until_input_found("shubham")

