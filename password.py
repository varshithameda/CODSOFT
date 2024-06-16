import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to Password Generator")

    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                print("Please enter a positive integer for the length.")
                continue
            else:
                break
        except ValueError:
            print("Please enter a valid integer for the length.")

    password = generate_password(length)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
