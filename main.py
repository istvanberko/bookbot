

def main():
    path_to_file = "/Users/istvan.berko/workspace/github.com/istvanberko/bookbot/books/frankenstein.txt"
    with open(path_to_file) as f:
        file_content = f.read()
    print_character_values(count_characters(file_content))


def count_words(fcontent):
    words = fcontent.split()
    return len(words)

def count_characters(fcontent):
    character_count = {}

    fcontent = fcontent.lower()
    
    for char in fcontent:
        if char in character_count and char.isalpha():
            character_count[char] += 1
        elif char.isalpha():
            character_count[char] = 1
        
    character_count = dict(sorted(character_count.items(), key=lambda item: item[1], reverse=True))
    return character_count

def print_character_values(ccount):
    for i in ccount:
        print(f"The '{i}' character was found {ccount[i]} times")

main()