import random 

def random_password():
    mayus = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
    minus = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    symbols = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    numbers = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']
    characters = mayus + minus + symbols + numbers
    password = []
    for i in range(15):
        characters_random = random.choice(characters)
        password.append(characters_random)

    password = ''.join(password)
    return password
        


def run():
    password = random_password()
    print('Your new password is ' + str(password)) 



if __name__ == '__main__':
    run()