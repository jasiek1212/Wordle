import requests
from constants import Constants

def format_word(word: str) -> dict[str, list[int]]:
    if word == "":
        raise ValueError("Word wasn't imported correctly")
    letter_list: dict = {}
    for index, letter in enumerate(word):
        if letter in letter_list:
            letter_list[letter].append(index)
            continue
        letter_list[letter] = [index]
    return letter_list

def generate_word(word_length: int = Constants.WORD_LENGTH) -> str:
    api_url = f"https://random-word-api.vercel.app/api?words=1&length={Constants.WORD_LENGTH}"

    response = requests.get(api_url)
    word = response.json()[0]

    return word

def check_if_exists(word: str) -> bool:
    api_url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"

    response = requests.get(api_url)
    response_json = response.json()

    if len(response_json) == 3:
        return False
    return True


