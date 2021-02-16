from typing import Dict


def save_row(n2: int, p2: int, smile_dict: Dict[str, str], line: str) -> None:
    """
    Функция для решения задачи № 5:
    выгрузить в отдельный файл строку, которая содержит
    смайлики двух разных тональностей  =) и :[

    :param n2: int
    :param p2: int
    :param smile_dict: Dict[str, str]
    :param line: str
    :return: None
    """
    # two different smiles
    if n2 > 0 and p2 > 0:
        smiles_pos = "\t".join(smile_dict["positive"])
        smiles_neg = "\t".join(smile_dict["negative"])
        with open("files_result/two_emotikons.csv", "a") as file5:
            file5.write(f'{line}"|"'
                        f'{smiles_pos}"|"'
                        f'{smiles_neg}\n')