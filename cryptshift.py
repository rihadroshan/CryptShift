class CaesarCipher:
    def __init__(self, shift):
        self.shift = shift % 26  

    def _shift_char(self, char, shift_amount):
        if char.islower():
            base = ord('a')
            return chr((ord(char) - base + shift_amount) % 26 + base)
        elif char.isupper():
            base = ord('A')
            return chr((ord(char) - base + shift_amount) % 26 + base)
        else:
            return char

    def encrypt(self, text):
        return ''.join(self._shift_char(char, self.shift) for char in text)

    def decrypt(self, text):
        return ''.join(self._shift_char(char, -self.shift) for char in text)

def main():
    import sys
    print("Welcome to CryptShift!\n")
    
    choice = None
    while choice not in ['e', 'd']:
        choice = input("Would you like to encrypt or decrypt a message? Please type 'e' for encrypt or 'd' for decrypt: ").strip().lower()
        if choice not in ['e', 'd']:
            print("Oops! That was an invalid choice. Please type 'e' for encrypt or 'd' for decrypt.\n")
    
    shift = None
    while shift is None:
        try:
            shift = int(input("\nPlease enter the shift value (a number): "))
        except ValueError:
            print("Oops! That wasn't a valid number. Please try again.\n")

    cipher = CaesarCipher(shift)

    prompt_message = "Please enter the message you want to encrypt: " if choice == 'e' else "Please enter the message you want to decrypt: "
    text = input(f"\n{prompt_message}")

    result = cipher.encrypt(text) if choice == 'e' else cipher.decrypt(text)
    action = "encrypted" if choice == 'e' else "decrypted"
    print(f"\nHere is your {action} message: {result}\n")

if __name__ == "__main__":
    main()
