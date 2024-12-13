def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path) 
    word_count = get_word_count(text) 
    char_count = get_character_count(text)
    print(f"=== Report on {book_path} ===")

def get_book_text(path): 
    with open(path) as f:
        file_contents = f.read()
        return file_contents  

def get_word_count(text): 
    words = text.split()
    return len(words)

def get_character_count(text): 
    lower_string = text.lower() 
    character_list = list(lower_string) 
    character_count = {}
    for character in character_list: 
        character_count[character] = character_count.get(character, 0) + 1
    return character_count 

#def get_character_report(char_count): 
    #char_count_list = []
    

main() 