def get_num_words(document):
    return len(document.split())


def count_words(document):
    words = document.split()
    word_count = {}
    for word in words:
        lower_word = word.lower()
        for char in lower_word:
            if (char in word_count):
                word_count[char] += 1
            else:
                word_count[char] = 1
    return word_count


def get_sorted_word_count_list(char_map):
    items = char_map.items()
    sorted_items = sorted(items, key=lambda x: x[1], reverse=True)
    return sorted_items
