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

        #We created a function for sorting, and what to sort. then pass it through it later in the .sort() method. Read documentation, if i forget

    sorted_list_of_dict.sort(reverse=True, key=sort_sys)
    return sorted_list_of_dict

def sort_sys(subj):
    return subj["amount"]