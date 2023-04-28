from Algorithms import RabinKarp, Sunday, SundayWildcards, WildNaive

with open('poison.txt', encoding='utf8') as f:
    poem = f.read().replace('\n', ' ')

patternWild = "I w\?s angry"
pattern = "And I"

wildSundayResults = SundayWildcards.wildSundaySearch(patternWild, poem)
print("Sunday with wildcards: ")
print(wildSundayResults)
print("Naive/Bruteforce: ")
print(WildNaive.brute_force(poem, patternWild))

# print("Sunday: ")
# print(Sunday.sundaySearch(pattern, poem))
#
# print("Rabin-Karp: ")
# print(RabinKarp.rabinKarp(pattern, poem))

