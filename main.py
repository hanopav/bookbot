def main():
    path = "books/frankenstein.txt"
    text = read_book(path)
    count_characters = counting(count_chars(text))
    count_alpha = counting(count_chars_alpha(text))
    words = count_words(text)
    report = reporting(count_chars_alpha(text))
    report.sort(reverse=True, key=sorting)
    print(f"\n--- Beginning of report about the publication located at {path} ---\n")
    print(f"There are {count_characters} characters, out of which {count_alpha} are alphabetical. There are {words} words in the text.\n\n")
    for i in report:
        print(f"The character {i["key"]} occurs {i["value"]} times\n")
    print("--- END REPORT---")

def read_book(path_to_file):
    with open(path_to_file) as f:
        text = f.read()
    return text

def counting(dict):
    count = 0
    for i in dict.values():
        count += i
    return count

def count_words(text):
    words = text.split()
    count = 0
    for i in words:
        count += 1
    return count

def count_chars(text):
    lower = text.lower()
    dict = {} 
    for i in lower:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    return dict

def count_chars_alpha(text):
    lower = text.lower()
    dict = {} 
    for i in lower:
        if i.isalpha() == True:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
    return dict

def reporting(dict):
    list_of_dicts = []
    for i in dict:
        list_of_dicts.append({"key" : i, "value" : dict[i]})
    return list_of_dicts

def sorting(dict):
    return dict["value"]

main()