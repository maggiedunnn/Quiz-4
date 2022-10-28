#The author is Maggie Dunn
def count_hashtag(string):
    index = 0
    total = 0
    while index < len(string):
        if string[index] == "#":
            total += 1
            index += 1
        else:
            index += 1
    print(total)
