def main():
    path = "books/frankenstein.txt"
    doc = read_document(path)
    word_count = count_words(doc)
    letter_counts = count_letters(doc)
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document")
    print("")
    letters = list(letter_counts)
    letters.sort(key=lambda letter: letter_counts[letter], reverse=True)
    for letter in letters:
        if letter.isalpha():
            print(f"The '{letter}' character was found {letter_counts[letter]} times")
    print("--- End report ---")

def read_document(path):
    with open(path) as f:
        return f.read()

def count_words(string):
    word_count = len(string.split())
    return word_count

def count_letters(string):
    counts = {}
    for c in string.lower():
        if c in counts:
            counts[c] += 1
        else:
            counts[c] = 1
    return counts

main()