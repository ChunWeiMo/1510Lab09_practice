import requests


def get_words_list(url):
    try:
        response = requests.get(url)
    except requests.exceptions.MissingSchema:
        print("Enter a correct URL")
        return
    
    whole_book = response.text
    whole_book = whole_book.lower().rstrip().lstrip()
    marks = [',', '.', '?', '!', '(', ')', '-',
             '――', ':', '“', '”', '"', ';', '‘', ]
    for mark in marks:
        whole_book = whole_book.replace(mark, ' ')

    words = whole_book.split()
    return words


def get_value(word):
    return word[1]


def sorted_by_word_count(words_list):
    words_count = dict()
    for word in words_list:
        try:
            words_count[word] += 1
        except KeyError:
            words_count[word] = 1
    sorted_words_list = sorted(
        words_count.items(), key=get_value, reverse=True)
    return sorted_words_list


def ask_place(sorted_words_list):
    place = input('Enter a positive integer: ')    
    try:
        place = int(place)
    except ValueError:
        print("Please enter an integer")
        return
    
    print(f'The {place}th most frequent word in this file is:')
    try:
        print(f'{sorted_words_list[place-1][0]} {sorted_words_list[place-1][1]}')
    except IndexError:
        print("The input number is out of list length")
        



def main():
    url = "https://www.gutenberg.org/cache/epub/72013/pg72013.txt"
    # url='abc'
    words_list = get_words_list(url)
    sorted_words_list = sorted_by_word_count(words_list)

    for order in range(10):
        print(
            f'{order+1}. {sorted_words_list[order][0]} {sorted_words_list[order][1]:,}')
    ask_place(sorted_words_list)
    
    


if __name__ == '__main__':
    main()
