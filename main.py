def word_counter(text_to_count):
    words = text_to_count.split()
    return len(words)

def char_counter(text_to_count):
    char_count = {}
    lowered_text = text_to_count.lower()
    lowered_words = lowered_text.split()

    for word in lowered_words:
        for char in word:
            if char in char_count:
                char_count[char] = char_count[char] + 1
            else:
                char_count[char] = 1

    return char_count

def book_report(text_list, num_words):
    text_list.sort(reverse=True, key=sort_on)
    
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    for char in text_list:
        #print(char)
        print(f"The {char["char"]} character was found {char["count"]} times")
    print("--- End report ---")
    return 0

def sort_on(dict):
    return dict["count"]

def dict_to_list_of_alpha_chars(dict):
    new_list = []
    for d in dict:
        if d.isalpha():
            temp_dict = {"char": d, "count": dict[d]}
            new_list.append(temp_dict)
    
    return new_list

def main():
    with open("books/frankenstein.txt") as f:
        book_content = f.read()
        
    word_count = word_counter(book_content)
    char_dict = char_counter(book_content)

    #print(dict_to_list_of_alpha_chars(char_dict))
    list_char = dict_to_list_of_alpha_chars(char_dict)

    book_report(list_char, word_count)

main()