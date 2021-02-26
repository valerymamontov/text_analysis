import re


# it's raw code:

rus_alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
eng_alphabet = "abcdefghijklmnopqrstuvwxyz1234567890"
s_symbols = ",.!?:)"

i = 0

with open("files/sentiment-10000.csv", encoding="utf-8") as file:
    for line in file:
        if i < 1000000:
            user_name = line.split('"|"')[2]
            text = line.split('"|"')[3]
            users_in_text = re.findall('@[^\s]+', text)

            if len(users_in_text) > 0:
                for user in users_in_text:
                    is_s_symbols = any(s in s_symbols for s in list(user))
                    if is_s_symbols:
                        user = user.split(",")[0]
                        user = user.split(".")[0]
                        user = user.split("!")[0]
                        user = user.split("?")[0]
                        user = user.split(":")[0]
                        user = user.split(")")[0]
                    TODO: "change code using regex"

                    is_russian = any(s in rus_alphabet for s in list(user))
                    if is_russian:
                        u = "".join([x for x in list(user) if x.lower() not in rus_alphabet])

                    last_symbol = user[-1:]
                    if last_symbol.lower() not in eng_alphabet:
                        if last_symbol == "…":
                            print(line)

                        # print(line)
                        # print(user_name, user)
            i += 1

# абвгдеёжзийклмнопрстуфхцчшщъыьэюя

#  @Faka_Princess: @__Green_Idiot__

# "Бесплатный обед за спасибо от сбербанка. Вот уж действительно спасибо:) (at @BurgerKingRu) http://t.co/sGbgp6gYsh"

# "@Nataaaashka2013сегодя есть свободное время))"
# "@vovich76,у МегаФона лучшая 4G-сеть в России: Москва, МО, всего 37 регионов. Сеть полностью готова к работе с iPhone, но вопрос поддержки 4G"
# "“@IGORSINYAK:Как же меня заебали эти всплывающие окна на айфон которые показывают новые лайки. Сука .”даа,+андроида в том,что там нет такого"
# "@GoodLineRock,любовь моя,мне скучно,поговори со мной :33333333333333"

# {'_', '4', ')', '…', '7', 'ь', ',', 'я', '5', 'к', '?', '2', '9', '.', '8', '0', '1', 'у', ':', '6', '3', '!'}
# {'…', '_', ')', ',', '!', 'у', '.', ':', 'ь', 'к', '?', 'я'}
print(symbols)
