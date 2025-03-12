def count_words(book_text):
    return len(book_text.split())

def count_chars(book_text):
    char_counts = {}
    for char in book_text:
        char_lower = char.lower()
        if char_lower in char_counts.keys():
            char_counts[char_lower] += 1
        else:
            char_counts[char_lower] = 1
    return char_counts

def stats_list(char_dict):
    sorted_dict = sorted(char_dict.items(), key=lambda item: item[1], reverse=True)
    
    for entry in sorted_dict:
        if entry[0].isalpha():
            print(f"{entry[0]}: {entry[1]}")