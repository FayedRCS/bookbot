def main():
    path_of_book = "books/frankenstein.txt"
    book_text = getting_text(path_of_book)
    words = word_count(book_text)
    characters = char_count(book_text)
    sorted_lst = sorting_characters(characters)


    print(f"--- Begin report of {path_of_book} ---")

    print(f"Scan found {words} words in the text\n")

    for i in sorted_lst:
        #checking if key value, titled "char" is in the alphabet
        if not i["char"].isalpha():
            continue

        print(f"The '{i['char']}' character was found '{i['amount']}' times")

    print("--- End Scan ---")


#count the amount of words, seperated by whitespace
def word_count(text):
    words = text.split()
    return len(words)

#breaking down further with character count
def char_count(text):

    char_dict = {}
    text = text.lower()
    
    #adds all symbols, but wont matter, we will check if key is in alphabeet later
    for i in text:
        if i in char_dict:
            char_dict[i] += 1
        else: char_dict[i] = 1

    return char_dict



def sorting_characters(dict):
    sorted_list_of_dict = []
    for i in dict:
        sorted_list_of_dict.append({"char" : i, "amount": dict[i]})

        #we created a function for sorting, and what to sort. then pass it through it later in the .sort() method. Read documentation, if i forget

    sorted_list_of_dict.sort(reverse=True, key=sort_sys)
    return sorted_list_of_dict

def sort_sys(subj):
    return subj["amount"]


#function for reading and returning the contents in book file
def getting_text(path):

    with open(path) as f:
        contents = f.read()
    return contents

main()
