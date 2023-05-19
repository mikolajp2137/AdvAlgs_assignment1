from Algorithms import RabinKarp, Sunday, SundayWildcards, WildNaive

with open('poison.txt', encoding='utf8') as f:
    poem = f.read().replace('\n', ' ')

patternWild = "I ?as a\*"
pattern = "And I"

print("Sunday with wildcards: ")
print(SundayWildcards.wildSundaySearch(patternWild, poem))
print("Naive/Bruteforce: ")
print(WildNaive.brute_force(patternWild, poem))
