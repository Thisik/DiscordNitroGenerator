import random
import requests

def generate_random_code(length=19):
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    return ''.join(random.choice(characters) for _ in range(length))

def check_code(code):
    url = f"https://discord.com/api/v8/entitlements/gift-codes/{code}"
    response = requests.get(url)
    if response.status_code == 200:
        print(f"Kód {code} je platný! Program bude ukončen.")
        exit()
    else:
        print(f"Kód {code} není platný.")

def main():
    while True:
        code = generate_random_code()
        print(f"Kontrola kódu: {code}")
        check_code(code)

if __name__ == "__main__":
    main()
