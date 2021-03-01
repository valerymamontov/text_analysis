import re
import time

# it's raw code:

start_time = time.time()
rus_alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
s_symbols = "%=*$;`~+,.!?{}()[]№/^<>|:…-"
pairs = set()

with open("files/sentiment.csv", encoding="utf-8") as file:
    for line in file:
        user_name = line.split('"|"')[2].lower()
        text = line.split('"|"')[3]
        text = bytes(text, "utf-8")
        text = text.decode("utf-8", "ignore")
        text = text.lower()
        users_in_text = re.findall('@[^\s]+', text)
        users = set()

        if len(users_in_text) > 0:
            for user in users_in_text:
                user = user.replace("@", "")

                is_s_symbols = any(s in s_symbols for s in list(user))
                if is_s_symbols:
                    user = re.sub("[%=*$;`~+,.!?{}()[\]№\/^<>|:…\>-]+", "", user)

                is_russian = any(s in rus_alphabet for s in list(user))
                if is_russian:
                    user = "".join([x for x in list(user) if x not in rus_alphabet])

                if len(user) > 1:
                    users.add(user)

            users.discard(user_name)

        if len(users) > 0:
            for us in users:
                pairs.add((user_name, us))


pairs_sorted = sorted(pairs, key=lambda x: x[0])

with open("files_result/users.csv", encoding="utf-8", mode="a") as f:
    for pair in pairs_sorted:
        p = re.sub("[() ']+", "", str(pair))
        p = p.split(",")
        f.write(f"{p[0]}|{p[1]}\n")


print("pairs: ", len(pairs))
print("time: " + f"{(time.time()-start_time)/60}")
