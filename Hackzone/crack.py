import hashlib
from tqdm import tqdm

def crack_sha512_hash(target_hash, wordlist_path):
    try:
        # Open the wordlist file with forgiving encoding to handle messy characters
        with open(wordlist_path, 'r', encoding='latin-1', errors='ignore') as file:
            words = file.readlines()
    except FileNotFoundError:
        print(f"[-] Wordlist not found: {wordlist_path}")
        return None

    print(f"[*] Cracking SHA-512 hash:\n{target_hash}\n")
    for word in tqdm(words, desc="Trying passwords"):
        word = word.strip()
        hashed = hashlib.sha512(word.encode()).hexdigest()
        if hashed == target_hash:
            print(f"[+] Match found: {word}")
            return word

    print("[-] No match found in wordlist.")
    return None
# === CONFIGURATION ===

# Replace with the SHA-512 hash you want to crack
target_hash = "3b337f0f4a06b06a1dab78f6973d3b0652232793226eb6a6f0bd66f3021b26f081c1c5d0eb6bbfef594ec21595e6801c5e1eda3670043e2225d7f9742f82c833"

# Replace with the full path to your wordlist file
wordlist_path = r"C:\Users\pratham.prabhu\Downloads\rockyou.txt"

# === EXECUTION ===
crack_sha512_hash(target_hash, wordlist_path)

