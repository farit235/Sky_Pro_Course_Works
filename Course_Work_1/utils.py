import random
from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings
import requests
import basic_word

disable_warnings(InsecureRequestWarning)


def load_random_word(link):
    response = requests.get(link, verify=False).json()
    word = random.sample(response, 1)
    instance_word = basic_word.BasicWord(word[0]['word'], word[0]['subwords'])
    return instance_word


