from collections import Counter

def parse_book(path: str):
    final_word_count = 0
    final_char_count = Counter()
    with open(path, "r") as book:
        for line in book:
            final_word_count += count_words_line(line)
            final_char_count += count_char_line(line)

    generate_book_report(final_word_count, final_char_count, path)

def generate_book_report(word_count: int, char_count: Counter[str], path: str):
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document")
    print("")
    for char, count in char_count.most_common():
        if char.isalpha():
            print(f"The {char} character was found {count} times")

    print("--- End report ---")

def count_words_line(line: str) -> int:
    return len(line.strip().split())

def count_char_line(line: str) -> Counter[str]:
    word_list = line.strip().split()
    count = Counter(char for word in word_list for char in word.lower())

    return count

if __name__ == "__main__":
    parse_book("books/frankenstein.txt")