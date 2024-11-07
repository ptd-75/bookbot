def count_words(file_contents):
    words = file_contents.split()
    print(len(words))
    
def main():
    with open("books/frankenstein.txt") as f:
        # ...
        file_contents = f.read()
    print(file_contents)
    count_words(file_contents)

main()