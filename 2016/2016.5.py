import hashlib


id = 'abbhdwsy'

i = 0
password = ""
while len(password) < 8:
    hash = id + str(i)
    hash = hashlib.md5(hash.encode()).hexdigest()
    if hash.startswith('00000'):
        password += hash[5]
    i += 1


print(f"Part 1: {password}")

i = 0

password = ['_']*8

while any(x == "_" for x in password):
    hash = id + str(i)
    hash = hashlib.md5(hash.encode()).hexdigest()
    if hash.startswith('00000'):
        try:
            if password[int(hash[5])] == "_":
                password[int(hash[5])] = hash[6]
        except (IndexError, TypeError, ValueError) as e:
            pass


    i += 1

p = ""
for i in password:
    p += i

print(f"Part 2: {p}")

