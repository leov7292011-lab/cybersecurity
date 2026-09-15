#hashing is a one way function. Same input --> same output

import hashlib

password = "monkey100?"

data = password.encode("utf-8")
digest = hashlib.md5(data).hexdigest()

print(f"password: {password}")
print(f"hash: {digest}")

# comparing hash passwords

diff_passwords = ["monkey100?", "doggiewoggie2", "donkeyfriend4" , "t" ]

for p in diff_passwords:
    data = password.encode("utf-8") #converts plain text into raw bytes
    digest = hashlib.sha256(data).hexdigest()

    print(f"password: {p}")
    print(f"hash: {digest}" , "\n") 