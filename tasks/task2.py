from typing import TextIO, Dict


def save_row(n1: int, p1: int, tone_dict: Dict[str, str], line: str) -> None:
    """
    Функция для решения задачи № 2:
    выгрузить в отдельный файл строку, которая содержит по крайней мере
    два слова противоположной тональности

    :param n1: int
    :param p1: int
    :param tone_dict: Dict[str, str]
    :param line: str
    :param file2: TextIO
    :return: None
    """
    # negative words + positive words
    if n1 > 0 and p1 > 0:
        with open("files_result/two_tokens.csv", "a") as file2:
            file2.write(f'{line}"|"'
                        f'{",".join(tone_dict["positive"])}"|"'
                        f'{",".join(tone_dict["negative"])}\n')
