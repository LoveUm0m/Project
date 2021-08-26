from itertools import zip_longest
import json
out = {}
with open('users.csv', encoding='utf-8') as users:
    with open('hobby.csv', encoding='utf-8') as hobby:
        NumUsers = sum(1 for line in users)
        NumHobby = sum(1 for line in hobby)

        if NumUsers < NumHobby:
            exit(1)

        users.seek(0)
        hobby.seek(0)
        for LineUser, LineUserHobby in zip_longest(users, hobby):
            out[LineUser.strip()] = LineUserHobby.strip() if \
                LineUserHobby is not None else LineUserHobby

with open('task3.json', 'w', encoding='utf-8') as f:
    json.dump(out, f, ensure_ascii=False)
print(out)