def main():

    with open("books/frankenstein.txt") as f:
        file_content = f.read()

    words = wordCount(file_content)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words} words found in the document\n")

    characters = charCount(file_content)
    print(f"{characters} are the amount of characters")

    


def wordCount(text):
    
    text = text.split()
    total_words = len(text)
    
    return total_words

def charCount(text):

    char_dict = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "u": 0, "w": 0, "y": 0, "x": 0, "z": 0,}
    text = text.lower()

    for i in text:

        if i in char_dict:
            char_dict[i] += 1

    list_of_dict = []
    for i in char_dict:
        list_of_dict.append({i:char_dict[i]})

    return char_dict


main()

