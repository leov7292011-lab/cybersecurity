import hashlib
import os
plaintext_password = "monkey100?"
password = plaintext_password.encode("utf-8")

#1. regular hash, no salt, for two users, same password --> identical hashes
hash_a = hashlib.sha256(password).hexdigest()
hash_b = hashlib.sha256(password).hexdigest()

print("No salt:")
print(f" User A: {hash_a}")
print(f" User B: {hash_b}")

# Add salt, each user will get their own SALT.
salt_a = os.urandom(16)

salt_b = os.urandom(16)
print(salt_a)
print(salt_b)

salt_hash_a = hashlib.sha256(salt_a + password).hexdigest()
salt_hash_b = hashlib.sha256(salt_b + password).hexdigest()

print("\n With salt:")
print(f"User A  salt + hash: {salt_hash_a}" )
print(f"User B salt + hash: {salt_hash_b}" )