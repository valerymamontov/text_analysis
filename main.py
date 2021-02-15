from tone import words_negative, words_positive
from smiles import smiles_negative, smiles_positive
from analysis import preproccess_text, find_polarity
from tasks import task1, task2, task3, task4, task5
import time
import datetime as dt

start_time = time.time()
empty_rows = 0
i = 0

print("Start:", dt.datetime.now())
with open("files/sentiment.csv", mode="r", encoding="utf-8") as file:
    for line in file:
        try:
            # decode unicode and resave line's content
            line = bytes(line, "utf-8")
            line = line.decode("utf-8", "ignore")

            text = line.split('"|"')[3]
            text = preproccess_text(text)

            # skip any row which contains one symbol
            if len(text) > 1:

                tone_dict = find_polarity(text, words_negative, words_positive, "words")
                smile_dict = find_polarity(text, smiles_negative, smiles_positive, "smiles")
                n1, p1 = len(tone_dict["negative"]), len(tone_dict["positive"])
                n2, p2 = len(smile_dict["negative"]), len(smile_dict["positive"])

                line = line.replace("\n", "")

                # task 1:
                # negative word + positive smile
                # positive word + negative smile
                task1.save_row(n1, p1, n2, p2,
                               tone_dict,
                               smile_dict,
                               line)

                # task 2 (negative words + positive words)
                task2.save_row(n1, p1, tone_dict, line)

                # task 3 ("не" + "ни" + any smile)
                task3.save_row(text, n2, p2, smile_dict, line)

                # task 4 (any smile without tone words)
                task4.save_row(n1, p1, n2, p2, smile_dict, line)

                # task 5 (two different smiles)
                task5.save_row(n2, p2, smile_dict, line)

            else:
                with open("files_result/!empty_rows.csv", "a") as file6:
                    file6.write(line)
                empty_rows += 1

            i += 1
        except Exception as ex:
            print(ex)
            print("ошибка на строке:", i)
            print(line)
            print(dt.datetime.now())
            print("empty rows:", empty_rows)
            print(f"time:\t{(time.time() - start_time) / 60}")

print("Finish:", dt.datetime.now())
print("empty rows:", empty_rows)
print(f"time:\t{(time.time() - start_time) / 60}")
