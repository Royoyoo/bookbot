import string

def main():
    path_to_file = "books/frankenstein.txt"

    with open(path_to_file) as f:
        file_contents = f.read()

    print(f"--- Begin report of {path_to_file} ---")    
    print(f"{count_words(file_contents)} words found in the document")
    print("")    
    print_chars(count_chars(file_contents))
    print(f"--- End report ---")    


def count_words(content):
    return len(content.split())

def count_chars(content):
    char_dict = {}

    for char in content.lower():

        if(char in char_dict):
            char_dict[char] += 1
        else:
            char_dict[char] = 1

    return char_dict

def print_chars(char_dict):
    for char in string.ascii_lowercase:

        count = 0
        if char in char_dict:
            count = char_dict[char]
        
        print(f"The '{char}' character was found {count} times")

main()