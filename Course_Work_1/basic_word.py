class BasicWord:

    def __init__(self, word, subword_list):
        self.word = word
        self.subword_list = subword_list

    def input_check(self):
        """Проверка введенного слова со списком допустимых слов"""
        word = input("Введите слово: ")
        if word in self.subword_list:
            return True
        else:
            return False

    def count_subwords(self):
        """Подсчет количества подслов"""
        return len(self.subword_list)

    def __repr__(self):
        print(f"Правильное слово: {self.word}, список подслов - {self.subword_list}\n")
