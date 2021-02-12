from tone import words_negative, words_positive
from smiles import smiles_negative, smiles_positive
from analysis import preproccess_text, find_polarity
import time


start_time = time.time()
task1 = open("files_result/emotikon_token.csv", "a")
task2 = open("files_result/two_tokens.csv", "a")
task3 = open("files_result/not_token.csv", "a")
task4 = open("files_result/emotikon_no_token.csv", "a")
task5 = open("files_result/two_emotikons.csv", "a")

empty_rows = 0

with open("files/sentiment-2.csv", encoding="cp1251") as file:
    for line in file:
        text = line.split('"|"')[3]
        text = preproccess_text(text)

        # skip any row which contains one symbol
        if len(text) > 2:
            tone_dict = find_polarity(text, words_negative, words_positive, "words")
            smile_dict = find_polarity(text, smiles_negative, smiles_positive, "smiles")

            n1, p1 = len(tone_dict["negative"]), len(tone_dict["positive"])
            n2, p2 = len(smile_dict["negative"]), len(smile_dict["positive"])

            # task 1 (positive smile + negative word or negative smile + positive word)
            if n2 > 0 and p1 > 0:
                task1.write(f'{line}"|"{" ".join(smile_dict["negative"])}"|"{",".join(tone_dict["positive"])}\n')
            if p2 > 0 and n1 > 0:
                task1.write(f'{line}"|"{" ".join(smile_dict["positive"])}"|"{",".join(tone_dict["negative"])}\n')

            # task 2 (negative + positive words)
            if n1 > 0 and p1 > 0:
                task2.write(f'{line}"|"{",".join(tone_dict["positive"])}"|"{",".join(tone_dict["negative"])}\n')

            # task 3 ("не" + "ни" + any smile)
            text_set = set(text.lower().split(" "))
            if "не" in text_set and (n2 > 0 and p2 > 0):
                task3.write(f'{line}"|"не{",".join(tone_dict["positive"] + tone_dict["negative"])}\n')
            if "ни" in text_set and (n2 > 0 and p2 > 0):
                task3.write(f'{line}"|"ни{",".join(tone_dict["positive"] + tone_dict["negative"])}\n')

            # task 4 (any smile without negative or positive words)
            if (n1 == 0 and p1 == 0) and (n2 > 0 and p2 > 0):
                task4.write(f'{line}"|"{" ".join(smile_dict["positive"] + smile_dict["negative"])}\n')

            # task 5 (two different smiles)
            if n2 > 0 and p2 > 0:
                task5.write(f'{line}"|"{" ".join(smile_dict["positive"])}"|"{" ".join(smile_dict["negative"])}\n')
        else:
            empty_rows += 1

task1.close()
task2.close()
task3.close()
task4.close()
task5.close()

print(empty_rows)
print(f"time:\t{(time.time()-start_time)/60}")
