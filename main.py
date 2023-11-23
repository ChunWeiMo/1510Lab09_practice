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
        words_count.items(), key=lambda x: x[1], reverse=True)
    return sorted_words_list


def ask_input_order():
    order = input('Enter a positive integer: ')
    try:
        order = int(order)
        return order
    except ValueError:
        print("Please enter an integer")
        


def check_input_order(order):
    if order < 1:
        raise ValueError

def print_input_order(order, sorted_words_list):
    ones = order % 10
    if order == 11:
        print(f'The {order}th most frequent word in this file is:')
    elif order == 12:
        print(f'The {order}th most frequent word in this file is:')
    elif order == 13:
        print(f'The {order}th most frequent word in this file is:')
    elif ones == 1:
        print(f'The {order}st most frequent word in this file is:')
    elif ones == 2:
        print(f'The {order}nd most frequent word in this file is:')
    elif ones == 3:
        print(f'The {order}rd most frequent word in this file is:')
    else :
        print(f'The {order}th most frequent word in this file is:')
    print(f'{sorted_words_list[order-1][0]} {sorted_words_list[order-1][1]}')


def main():
    # url = "https://www.gutenberg.org/cache/epub/72013/pg72013.txt"  # the book I pick
    url = "https://www.gutenberg.org/cache/epub/2554/pg2554.txt"  # Lab09 file
    # url = 'https://www.google.ca'
    # url = 'abc'
    words_list = get_words_list(url)
    if words_list:
        sorted_words_list = sorted_by_word_count(words_list)
        for order in range(10):
            print(
                f'{order+1}. {sorted_words_list[order][0]} {sorted_words_list[order][1]:,}')
        print()
        order = ask_input_order(sorted_words_list)
        try:
            check_input_order(order)
        except ValueError:
            print("Please enter a positive number")
        except TypeError:
            print("Please enter an integer")
        else:
            print_input_order(order, sorted_words_list)
        finally:
            print("\nPROGRAM END.")


if __name__ == '__main__':
    main()
