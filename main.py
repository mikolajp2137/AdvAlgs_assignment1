import Sunday

with open('raven.txt', encoding='utf8') as f:
    poem = f.read().replace('\n', ' ')


pattern = "Raven"

print(Sunday.sundaySearch(pattern,poem))
