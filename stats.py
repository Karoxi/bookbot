def get_num_words(string_text):
    wordlist = string_text.split()
    return len(wordlist)

def get_num_chars(string_text):
    string_text = string_text.lower()
    char_dict = {}
    for char in string_text:
        if char not in char_dict: 
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict

def sort_dict(char_num_dict):
    dict_list = []
    for i in char_num_dict: 
        newdict = {}
        newdict["char"] = i
        newdict["num"] = char_num_dict[i]
        dict_list.append (newdict)
        dict_list.sort(reverse=True, key=lambda d: d["num"])
    return dict_list
    