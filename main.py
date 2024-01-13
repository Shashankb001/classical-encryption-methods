def vigenere():
    def resize_key(key, text):  # making key length the same as cipher/plain text
        len_key = len(key)
        len_txt = len(text)
        quo = len_txt // len_key
        new_key = key * quo
        for i in range(len_txt % len_key):
            new_key += key[i]
        return new_key

    def encryption(key, text):
        string = ""
        for i in range(len(text)):
            k = key[i]
            t = text[i]
            string += letters[(letters.index(k) + letters.index(t)) % 26]
        return string

    def decryption(key, text):
        string = ""
        for i in range(len(text)):
            k = key[i]
            t = text[i]
            string += letters[(letters.index(t) - letters.index(k)) % 26]
        return string

    key = input("Enter key : ").replace(' ', '')
    letters = "abcdefghijklmnopqrstuvwxyz"
    choice = input("Enter 'encrypt' for encryption and 'decrypt' for decryption : ").lower()
    if choice == 'encrypt':
        plain_text = input("Enter plain text : ").replace(" ", "")
        key = resize_key(key, plain_text)
        encrypted_text = encryption(key, plain_text)
        print("Encrypted text : ", encrypted_text)
    else:
        cipher_text = input("Enter cipher text : ").replace(" ", "")
        key = resize_key(key, cipher_text)
        decrypted_text = decryption(key, cipher_text)
        print("Decrypted text : ", decrypted_text)


def playfair():
    def replace_j(string):
        for i in range(len(string)):
            if string[i] == 'j':
                string[i] = 'i'
        return string

    def sort(seq):
        unique = []
        for item in seq:
            if item not in unique: unique.append(item)
        return unique

    def in_list(item):
        for i in grid:
            if item in i:
                return [grid.index(i), i.index(item)]
        return -1

    def decryption(text):
        decrypt = ""
        for i in range(0, len(text), 2):
            i1, j1 = in_list(text[i])
            i2, j2 = in_list(text[i + 1])
            if (i1 == i2):
                decrypt += grid[i1][(j1 - 1) % 5] + grid[i1][(j2 - 1) % 5]
            elif (j1 == j2):
                decrypt += grid[(i1 - 1) % 5][j1] + grid[(i2 - 1) % 5][j2]
            else:
                decrypt += grid[i1][j2] + grid[i2][j1]
        return decrypt

    def encryption():
        encrypt = ""
        for i in pair:
            i1, j1 = in_list(i[0])
            i2, j2 = in_list(i[1])
            if (i1 == i2):
                encrypt += grid[i1][(j1 + 1) % 5] + grid[i1][(j2 + 1) % 5]
            elif (j1 == j2):
                encrypt += grid[(i1 + 1) % 5][j1] + grid[(i2 + 1) % 5][j1]
            else:
                encrypt += grid[i1][j2] + grid[i2][j1]
        return encrypt

    def algorithm(key, text):
        unique_alpha = sort(key)
        var = 0
        iter = 24
        for i in range(26):
            if chr(i + 97) not in unique_alpha:
                if (chr(i + 97) != 'j'):
                    non_uniq.append(chr(i + 97))
        unique_alpha += non_uniq
        for i in range(5):
            temp = []
            for _ in range(5):
                temp.append(unique_alpha[var])
                var += 1
            grid.append(temp)
        i = 0
        while (i < len(text)):
            if (i == len(text) - 1):
                pair.append([text[i], unique_alpha[iter]])
                i += 1
            else:
                if (text[i] != text[i + 1]):
                    pair.append([text[i], text[i + 1]])
                    i += 2
                else:
                    pair.append([text[i], unique_alpha[iter]])
                    iter -= 1
                    i += 1

    key, pair, grid, non_uniq = [], [], [], []
    key[:0] = input("Enter key : ").lower().replace(' ', '')
    replace_j(key)
    choice = input("Enter 'encrypt' for encryption and 'decrypt' for decryption : ").lower()
    if (choice == 'encrypt'):
        plain_text = input("Plain-text : ").lower().replace(' ', '')
        replace_j(plain_text)
        algorithm(key, plain_text)
        print("Encrypted text: ", encryption())
    else:
        cipher_text = input("Cipher-text : ").replace(' ', '')
        replace_j(cipher_text)
        algorithm(key, cipher_text)
        print("Decrypted text: ", decryption(cipher_text))


