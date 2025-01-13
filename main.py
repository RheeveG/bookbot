def main():
    content = read_contents()
    
    prep_content = prepare_text(content)
    dict = process_char_dict(prep_content)
    sorted = sort_dict(dict)
    print_report(content, sorted)


def read_contents():    
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    return (file_contents)

def count_words(file_contents):
    words = file_contents.split()
    total = 0
    for word in words:
        total += 1
    print (f"The text has a total of {total} words")

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
    
    
def print_report(content, sorted):
    print("--- Begin report of books/frankenstein.txt ---\n")
    count_words(content)
    for e in sorted:
        print(f"The '{e["key"]}' character was used {e["num"]} times.")
    print("--- End of Report ---\n")
main()