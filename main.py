import sys

from stats import get_num_words, count_words, get_sorted_word_count_list


def get_book_test(filePath):
    with open(filePath) as file:
        content = file.read()
        return content


def main():
    entries = sys.argv
    if (len(entries) < 2):
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)
    path = sys.argv[1]
    content = get_book_test(path)
    word_count = get_num_words(content)
    char_map = count_words(content)
    sorted_char_list = get_sorted_word_count_list(char_map)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print('----------- Word Count ----------')
    print(f'Found {word_count} total words')
    print("--------- Character Count -------")

    for item in sorted_char_list:
        if item[0].isalpha():
            print(f'{item[0]}: {item[1]}')

    print("============ END ===============")


main()
