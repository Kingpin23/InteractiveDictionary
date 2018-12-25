import json
from difflib import get_close_matches


data = json.load(open("data.json"))


def meaning(w):
     w = w.lower()
     if w in data:
        return data[w]
     elif w.title() in data:
        return data[w.title()]
     elif w.upper() in data:
        return data[w.upper()]
     elif len(get_close_matches(w,data.keys())) > 0:
        y_n = input("Did you want to search for %s instead?. Enter Y for yes and N for no." %get_close_matches(w,data.keys())[0])

        if y_n =="Y":
            return data[get_close_matches(w,data.keys())[0]]
        elif y_n == "N":
            return "The word doesn't exist double check or try again."
        else:
            return "Sorry! We couldn't understand your response.Try again entering Y or N."
     else:
        return "Sorry! The word is not available."


word = input("Enter Your word here:")


output = meaning(word)


if type(output) == list:
    i=0
    for item in output:
        i +=1
        print(str(i)+". "+item)
else:
    print(output)


print("=====================================================================================")


