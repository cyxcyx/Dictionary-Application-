import json
from difflib import get_close_matches

# data is a python dictionary
data = json.load(open("data.json"))


def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word,data.keys())) > 0:
        answer = input("Did you mean %s instead? Y for true and N for false\n"% get_close_matches(word,data.keys())[0])
        if answer == 'Y':
            return data[get_close_matches(word,data.keys())[0]]
        elif answer == 'N':
            return "The word you entered does not exist, pls double check :)"
        else:
            return "The world you enter is unrecognizable"
    else:
        return "The word you entered does not exist, pls double check :)"



word = input("Enter the word: \n")

output = (translate(word))

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
