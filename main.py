def count_words(file_contents):
    words = file_contents.split()
    print(len(words))

def main():
    with open("books/frankenstein.txt") as f:
        # ...
        file_contents = f.read()
    print(file_contents)
    count_words(file_contents)

    lowered_string = file_contents.lower()
    character_counts = {}
    for char in lowered_string:
        if char in character_counts:
            character_counts[char] += 1
        else:
            character_counts[char] = 1
    print(character_counts)

main()