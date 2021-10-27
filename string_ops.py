def remove_vowels(word):
    vowels = 'aeiouy'
    new_word = ''
    for character in word:
        if character.lower() not in vowels:
            new_word += character
    return new_word

def reversed_string(word):
    return word[::-1]


def main():
    print(remove_vowels('christmas'))
    print(reversed_string('republic'))


if __name__ == '__main__':
    main()
