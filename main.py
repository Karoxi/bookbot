import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()
    
def print_report(path_to_book):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(get_book_text(path_to_book))} total words")
    print("--------- Character Count -------")
    #print(f"{get_num_chars(get_book_text("./books/frankenstein.txt"))}")
    final_list = sort_dict(get_num_chars(get_book_text(path_to_book)))
    for i in final_list:
     print(f"{i["char"]}: {i["num"]}")
    print("============= END ===============")

from stats import get_num_words, get_num_chars, sort_dict

def main():
    if len(sys.argv) != 2: 
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else: 
        print_report(sys.argv[1])
    
    
    
main()