import argparse
import os
import random

def load_nouns():
    filename = os.path.join(os.path.dirname(__file__), "animals.txt")
    valid_words = []
    with open(filename) as word_file:
        for line in word_file:
            if not "(" in line and not " " in line and not "list" in line:
                valid_words.append(line.split(os.linesep)[0].replace(" ", "_"))
   
    return valid_words

def load_adjectives(colors):
    filename = os.path.join(os.path.dirname(__file__), "english-adjectives.txt")
    valid_words = []
    with open(filename) as word_file:
        for line in word_file:
            if not "(" in line and not " " in line and not line in colors:
                valid_words.append(line.split(os.linesep)[0])
   
    return valid_words

def load_colors():
    filename = os.path.join(os.path.dirname(__file__), "colors.csv")
    valid_words = []
    with open(filename) as word_file:
        for line in word_file:
            if not "(" in line:
                valid_words.append(line.split(',')[0].strip('"'))
    return valid_words

def gen_name(version = None, salt = "YOUR_PROJECT_CODE"):
    nouns = load_nouns()
    colors = load_colors()
    adjectives = load_adjectives(colors)
    seedstr = "{}{}".format(salt,version) if version is not None else None
    random.seed(seedstr) 
    string = "{}_{}_{}".format(random.choice(colors).lower(),random.choice(adjectives),random.choice(nouns).lower()).replace("\n","")
    return string


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Namegenerator for versions')
    parser.add_argument("-v", '--version', type=str, help='version that should get an additional name',dest='v',action='store')
    parser.add_argument("-s", '--salt', type=str, help='salt to use for the random name, best to use application id of the version', dest='s', action='store')
    args = parser.parse_args()
    print(gen_name(args.v, args.s))