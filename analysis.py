import re
import string


def preproccess_text(text: str) -> str:
    """
    Функция для предварительной обработки текста.
    :param text: str
    :return: str
    """
    text = text.replace("ё", "е")
    text = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', 'URL', text)
    text = re.sub('@[^\s]+', 'USER', text)
    text = text.replace(",", " ")
    text = text.replace("&lt;", "<")
    text = text.replace("&gt;", ">")
    text = re.sub(' +', ' ', text)
    text = text.replace("\n", "")
    return text.strip()


def find_polarity(text: str, negative, positive: set(), set_type: str) -> dict():
    """
    Функция для поиска в тексте "полярных" слов или смайликов.
    Полярных - значит противоположных по тональности:
    добрый <-> злой или :) <-> :(
    Возвращает словарь с двумя списками.
    :param text: str
    :param negative: set()
    :param positive: set()
    :param set_type: str
    :return: dict()
    """
    assert len(negative) > 0 or len(positive), "Наборы не должны быть пустыми"
    assert set_type in ["words", "smiles"], "Допустимы два значения set_type: words или smiles"

    if set_type == "words":
        neg1w = [neg for neg in negative if neg.count(" ") == 0]  # набор из одного слова
        neg2w = [neg for neg in negative if neg.count(" ") > 0]  # набор из двух и более слов
        # pos1 = list(filter(lambda x: x.count(" ") == 0), positive)
        pos1w = [pos for pos in positive if pos.count(" ") == 0]
        pos2w = [pos for pos in positive if pos.count(" ") > 0]

        # преобразование текста в набор и поиск слова в наборе
        # текст приводится к нижнему регистру только в этом блоке,
        # при поиске тональных слов
        # иначе будут преобразованы смайлики ( =D ---> =d )
        text = text.lower()
        text = re.sub('[^a-zA-Zа-яА-Я1-9]+', ' ', text)
        text = re.sub(' +', ' ', text)
        text = text.strip(string.punctuation)
        text_set = set(text.split(" "))
        neg = [t for t in text_set if t in neg1w]
        pos = [t for t in text_set if t in pos1w]

        # поиск многословных тональных выражений в тексте
        neg += [word for word in neg2w if word in text]
        pos += [word for word in pos2w if word in text]
    else:
        neg = [neg for neg in negative if neg in text]
        pos = [pos for pos in positive if pos in text]

    return {"negative": neg, "positive": pos}
