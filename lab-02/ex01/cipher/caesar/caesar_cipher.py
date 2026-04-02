from cipher.caesar.alphabet import ALPHABET

class CaesarCipher:
    def __init__(self):
        self.alphabet = ALPHABET

    def encrypt_text(self, text: str, key: int) -> str:
        alphabet_len = len(self.alphabet)
        text = text.upper()
        encrypted_text = []
        for letter in text:
            # Tìm vị trí của chữ cái trong bảng chữ cái
            letter_index = self.alphabet.index(letter)
            # Tính vị trí mới sau khi dịch chuyển (dùng % để quay vòng về A nếu quá Z)
            output_index = (letter_index + key) % alphabet_len
            encrypted_text.append(self.alphabet[output_index])
        return "".join(encrypted_text)

    def decrypt_text(self, text: str, key: int) -> str:
        alphabet_len = len(self.alphabet)
        text = text.upper()
        decrypted_text = []
        for letter in text:
            letter_index = self.alphabet.index(letter)
            # Giải mã bằng cách trừ đi khóa key
            output_index = (letter_index - key) % alphabet_len
            decrypted_text.append(self.alphabet[output_index])
        return "".join(decrypted_text)