from tone import words_negative, words_positive
from smiles import smiles_negative, smiles_positive
from analysis import preproccess_text, find_polarity
from tasks import task1, task2, task3, task4, task5
import time
import datetime as dt

start_time = time.time()
empty_rows = 0
i = 0

print(f"Start: {dt.datetime.now()}")
with open("files/sentiment-10000.csv", encoding="utf-8") as file:
    for line in file:
        i += 1
        try:
            line = bytes(line, "utf-8")
            line = line.decode("utf-8", "ignore")

            text = line.split('"|"')[3]
            text = preproccess_text(text)

            if len(text) > 1:
                tone_dict = find_polarity(text, words_negative, words_positive, "words")
                smile_dict = find_polarity(text, smiles_negative, smiles_positive, "smiles")
                n1, p1 = len(tone_dict["negative"]), len(tone_dict["positive"])
                n2, p2 = len(smile_dict["negative"]), len(smile_dict["positive"])

                line = line.replace("\n", "")

                task1.save_row(n1, p1, n2, p2,
                               tone_dict,
                               smile_dict,
                               line)

                task2.save_row(n1, p1, tone_dict, line)
                task3.save_row(text, n2, p2, smile_dict, line)
                task4.save_row(n1, p1, n2, p2, smile_dict, line)
                task5.save_row(n2, p2, smile_dict, line)
            else:
                empty_rows += 1
                with open("files_result/!empty_rows.csv", "a") as f:
                    f.write(line)

        except Exception as ex:
            print(f"error on row:\t\t{i}, current time: {dt.datetime.now()}")
            print(ex)
            print(line)
            print(f"time:\t{(time.time() - start_time) / 60}")


print(f"Finish: {dt.datetime.now()}")
print(f"Empty rows: {empty_rows}")
print(f"Total time: {(time.time() - start_time) / 60}")
