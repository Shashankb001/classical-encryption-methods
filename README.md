# classical-encryption-methods
This script provides a menu with four distinct types of classical encryption methods: Playfair cipher, Hill cipher, Vigenere cipher, and Vernam cipher. Each cipher is implemented in a distinct function, and the script allows users to encrypt or decrypt a given text using their preferred technique.

    Playfair Cipher: This method involves creating a 5x5 grid of letters based on a key, and encrypting pairs of letters according to their position in the grid. It substitutes pairs of letters instead of individual letters.

    Hill Cipher: This method uses linear algebra, encrypting text by multiplying each block of letters (converted to numerical values) by a matrix (formed from the key), modulo 26.

    Vigenere Cipher: This is a method of encrypting alphabetic text by using a simple form of polyalphabetic substitution. A key is used to generate a repeating key string, which is then used to shift the letters in the plaintext.

    Vernam Cipher: Also known as the one-time pad, it's a symmetric encryption technique where plaintext is combined with a random key. It's theoretically unbreakable if the key is random, as long as the message, and used only once.

Each cipher function in the script follows a similar structure:

    Prompt the user for a key and a choice between encryption and decryption.
    Perform necessary transformations on the key and the text (like resizing the key to match the text length in Vigenere and Vernam ciphers, or creating a matrix in the Hill cipher).
    Implement the specific algorithm for encryption or decryption.
    Output the encrypted or decrypted text.
