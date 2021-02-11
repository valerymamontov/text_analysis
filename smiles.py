def get_smiles(path_to_file: str) -> set():
    """
    Функция построчно считывает файл и записывает из него все смайлики.
    Возвращает набор уникальных элементов (множество)
    :param path_to_file: str
    :return: set()
    """
    smiles_set = set()
    with open(path_to_file, encoding="cp1251") as file:
        for row in file:
            smile = row.split('"|"')[0]
            smiles_set.add(smile)
    return smiles_set


smiles_negative = get_smiles("files/smiles_negative.txt")
smiles_positive = get_smiles("files/smiles_positive.txt")
