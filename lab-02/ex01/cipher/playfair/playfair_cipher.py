class PlayfairCipher:
    def __init__(self):
        pass

    def __create_matrix(self, key):
        key = key.upper().replace('J', 'I')
        matrix = []
        for char in key:
            if char not in matrix and char.isalpha():
                matrix.append(char)
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        for char in alphabet:
            if char not in matrix:
                matrix.append(char)
        return [matrix[i:i+5] for i in range(0, 25, 5)]

    def __find_position(self, matrix, char):
        for r, row in enumerate(matrix):
            if char in row:
                return r, row.index(char)
        return None

    def __prepare_text(self, text):
        text = text.upper().replace('J', 'I').replace(" ", "")
        prepared_text = ""
        i = 0
        while i < len(text):
            prepared_text += text[i]
            if i + 1 < len(text):
                if text[i] == text[i+1]:
                    prepared_text += 'X'
                else:
                    prepared_text += text[i+1]
                    i += 1
            else:
                prepared_text += 'X'
            i += 1
        return prepared_text

    def playfair_encrypt(self, plain_text, key):
        matrix = self.__create_matrix(key)
        prepared_text = self.__prepare_text(plain_text)
        ciphertext = ""
        for i in range(0, len(prepared_text), 2):
            r1, c1 = self.__find_position(matrix, prepared_text[i])
            r2, c2 = self.__find_position(matrix, prepared_text[i+1])
            if r1 == r2:
                ciphertext += matrix[r1][(c1 + 1) % 5] + matrix[r2][(c2 + 1) % 5]
            elif c1 == c2:
                ciphertext += matrix[(r1 + 1) % 5][c1] + matrix[(r2 + 1) % 5][c2]
            else:
                ciphertext += matrix[r1][c2] + matrix[r2][c1]
        return ciphertext

    def playfair_decrypt(self, cipher_text, key):
        matrix = self.__create_matrix(key)
        decrypted_text = ""
        for i in range(0, len(cipher_text), 2):
            r1, c1 = self.__find_position(matrix, cipher_text[i])
            r2, c2 = self.__find_position(matrix, cipher_text[i+1])
            if r1 == r2:
                decrypted_text += matrix[r1][(c1 - 1) % 5] + matrix[r2][(c2 - 1) % 5]
            elif c1 == c2:
                decrypted_text += matrix[(r1 - 1) % 5][c1] + matrix[(r2 - 1) % 5][c2]
            else:
                decrypted_text += matrix[r1][c2] + matrix[r2][c1]
        return decrypted_text