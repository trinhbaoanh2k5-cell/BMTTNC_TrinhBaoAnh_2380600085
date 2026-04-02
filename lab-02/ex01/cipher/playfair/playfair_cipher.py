class PlayfairCipher:
    def __init__(self):
        pass

    # 1. Hàm tạo ma trận 5x5 từ Key
    def generate_matrix(self, key):
        key = key.upper().replace('J', 'I').replace(" ", "")
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        matrix_flat = []
        used_chars = set()
        
        for char in key:
            if char not in used_chars and char in alphabet:
                matrix_flat.append(char)
                used_chars.add(char)
                
        for char in alphabet:
            if char not in used_chars:
                matrix_flat.append(char)
                used_chars.add(char)
                
        return [matrix_flat[i:i+5] for i in range(0, 25, 5)]

    # 2. Hàm tìm vị trí hàng và cột của một ký tự
    def find_position(self, matrix, char):
        for r, row in enumerate(matrix):
            if char in row:
                return r, row.index(char)
        return None

    # 3. Hàm Mã hóa (Encrypt)
    def playfair_encrypt(self, plain_text, key):
        matrix = self.generate_matrix(key)
        plain_text = plain_text.upper().replace('J', 'I').replace(" ", "")
        
        # Xử lý cặp ký tự (thêm X nếu trùng hoặc lẻ)
        prepared_text = ""
        i = 0
        while i < len(plain_text):
            a = plain_text[i]
            if (i + 1) < len(plain_text):
                b = plain_text[i+1]
                if a == b:
                    prepared_text += a + 'X'
                    i += 1
                else:
                    prepared_text += a + b
                    i += 2
            else:
                prepared_text += a + 'X'
                i += 1
        
        cipher_text = ""
        for i in range(0, len(prepared_text), 2):
            row1, col1 = self.find_position(matrix, prepared_text[i])
            row2, col2 = self.find_position(matrix, prepared_text[i+1])
            
            if row1 == row2: # Cùng hàng
                cipher_text += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
            elif col1 == col2: # Cùng cột
                cipher_text += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
            else: # Hình chữ nhật
                cipher_text += matrix[row1][col2] + matrix[row2][col1]
        return cipher_text

    # 4. Hàm Giải mã (Decrypt)
    def playfair_decrypt(self, cipher_text, key):
        matrix = self.generate_matrix(key)
        cipher_text = cipher_text.upper().replace(" ", "")
        
        plain_text = ""
        for i in range(0, len(cipher_text), 2):
            row1, col1 = self.find_position(matrix, cipher_text[i])
            row2, col2 = self.find_position(matrix, cipher_text[i+1])
            
            if row1 == row2:
                plain_text += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
            elif col1 == col2:
                plain_text += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
            else:
                plain_text += matrix[row1][col2] + matrix[row2][col1]
        return plain_text