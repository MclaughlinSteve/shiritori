import constant

score = 0
previous_word = ''


def play():
    print('始めましょう。頑張ってください！')

    continue_playing = True
    while continue_playing:
        print('単語を書いてください')

        word = input().strip()
        last = extract_last_syllable(word)
        continue_playing = is_word_valid(last, word)
        if continue_playing:
            generate_response(last)

    ending_message = '君のスコアは{} ポイントでした。またゲームをしてください。'
    print(ending_message.format(score))


def extract_last_syllable(word):
    word_size = len(word)
    last = word[word_size - 1]
    if last in constant.SUBSCRIPTS:
        last = word[word_size - 2:]
    return last


def is_word_valid(last, word):
    if last in constant.INVALID_ENDINGS \
            or previous_word != '' and not word.startswith(extract_last_syllable(previous_word)):
        print('大変ですね。。。')
        return False
    return True


def generate_response(last):
    # TODO: Replace this if block with a function that does more than just this specific example case
    if last == 'じょ':
        global previous_word
        previous_word = 'じょうせい'
        print(previous_word)

    increment_score()


def increment_score():
    global score
    score += 1


play()
