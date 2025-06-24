def count_words(book_text):
    words = book_text.split()
    count = 0
    
    for word in words:
        count += 1
    return count

def count_chars(book_text):
    chars = book_text.lower()
    char_dict = {}
    
    for char in chars:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_on(char_list):
    letter, count = char_list
    return count

def sorted_list(char_dict):
    char_list = list(char_dict.items())
    char_list.sort(reverse=True, key=sort_on)
    char_sorted_list = []

    for item in char_list:
        char_dict_item = {}
        char_dict_item["char"] = item[0]
        char_dict_item["num"] = item [1]
        char_sorted_list.append(char_dict_item)    
    return char_sorted_list
