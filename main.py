import re

with open('english2.txt') as file:
    words = file.readlines()

words = [word.rstrip() for word in words]

ENGLISH_LETTER_FREQ = 'jqxzwvfybhkmpgudclotnraise'


def words_score(word):
    score = 0
    for letter in word:
        score += ENGLISH_LETTER_FREQ.index(letter)
    return [score, word]


def find_word_format(word_format):
    pattern = ''
    for char in word_format:
        if char == '_':
            pattern += '\w'
        else:
            pattern += char
    return pattern


filtering_5letter_word_pattern = re.compile('^[a-z]{5}$')
word_with_5letter = list(filter(filtering_5letter_word_pattern.match, words))
word_without_repeated_letter = [word for word in word_with_5letter if len(word) == len(set(list(word)))]


def finding_correct_word():
    sorted_freq_word = sorted(list(map(words_score, word_without_repeated_letter)), reverse=True)

    print('first 15 high score words'.center(50, '*'))
    for word in sorted_freq_word[:5]:
        print(" ")
        print(f'word: {word[1]}, score: {word[0]}')
        print(" ")
        print('=' * 50)

    sorted_freq_word = list(map(lambda x: x[1], sorted_freq_word))
    print('*' * 50)
    print('''Enter your letters if you want filtering words with specific letters
    (e.g. "abc" for filtering every word with one of these letters)
    or enter specific format (e.g. "--i-e" for word "raise"''')

    every_usr_input = ''
    input_for_filtering = input('\nType your letters or word format >>>>>>>>>> ')

    should_continue = True
    while should_continue:
        if input_for_filtering.isalpha():
            usr_pattern = "^[^" + input_for_filtering + "]{5}$"
        else:
            usr_pattern = find_word_format(input_for_filtering)

        filtering_word_with_user_pattern = re.compile(usr_pattern)
        words_filtered_with_usr_input = list(filter(filtering_word_with_user_pattern.match, sorted_freq_word))

        print(' ')
        for num, word in enumerate(words_filtered_with_usr_input[:15], start=1):
            print(f'{num}- {word}')

        if input('\nType "y" to continue with your current filtered words for finding correct word or "n" to start from the beginning.>>>') == 'y':
            sorted_freq_word = words_filtered_with_usr_input
            every_usr_input += '/' + input_for_filtering
            input_for_continue_filtering = input(f'you can continue hear: {every_usr_input} >>>')
            input_for_filtering = input_for_continue_filtering
        else:
            should_continue = False
            finding_correct_word()


if __name__ == '__main__':
    finding_correct_word()
