import json
from difflib import get_close_matches

# data is a python dictionary
data = json.load(open("data.json"))

def translate(word):
    word = word.lower();
    if word in data:
        return data[word]
    elif len(get_close_matches(word,data.keys())) > 0:
        print("Did you mean %s instead? Y for true and N for false"% get_close_matches(word,data.keys())[0])
        answer = input()
        if answer == 'Y':
            return data[get_close_matches(word,data.keys())[0]]
        else:
            return "The word you entered does not exist, pls double check :)"
    else:
        return "The word you entered does not exist, pls double check :)"


print(translate('rainm'))