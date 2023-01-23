import player
import utils

DATA_SOURCE = 'https://jsonkeeper.com/b/MUFE'

username = input("Введите имя игрока: ")
player_1 = player.Player(username, [])
print(f"Привет, {player_1.name}!\n")

main_word = utils.load_random_word(DATA_SOURCE)
print(f"Составьте из слова '{main_word.word}' - {main_word.count_subwords()} слов!\n"
     f"Слова должны быть не короче 3 букв\n"
     f"Чтобы закончить игру напишите 'stop' или отгадайте все слова\n"
     f"Поехали! Напишите Ваше первое слово! ")

while True:
    if main_word.count_subwords() == player_1.count_used_words():
        print(f"Игра завершена, Вы угадали все {player_1.count_used_words()} слов\n")
        exit(0)
    word = input("Ваше слово: ")
    if word == "stop":
        print(f"Игра завершена, Вы угадали {player_1.count_used_words()} слово из {main_word.count_subwords()}\n")
        exit(0)
    elif len(word) <= 2:
        print("Нет слов менее 3 букв!\n")
    elif word not in main_word.subword_list:
        print("Неверное слово :(\n")
    elif word in player_1.used_words:
        print("Слово уже использовано :)\n")
    else:
        player_1.add_used_word(word)
        print("Слово добавлено в список использованных слов!\n")

