class Player:

    def __init__(self, name, used_words):
        self.name = name
        self.used_words = used_words

    def count_used_words(self):
        """Функция подсчета использованных слов"""
        return len(self.used_words)

    def add_used_word(self, word):
        """Функция добавления слова в использованные слова"""
        self.used_words.append(word)

    def check_used_word(self, word):
        """Функция проверки слова до этого момента"""
        if word in self.used_words:
            return True
        else:
            return False

    def __repr__(self):
        print(f"Пользователь: {self.name} и использованные слова {self.used_words}")
