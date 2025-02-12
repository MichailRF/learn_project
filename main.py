import random


def input_data():

    words = ["code", "bit", "list", "soul", "next"]
    return words


def morse_encode(word, morse_code):
    """
    переводит английские слов в последовательность точек и тире
    :param morse_code:
    :param word:
    :return: строки морзянки
    """
    word_encoded = []

    for letter in word:
        word_encoded.append(morse_code.get(letter, ""))
    return " ".join(word_encoded)


def get_word(words):

    """
    получает случайное слово из списка
    :return: строка слова
    """

    return random.choice(words)


def print_statistics(answers):
    """
    на основе списка answers выводит статистику
    :param answers: список верности ответов
    """

    answers_total = len(answers)
    answers_correct = sum(answers)
    answers_incorrect = answers_total - answers_correct
    print(f"Всего задачек: {answers_total}\nРешено верно: {answers_correct}\nРешено неверно: {answers_incorrect}")


def main():
    morse_code = {
        "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....",
        "7": "--...", "8": "---..", "9": "----.", "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".",
        "f": "..-.", "g": "--.", "h": "....", "i": "..", "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.",
        "o": "---", "p": ".--.", "q": "--.-", "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--",
        "x": "-..-", "y": "-.--", "z": "--..", ".": ".-.-.-", ",": "--..--", "?": "..--..", "!": "-.-.--",
        "-": "-....-",
        "/": "-..-.", "@": ".--.-.", "(": "-.--.", ")": "-.--.-"}

    answers = []

    print("Сегодня мы потренируемся расшифровывать азбуку морзе")
    input("Нажмите enter")

    words = input_data()

    for i in range(len(words)):
        word = get_word(words)
        word_morse = morse_encode(word, morse_code)

        user_input = input(f"Слово - {i+1} {word_morse}\n")

        if user_input.lower() == word:
            print(f"Верно {word}\n")
            answers.append(True)
        else:
            print(f"Неверно {word}\n")
            answers.append(False)

    print_statistics(answers)


main()
