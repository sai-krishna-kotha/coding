# Reverse each word in a sentence
# "kotha sai krishna" -> "krishna sai kotha"
def sol(sentence: str):
    words = sentence.split()
    return ' '.join(reversed(words))

print(sol("kotha sai krishna"))