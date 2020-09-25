# jewels = "abc", stones = "ac", return 2
# jewels = "Af", stones = "AaaddfFf", return 3
# jewels = "AYOPD", stones = "ayopd", return 0

from collections import Counter
def jewels_and_stone(jewels,stones):

    jewl = Counter(jewels)
    stone_count = 0
    for i in range(len(stones)):
        if stones[i] in jewl:
            stone_count += 1
    return stone_count

print(jewels_and_stone("abc","ac"))
print(jewels_and_stone("Af","AaaddfFf"))
print(jewels_and_stone("AYOPD","ayopd"))