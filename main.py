from stats import count_words
import sys

def main():
    if len(sys.argv) < 2:
        print ("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_book = sys.argv[1]
    print (path_to_book)
    content = read_contents(path_to_book)
    
    prep_content = prepare_text(content)
    dict = process_char_dict(prep_content)
    sorted = sort_dict(dict)
    print_report(content, sorted, path_to_book)


def read_contents(path_to_book):    
    with open(path_to_book) as f:
        file_contents = f.read()
    return (file_contents)

def prepare_text(file_contents):
    lowered_file_contents = file_contents.lower()
    return lowered_file_contents

def process_char_dict(lower):

    char_dict = {}

    for c in lower:
        if c not in char_dict:
            char_dict[f"{c}"] = 1
        else:
            char_dict[f"{c}"] += 1
    return char_dict
def sort_on(dict):
        return dict["num"]
def sort_dict(dict):
    
    char_list = []
    for value in dict:
        if value.isalpha():
            char_list.append({"key":f"{value}", "num":dict[value]})
    char_list.sort(reverse=True, key=sort_on)
    return char_list
    
    
def print_report(content, sorted, path_to_book):
    print(f"--- Begin report of {path_to_book} ---\n")
    count_words(content)
    for e in sorted:
        print(f"{e["key"]}: {e["num"]}")
    print("--- End of Report ---\n")
main()