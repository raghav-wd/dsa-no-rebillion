vowels = ["a","e","i","o","u"]

n = 2
def combinations(str="", index = 0):
    if len(str) == n:
        print(str)
        return None
    for i in range(index, len(vowels)):
        combinations(str + vowels[i], i)

combinations()