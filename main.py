def main(): 
    book_path = "books/frankenstein.txt"
    text = open_file(book_path)
    word_count = count_words(text)
    character_count = count_characters(text)
    print(character_count)

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