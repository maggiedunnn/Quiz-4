#The author is Maggie Dunn
def hash_spam(string):
    index = 0
    total = 0
    while index < len(string):
        if string[index] == "#":
            total += 1
            index += 1
        else:
            index += 1
    if total >= 4:
        print("this tweet will be considered spam.")
    else:
        return None
