import requests


def get_words_list(url):
    try:
        response = requests.get(url)
    except requests.exceptions.MissingSchema:
        print("Enter a correct URL")
        return
    whole_book = response.text
    whole_book = whole_book.lower().rstrip().lstrip()
    
    whole_book_no_punctuation = ''
    for character in whole_book:
        if character.isalnum() == False:
            character = ' '
        whole_book_no_punctuation += character   

    words = whole_book_no_punctuation.split()
    return words


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
    except ValueError:
        print("Please enter an integer")
    else:
        if order < 1:
            raise ValueError
        else:
            return order
        
    

def print_input_order(order, sorted_words_list):
    try:
        sorted_words_list[order-1]
    except IndexError:
        print('Input is out of words list range.')
    except TypeError:
        print('Order must be an integer')
    else:
        print(f'The {order}th most frequent word in this file is:')
        print(f'{sorted_words_list[order-1][0]} {sorted_words_list[order-1][1]}')


def main():
    # url = "https://www.gutenberg.org/cache/epub/2554/pg2554.txt"  # Lab09 file
    url = "https://www.gutenberg.org/cache/epub/72013/pg72013.txt"  # the book I pick
    words_list = get_words_list(url)
    if words_list:
        sorted_words_list = sorted_by_word_count(words_list)
        for order in range(10):
            print(
                f'{order+1}. {sorted_words_list[order][0]} {sorted_words_list[order][1]:,}')
        print()

        try:
            order = ask_input_order()
        except ValueError:
            print("Pleas enter a positive number.")
        else:
            print_input_order(order, sorted_words_list)
        finally:
            print("\nPROGRAM END.")
    

if __name__ == '__main__':
    main()
