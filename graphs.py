import re


# it's raw code:

rus_alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
eng_alphabet = "abcdefghijklmnopqrstuvwxyz1234567890_"
s_symbols = "%=*$;`~+,.!?):…-"

symbols = set()
i = 0
n = 0
pairs = set()
count_pairs = 0

with open("files/sentiment.csv", encoding="utf-8") as file:
    for line in file:
        if i < 1000000:
            user_name = line.split('"|"')[2].lower()
            text = line.split('"|"')[3]
            text = bytes(text, "utf-8")
            text = text.decode("utf-8", "ignore")
            text = text.lower()
            users_in_text = re.findall('@[^\s]+', text)
            users = set()

            if len(users_in_text) > 0:
                for user in users_in_text:
                    is_s_symbols = any(s in s_symbols for s in list(user))
                    if is_s_symbols:
                        user = re.sub("[%=*$;`~+,.!?):…\>-]+", "", user)

                    is_russian = any(s in rus_alphabet for s in list(user))
                    if is_russian:
                        user = "".join([x for x in list(user) if x not in rus_alphabet])

                    last_symbol = user[-1:]
                    if last_symbol not in eng_alphabet:
                        symbols.add(last_symbol)
                        n += 1
                        with open("files_result/text.csv", encoding="utf-8", mode="a") as t:
                            t.write(line.split('"|"')[3] + "\n")

                    user = user.replace("@", "")
                    if len(user) > 1:
                        users.add(user)

            users.discard(user_name)

            if len(users) > 0:
                for user in users:
                    count_pairs += 1
                    pairs.add((user_name, user))

            i += 1

with open("files_result/users.csv", encoding="utf-8", mode="a") as f:
    for pair in pairs:
        p = re.sub("[() ]+", "", str(pair))
        p = p.split(",")
        f.write(f"{p[0]}|{p[1]}\n")

print("symbols: ", symbols)
print("count last symbols: ", n)
print("count_pairs: ", count_pairs)
print("pairs: ", len(pairs))

# "Бесплатный обед за спасибо от сбербанка. Вот уж действительно спасибо:) (at @BurgerKingRu) http://t.co/sGbgp6gYsh"
# "@Nataaaashka2013сегодя есть свободное время))"
# "@vovich76,у МегаФона лучшая 4G-сеть в России: Москва, МО, всего 37 регионов. Сеть полностью готова к работе с iPhone, но вопрос поддержки 4G"
# "“@IGORSINYAK:Как же меня заебали эти всплывающие окна на айфон которые показывают новые лайки. Сука .”даа,+андроида в том,что там нет такого"
# "@GoodLineRock,любовь моя,мне скучно,поговори со мной :33333333333333"
# {'_', '4', ')', '…', '7', 'ь', ',', 'я', '5', 'к', '?', '2', '9', '.', '8', '0', '1', 'у', ':', '6', '3', '!'}
# {'…', '_', ')', ',', '!', 'у', '.', ':', 'ь', 'к', '?', 'я'}
# symbols:  {'А', '❤', '-', '`', '☇', '™', '️', '{', 'Е', 'Т', '*', '»', ']', 'Ь', 'Ю', '=', '@', '“', 'И', ';', '(', 'є', '♥', '–', 'Й', 'Л', '~', 'К', 'Я', 'ө', 'Х', '$', '▸', '#', '+', 'О', '%', '”', 'У', 'В', '^'}
# count last symbols:  453
# pairs:  332753
