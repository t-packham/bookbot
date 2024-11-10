def main(): 
    book_path = "books/frankenstein.txt"
    text = open_file(book_path)
    count = count_words(text)
    print(count)

def open_file(path):
    with open(path) as f:
        return f.read()

def count_words(books):
    words = books.split()
    count = len(words)
    return count


main()