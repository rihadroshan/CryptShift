# CryptShift

CryptShift is a Python program that allows you to encrypt and decrypt messages using the Caesar cipher technique. The Caesar cipher shifts each letter in a message by a fixed number of positions down or up the alphabet.

## Usage

1. **Encryption**: To encrypt a message, each letter in the message is shifted forward in the alphabet by a specified number of positions.

2. **Decryption**: To decrypt an encrypted message, each letter is shifted backward by the same number of positions to recover the original message.

## Features

- **Shift Value**: You can specify the number of positions each letter should be shifted in the alphabet.
- **Supports**: It supports both uppercase and lowercase letters in the English alphabet.
- **Input Validation**: Validates user inputs for choice (encrypt/decrypt) and shift value.
- **Error Handling**: Provides error messages for invalid inputs.

## How to Use

1. Clone the repository:
   ```
   git clone https://github.com/rihadroshan/PRODIGY_CS_01.git
   ```

2. Navigate into the project directory:
   ```
   cd PRODIGY_CS_01
   ```

3. Run the program:
   ```
   python CryptShift.py
   ```

4. Follow the prompts to encrypt or decrypt a message.

## Example

Here's an example of how to use the Caesar cipher program:

```
Welcome to CryptShift!

Would you like to encrypt or decrypt a message? Please type 'e' for encrypt or 'd' for decrypt: e

Please enter the shift value (a number): 3

Please enter the message you want to encrypt: Hello, World!

Here is your encrypted message: Khoor, Zruog!
```
