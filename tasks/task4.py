from typing import TextIO, Dict


def save_row(n1: int, p1: int, n2: int, p2: int, smile_dict: Dict[str, str], line: str) -> None:
    """
    Функция для решения задачи № 4:
    выгрузить в отдельный файл строку, которая содержит
    смайлик, но не содержит оценочные слова

    :param n1: int
    :param p1: int
    :param n2: int
    :param p2: int
    :param smile_dict: Dict[str, str]
    :param line: str
    :return: None
    """

    # any smile without negative and positive words
    if (n2 > 0 or p2 > 0) and (n1 == 0 and p1 == 0):
        smiles = "\t".join(smile_dict["positive"] + smile_dict["negative"])
        with open("files_result/emotikon_no_token.csv", "a") as file4:
            file4.write(f'{line}"|"{smiles}\n')