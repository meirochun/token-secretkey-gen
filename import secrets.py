import secrets

# This is equivalent to 256 bits. So. Sha256.
secret_key = secrets.token_hex(32)

print ("Generated secret key: ", secret_key)