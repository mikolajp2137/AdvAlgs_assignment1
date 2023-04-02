from Algorithms import RabinKarp, Sunday, SundayWildcards

with open('poison.txt', encoding='utf8') as f:
    poem = f.read().replace('\n', ' ')

patternWild = "wr*h"
pattern = "wrath"

wildSundayResults = SundayWildcards.wildSundaySearch(patternWild, poem)
print(wildSundayResults)

print(Sunday.sundaySearch(pattern, poem))
print(RabinKarp.rabinKarp(pattern, poem))
