def main(): 
    book_path = "books/frankenstein.txt"
    text = open_file(book_path)
    print(text)
def open_file(path):
    with open(path) as f:
        return f.read()


main()