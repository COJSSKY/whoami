#!/usr/bin/python3

import random

words = ["Discovering Your Passions", "Discovering Your Skills", "You are here to exist", "You are here to make friends", "Idk figure it our", "You know, Right?", "You are here to enjoy life"]

random_phrase = " ".join(random.sample(words, random.randint(2, 5)))

print(random_phrase)
