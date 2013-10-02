# You are to produce a random text generator using markov chains. We've provided a very bare skeleton for 
# you to start your program from. Up until now, we've been writing our programs in a very freeform manner, just writing code at the 'top level', 
# the same place where we put our global variables. This is generally considered bad form. Code should always be contained in functions or class methods wherever possible.

# The skeleton program we've provided has a recommended set of functions to start with, including a very odd if 
# statement at the bottom. You can ignore how this statement works for now, all it does is it makes sure your program starts inside the main() function.

# The program should accept a filename from the command line, and a sample run should look similar to the following:

#     meringue:Exercise08 chriszf$ python markov.py shakespeare.txt
#     Forsooth, or somesuch.

# You can use any text as an input corpus, you might try (Project Gutenberg)[http://www.gutenberg.org/] for some inspiration.

# Extra Credit
# ------------
# Do any of the following

# 1. See what happens when you mix two different authors together as a single source
# 2. Modify the program to allow any number of words to use as keys, ie: choose the size of your n-gram used in your chain
# 3. Create a new Twitter persona and wire up your markov program with the twitter module (import twitter) to produce random tweets.
import random
from sys import argv
script, filename1 = argv

def read_text(text):
    f = open(text)
    text = f.read()
    return text

def strip_text(text):
    sexy_list = text.split()
    for i in range(len(sexy_list)):
        sexy_list[i] = sexy_list[i].strip("\'\".;:!,?/^&*()")
    return sexy_list

def tuple_dict(l):
    bigram_dict = {}
    for i in range(len(l) - 2):
        tuple_var = (l[i], l[i + 1])
        if not bigram_dict.get(tuple_var):
            bigram_dict[tuple_var] = [l[i + 2]]
        else:
            bigram_dict[tuple_var].append(l[i + 2])
    return bigram_dict

def make_pseudo_text(dict):
    new_words = random.sample(dict, 1)
    new_words = new_words[0]
    pseudo_text = new_words[0] + " " + new_words[1]
    while len(pseudo_text) <= 75:
        next_word = random.sample(dict.get(new_words), 1)
        pseudo_text += " " + next_word[0]
        new_words = new_words[1], next_word[0]
    return pseudo_text

def main():
    # print make_pseudo_text(tuple_dict(strip_text(read_text(filename1))))

    text = read_text(filename1)
    _list = strip_text(text)
    bigram_dict = tuple_dict(_list)
    final_output = make_pseudo_text(bigram_dict)
    print final_output


main()