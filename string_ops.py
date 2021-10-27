def remove_vowels(word):
    vowels = 'aeiouy'
    new_word = ''
    for character in word:
        if character.lower() not in vowels:
            new_word += character
    return new_word


def reversed_string(word):
    return word[::-1]


def translate_to_robber(text):
    vowels = 'aeiouy'
    robber_str = ''

    for c in text:
        if c not in vowels and c.isalpha():
            robber_str += c + 'o' + c
        else:
            robber_str += c

    return robber_str


def main():
    print(remove_vowels('christmas'))
    print(reversed_string('republic'))


if __name__ == '__main__':
    main()
