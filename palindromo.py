def palindromo(word):
    word = word.replace(' ', '').lower()
    word_inverse = word[::-1]
    if word == word_inverse:
        return True
    else:
        return False


def run():
    word = input('Hi, please type a word: ')
    if palindromo(word) == True:
        print('Yes, it is a palindromo word')
    else:
        print('No, it is not a palindromo word, try another word')


if __name__ == '__main__':
    run()