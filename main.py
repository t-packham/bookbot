def main(): 
    book_path = "books/frankenstein.txt"
    text = open_file(book_path)
    word_count = count_words(text)
    character_count = count_characters(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    for char in character_count:
        if char.isalpha():
            print(f"The '{char}' character was found {character_count[char]} times")

def open_file(path):
    with open(path) as f:
        return f.read()

def count_words(books):
    words = books.split()
    count = len(words)
    return count

def count_characters(text):
    characters = {}
    for letter in text:
        letter = letter.lower()
        if letter in characters:
            characters[letter] += 1
        else:
            characters[letter] = 1
    return characters
        


main()