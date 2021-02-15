from typing import TextIO, Dict


def save_row(text: str, n2: int, p2: int, smile_dict: Dict[str, str], line: str) -> None:
    """
    Функция для решения задачи № 3:
    выгрузить в отдельный файл строку, которая содержит
    частицу "не" или "ни" и смайлик

    :param text: str
    :param n2: int
    :param p2: int
    :param smile_dict: Dict[str, str]
    :param line: str
    :return: None
    """

    text_set = set(text.lower().split(" "))

    if n2 > 0 and p2 > 0:
        smiles = "\t".join(smile_dict["positive"] + smile_dict["negative"])
        with open("files_result/not_token.csv", "a") as file3:
            # "не" + "ни" + any smile
            if "не" in text_set and "ни" in text_set:
                file3.write(f'{line}"|"не,ни"|"{smiles}\n')

            # "не" + any smile
            elif "не" in text_set:
                file3.write(f'{line}"|"не"|"{smiles}\n')

            # "ни" + any smile
            elif "ни" in text_set:
                file3.write(f'{line}"|"ни"|"{smiles}\n')

