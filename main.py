from stats import count_words, count_chars, stats_list
import sys

def get_book_text(path):
    with open(path) as f:
        read_data = f.read()
    return read_data

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else: 
        file_location = sys.argv[1]
        file_contents =  get_book_text(file_location)
        num_words = count_words(file_contents)
        num_chars = count_chars(file_contents)

        print("\n")
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {file_location}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        stats_list(num_chars)
        print("============= END ===============")
        print("\n")
        
main()