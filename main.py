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


def filter_words_with_pattern(pattern, current_words):
    user_pattern = re.compile(pattern)
    return list(filter(user_pattern.match, current_words))


filtering_5letter_word_pattern = re.compile('^[a-z]{5}$')
word_with_5letter = list(filter(filtering_5letter_word_pattern.match, words))


def finding_correct_word():
    sorted_freq_word = sorted(list(map(words_score, word_with_5letter)), reverse=True)
    sorted_freq_word = list(map(lambda x: x[1], sorted_freq_word))

    print(' This program helps you choose the right words for your "WORDLE" game '.center(80, '*'))
    if input('\nWant to filter words with duplicate letters? (enter "y" for accept): ') == 'y':
        sorted_freq_word = [word for word in sorted_freq_word if len(word) == len(set(list(word)))]

    print(' HIGHEST SCORE WORD '.center(50, '*'))
    print(f'word: {sorted_freq_word[0]}')
    print(f"From about {len(sorted_freq_word)} words")
    print('=' * 50)

    print('Enter your guess word RESULT like "x" for wrong letter, "y" for correct letter with unknown position and "g" for correct letter.')
    print('(e.g. leant : yyyxg ) and the correct word is "pleat"')

    should_continue = True
    while should_continue:
        guess_word = input('\nEnter your guess word >>>>>>>>>> ')
        guess_result = input('Enter your guess result >>>>>>>>>> ')

        if guess_result:
            if 'x' in guess_result:  # "x": All words that have the letters marked with an X will be removed
                x_indices = [span.start() for span in re.finditer('x', guess_result)]
                input_for_filtering_x = ''.join([guess_word[i] for i in x_indices])
                x_pattern = "^[^" + input_for_filtering_x + "]{5}$"
                words_filtered_with_usr_input_x = filter_words_with_pattern(x_pattern, sorted_freq_word)
                sorted_freq_word = words_filtered_with_usr_input_x
            if 'y' in guess_result:  # "y": All words that have the letters marked with y in the y position will be deleted
                y_indices = [span.start() for span in re.finditer('y', guess_result)]
                input_for_filtering_y = ''.join([guess_word[i] for i in y_indices])
                y_pattern = '^' + ''.join(f'[^{char}]' if char in input_for_filtering_y else '.' for char in guess_word) + '$'
                words_filtered_with_usr_input_y = filter_words_with_pattern(y_pattern, sorted_freq_word)
                sorted_freq_word = words_filtered_with_usr_input_y
            if 'g' in guess_result:  # "g": All words that do not have the letters marked with a g in position g will be deleted
                g_indices = [span.start() for span in re.finditer('g', guess_result)]
                input_for_filtering_g = ''.join([guess_word[i] for i in g_indices])
                g_pattern = '^' + ''.join(char if char in input_for_filtering_g else '.' for char in guess_word) + '$'
                words_filtered_with_usr_input_g = filter_words_with_pattern(g_pattern, sorted_freq_word)
                sorted_freq_word = words_filtered_with_usr_input_g
        else:
            print('Enter correct word or pattern!!!')
            break

        print('#' * 50)
        print(f'The number of words reduced to {len(sorted_freq_word)} word.')
        print('-' * 20)
        for num, word in enumerate(sorted_freq_word[:25], start=1):
            print(f'{num}- {word}')

        if input('\nType "n" to start from the beginning or "y" to continue with your current filtered words for finding correct word.>>>') == 'y':
            print()
        else:
            should_continue = False
            finding_correct_word()


if __name__ == '__main__':
    finding_correct_word()