def vernam():
    def encryption(key, text):
        string = ""
        for i in range(len(text)):
            k = key[i]
            t = text[i]
            string += letters[(letters.index(k) + letters.index(t)) % 26]
        return string

    def decryption(key, text):
        string = ""
        for i in range(len(text)):
            k = key[i]
            t = text[i]
            string += letters[(letters.index(t) - letters.index(k)) % 26]
        return string

    key = input("Enter key : ").replace(' ', '').lower()
    letters = "abcdefghijklmnopqrstuvwxyz"
    choice = input("Enter 'encrypt' for encryption and 'decrypt' for decryption : ").lower()
    if choice == 'encrypt':
        plain_text = input("Enter plain text : ").replace(" ", "")
        encrypted_text = encryption(key, plain_text)
        print("Encrypted text : ", encrypted_text)
    else:
        cipher_text = input("Enter cipher text : ").replace(" ", "")
        decrypted_text = decryption(key, cipher_text)
        print("Decrypted text : ", decrypted_text)


def hill():
    def decryption(matrix):
        def mod_inv(det):
            for i in range(26):
                if (det * i) % 26 == 1:
                    return i

        def getMatrixMinor(m, i, j):
            l = []
            for row in (m[:i] + m[i + 1:]):
                l.append(row[:j] + row[j + 1:])
            return l

        def transpose(mat):
            trans = []
            rows = len(mat)
            for i in range(rows):
                temp = []
                for j in range(rows):
                    temp.append(mat[j][i])
                trans.append(temp)
            return trans

        def smaller_matrix(matrix, row, column):
            new_matrix = [x[:] for x in matrix]
            new_matrix.remove(matrix[row])
            for i in range(len(new_matrix)):
                new_matrix[i].pop(column)
            return new_matrix

        def determinant(A):
            num_rows = len(A)
            if len(A) == 1:
                return A[0][0]
            elif len(A) == 2:
                return A[0][0] * A[1][1] - A[1][0] * A[0][1]
            else:
                ans = 0
                num_columns = num_rows
                for j in range(num_columns):
                    ans += (-1) ** (j) * A[0][j] * determinant(smaller_matrix(A, 0, j))
                return ans

        def matrix_multiplication(mat, det):
            det = mod_inv(det)
            if det == None:
                print("Modular Inverse doesn't exist, create another key")
                exit(0)
            for i in range(len(mat)):
                for j in range(len(mat)):
                    mat[i][j] = (mat[i][j] * det) % 26
            return mat

        def adjoint(m):
            cofactors = []
            for r in range(len(m)):
                cofactorRow = []
                for c in range(len(m)):
                    minor = getMatrixMinor(m, r, c)
                    cofactorRow.append((((-1) ** (r + c)) * determinant(minor)) % 26)
                cofactors.append(cofactorRow)
            return transpose(cofactors)

        det = determinant(matrix) % 26
        print("ADJOINT: ", adjoint(matrix))
        adjoint_matrix = matrix_multiplication(adjoint(matrix), det)
        return adjoint_matrix

    def decode(grid, pairs, message):
        for i in pairs:
            for j in range(length):
                res = sum([i[m] * grid[j][m] for m in range(length)]) % 26
                message += chr(res + 97)
        return message

    def split_text(text, length):
        var = 0
        for i in range(0, len(text), length):
            temp = []
            for _ in range(length):
                temp.append(ord(text[var]) - 97)
                var += 1
            pairs.append(temp)

    def algorithm(length, key):
        var = 0
        for i in range(length):
            temp = []
            for j in range(length):
                temp.append(ord(key[var]) - 97)
                var += 1
            grid.append(temp)

    grid, pairs = [], []
    message = ""
    key = input("Enter key : ").lower().replace(' ', '')
    text = input("Enter cipher/plain text : ").lower().replace(' ', '')
    choice = input("Enter 'encrypt' for encryption and 'decrypt' for decryption : ").lower()
    length = int((len(key)) ** 0.5)
    if len(key) > length ** 2:
        for i in range((length + 1) ** 2 - len(key)):
            key += chr(97 + i)
        length += 1
    if (len(text) % length != 0):
        text += 'z' * (length - len(text) % length)
    algorithm(length, key)
    split_text(text, length)
    if (choice == 'decrypt'):
        grid = decryption(grid)
    message = decode(grid, pairs, message)
    print(choice + "ed text : " + message)


print("Enter\n1.Playfair cipher\n2.Hill cipher\n3.Vigenere cipher\n4.Vernam cipher")
choice = int(input("Choice - "))
if choice == 1:
    playfair()
elif choice == 2:
    hill()
elif choice == 3:
    vigenere()
else:
    vernam()
