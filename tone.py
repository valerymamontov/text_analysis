def get_tone_words(path_to_file: str) -> set():
    """
    Функция для построчного считывания файла и получения
    уникальных тональных слов
    :param path_to_file: str
    :return: set()
    """
    with open(path_to_file, encoding="cp1251") as file:
        tone_words = set()
        for line in file:
            line = line.replace("\n", "")
            tone_words.add(line)
    return tone_words


words_negative = get_tone_words("files/tone_negative.txt")
words_positive = get_tone_words("files/tone_positive.txt")
