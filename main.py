from stats import word_count, char_count, sorting_characters
import sys #provides access to command line arguments


def getting_text(path):

    with open(path) as f:
        contents = f.read()
        return contents

def main():

    path_of_book = sys.argv[1] #['main.py', 'books/frankenstein.txt'], the index 1 is the path to the book
    book = getting_text(path_of_book)

    words = word_count(book)
    characters = char_count(book)
    sorted_format = sorting_characters(characters)

    print(f"============ BOOKBOT ============\n"f"Analyzing book found at {path_of_book}...")

    print(f"----------- Word Count ----------\n"f"Found {words} total words")

    print(f"--------- Character Count -------")

    for i in sorted_format:
        #checking if key value, titled "char" is in the alphabet
        if not i["char"].isalpha():
            continue

        print(f"{i['char']}: {i['amount']}")

    print("============= END ===============")


if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
        (sys.exit(1))

else:
    main()

    


