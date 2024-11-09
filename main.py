file_path = "books/frankenstein.txt"

def count_words(file_contents):
    words = file_contents.split()
    return (len(words))

def sort_on(dict):
    return dict["num"]

def main():
    with open(file_path) as f:
        # ...
        file_contents = f.read()
    # print(file_contents)
    word_count = count_words(file_contents)

    lowered_string = file_contents.lower()
    character_counts = {}
    for char in lowered_string:
        if char.isalpha():   # Only count the character if it's a letter
            if char in character_counts:
                character_counts[char] += 1
            else:
                character_counts[char] = 1
    # print(character_counts)

    # After the counting loop finishes...
    chars_list = []  # Create an empty list
    for char, count in character_counts.items():  # Loop through your dictionary
        # Create a dictionary for each character with "char" and "num" keys
        char_dict = {"char": char, "num": count}
        # Add this dictionary to your list
        chars_list.append(char_dict)

    # Sort the list here!
    chars_list.sort(reverse=True, key=sort_on)

# begin report output
    print(f"--- Begin report of {file_path} ---")
    print(f"{word_count} words found in the document")
    print() # blank line for spacing

    # loop through sorted chars_list
    for char_dict in chars_list:
        print(f"The '{char_dict['char']}' character was found {char_dict['num']} times")
    
    print("--- End report ---")    

main()