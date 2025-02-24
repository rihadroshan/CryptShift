# CryptShift: A Simple Caesar Cipher Encryption Tool  

**CryptShift** is a user-friendly command-line application that implements the classic **Caesar cipher** — a simple yet effective encryption technique. It allows you to securely encode and decode messages by shifting letters in the alphabet by a specified number of positions.  

## Features  

- **Encryption and Decryption**:  
  - *Encryption*: Shifts each letter forward in the alphabet by a specified amount.  
  - *Decryption*: Shifts each letter backward to recover the original message.  
- **Shift Value Customization**: Define the number of positions to shift letters, offering flexibility in how secure your message is.  
- **Case Sensitivity**: Supports both uppercase and lowercase letters. Non-alphabetic characters (like punctuation and numbers) remain unchanged.  
- **Input Validation**:  
  - Ensures the shift value is a valid number.  
  - Guides users to make correct choices (encrypt or decrypt).  
- **Error Handling**: Friendly error messages for invalid inputs.  

## How to Use

1. **Clone the repository**:

```bash
git clone https://github.com/rihadroshan/cryptshift.git
cd cryptshift
```

3. **Run the program**:

```bash
python3 cryptshift.py
```

## Usage  

1. **Launch the program**.  
2. **Choose an action**:  
   - Type `e` to **encrypt** a message.  
   - Type `d` to **decrypt** a message.  
3. **Enter the shift value**: Input a number representing how many positions each letter should be shifted.  
4. **Provide your message**:  
   - If encrypting, type the message you want to secure.  
   - If decrypting, enter the encrypted message to reveal the original text.  
5. **View the result**: Your encrypted or decrypted message will be displayed.  


## Example  

**Encryption**:  

```
Welcome to CryptShift!

Would you like to encrypt or decrypt a message? Please type 'e' for encrypt or 'd' for decrypt: e

Please enter the shift value (a number): 3

Please enter the message you want to encrypt: Hello, World!

Here is your encrypted message: Khoor, Zruog!
```

**Decryption**:  

```
Welcome to CryptShift!

Would you like to encrypt or decrypt a message? Please type 'e' for encrypt or 'd' for decrypt: d

Please enter the shift value (a number): 3

Please enter the message you want to decrypt: Khoor, Zruog!

Here is your decrypted message: Hello, World!
```
