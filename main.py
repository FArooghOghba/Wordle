import re

with open('english2.txt') as file:
    words = file.readlines()

words = [word.rstrip() for word in words]

ENGLISH_LETTER_FREQ = 'jqxzwvfybhkmpgudclotnraise'


def words_score(word):  # Find every word score with english letter frequency .
    score = 0
    for letter in word:
        score += ENGLISH_LETTER_FREQ.index(letter)
    return [score, word]


filtering_5letter_word_pattern = re.compile('^[a-z]{5}$')
word_with_5letter = list(filter(filtering_5letter_word_pattern.match, words))
word_without_repeated_letter = [word for word in word_with_5letter if len(word) == len(set(list(word)))]


def finding_correct_word():
    sorted_freq_word = sorted(list(map(words_score, word_without_repeated_letter)), reverse=True)

    print(' First 15 HIGH SCORE words '.center(50, '*'))
    print(f"About {len(sorted_freq_word)} words")
    for word in sorted_freq_word[:5]:
        print()
        print(f'word: {word[1]}, score: {word[0]}')
        print()
        print('=' * 50)

    sorted_freq_word = list(map(lambda x: x[1], sorted_freq_word))
    print('*' * 50)
    print('''Enter your letters if you want to filter the words that have these letters that you enter:
    (e.g. "abc" to filter every word with one of these letters)
    , A special format for words has these letters in a certain place:
    (e.g. "--i-e" for word "raise")
    or words whose letters are known but the position of the letters is not known:
    (e.g. "ra?s?" for word "shard")''')

    every_usr_input = ''
    input_for_filtering = input('\nType your letters or word format >>>>>>>>>> ')

    should_continue = True
    while should_continue:
        if input_for_filtering.isalpha():  # If True It's going to filter just specific letter
            usr_pattern = "^[^" + input_for_filtering + "]{5}$"
        elif '_' in input_for_filtering:  # If True It's going to filter words with specific format
            usr_pattern = input_for_filtering.replace('_', '.')
        elif '?' in input_for_filtering:  # If True It's going to filter word with unknown letter position
            pattern = input_for_filtering.replace('?', '.')
            usr_pattern = '^' + ''.join(f'[^{char}]' if char.isalpha() else '.' for char in pattern) + '$'
        else:
            print('Enter correct pattern!!!')
            break

        filtering_word_with_user_pattern = re.compile(usr_pattern)
        words_filtered_with_usr_input = list(filter(filtering_word_with_user_pattern.match, sorted_freq_word))

        print('#' * 50)
        print(f'The number of words reduced to {len(words_filtered_with_usr_input)} word.')
        print('-' * 20)
        for num, word in enumerate(words_filtered_with_usr_input[:25], start=1):
            print(f'{num}- {word}')

        if input('\nType "n" to start from the beginning or "y" to continue with your current filtered words for finding correct word.>>>') == 'y':
            sorted_freq_word = words_filtered_with_usr_input
            every_usr_input += '|' + input_for_filtering
            print()
            input_for_continue_filtering = input(f'you can continue hear: {every_usr_input} >>>')
            input_for_filtering = input_for_continue_filtering
        else:
            should_continue = False
            finding_correct_word()


if __name__ == '__main__':
    finding_correct_word()
