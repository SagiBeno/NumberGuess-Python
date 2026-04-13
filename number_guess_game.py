import random

def main():
    print("Üdvözöllek a Számkitalálós játékban!")
    print("Gondoltam egy számra 1 és 100 között.")
    number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = input("Kérlek, add meg a tippedet (1-100): ")
        if not guess.isdigit():
            print("Kérlek, csak számot adj meg!")
            continue
        guess = int(guess)
        attempts += 1

        if guess < number:
            print("A tippelt szám kisebb, mint a gondolt szám.")
        elif guess > number:
            print("A tippelt szám nagyobb, mint a gondolt szám.")
        else:
            print(f"Gratulálok! {attempts} próbálkozásból kitaláltad a számot ({number})!")
            break

if __name__ == "__main__":
    main()