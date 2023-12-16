# Token secret key generator
A secret key generator made in python. HELPS A LOT WITH AUTH STUFF BTW

> secret_key = secrets.token_hex(32) generate a random 64-character hexadecimal string (256 bits)

> secret_key = secrets.token_hex(64) generate a random 128-character hexadecimal string (512 bits)

Few explanations:

The number of bits in a cryptographic key is directly related to its strength. Here are some common key sizes for different cryptographic algorithms:

    Symmetric Key Algorithms:
        128 bits
        192 bits
        256 bits

    For example, in AES (Advanced Encryption Standard), you commonly see key sizes of 128, 192, or 256 bits.

    Hash Functions (like SHA-256):
        224 bits
        256 bits
        384 bits
        512 bits

    SHA-256, as the name suggests, produces a 256-bit hash.

    Asymmetric Key Algorithms (RSA, ECC, etc.):
        1024 bits (considered weak and not recommended for most purposes)
        2048 bits
        3072 bits
        4096 bits
        Larger key sizes for increased security
