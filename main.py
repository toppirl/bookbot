from stats import word_count, char_count, sorted_count
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    if(len(sys.argv) != 2):
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = word_count(text)
    chars = char_count(text)
    sort_this = sorted_count(chars)
    print(f'============ BOOKBOT ============')
    print(f'Analyzing book found at {book_path}...')
    print(f'----------- Word Count ----------')
    print(f'Found {num_words} total words')
    print(f'--------- Character Count -------')
    for obj in sort_this:
        for char in obj:
            count = obj[char]
            if char.isalpha():
                print(f'{char}: {count}')
    print(f'============= END ===============')
main()



