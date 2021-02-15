from typing import TextIO, Dict


def save_row(n1: int, p1: int, n2: int, p2: int, tone_dict: Dict[str, str], smile_dict: Dict[str, str], line: str) -> None:
    """
    Функция для решения задачи № 1:
    выгрузить в отдельный файл строку, которая содержит
    смайлик и слово противоположной тональнсоти к смайлику

    :param n1: int
    :param p1: int
    :param n2: int
    :param p2: int
    :param tone_dict: Dict[str, str]
    :param smile_dict: Dict[str, str]
    :param line: str
    :return: None
    """

    # positive word + negative smile
    if p1 > 0 and n2 > 0:
        smiles = "\t".join(smile_dict["negative"])
        with open("files_result/emotikon_token.csv", "a") as file1:
            file1.write(f'{line}"|"'
                        f'{smiles}"|"'
                        f'{",".join(tone_dict["positive"])}\n')

    # negative word + positive smile
    if n1 > 0 and p2 > 0:
        smiles = "\t".join(smile_dict["positive"])
        with open("files_result/emotikon_token.csv", "a") as file1:
            file1.write(f'{line}"|"'
                        f'{smiles}"|"'
                        f'{",".join(tone_dict["negative"])}\n')
