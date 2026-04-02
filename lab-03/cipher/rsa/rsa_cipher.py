import rsa
import os

class RSACipher:
    def __init__(self):
        # Đường dẫn tuyệt đối để tránh lỗi không tìm thấy folder keys
        self.key_path = os.path.join(os.getcwd(), 'cipher', 'rsa', 'keys')
        if not os.path.exists(self.key_path):
            os.makedirs(self.key_path)

    def generate_keys(self):
        (pub_key, priv_key) = rsa.newkeys(2048)
        with open(os.path.join(self.key_path, 'publicKey.pem'), 'wb') as f:
            f.write(pub_key.save_pkcs1())
        with open(os.path.join(self.key_path, 'privateKey.pem'), 'wb') as f:
            f.write(priv_key.save_pkcs1())

    def load_keys(self):
        with open(os.path.join(self.key_path, 'publicKey.pem'), 'rb') as f:
            pub_key = rsa.PublicKey.load_pkcs1(f.read())
        with open(os.path.join(self.key_path, 'privateKey.pem'), 'rb') as f:
            priv_key = rsa.PrivateKey.load_pkcs1(f.read())
        return priv_key, pub_key

    def encrypt(self, message, pub_key):
        return rsa.encrypt(message.encode('utf-8'), pub_key).hex()

    def decrypt(self, crypto_hex, priv_key):
        crypto_bytes = bytes.fromhex(crypto_hex)
        return rsa.decrypt(crypto_bytes, priv_key).decode('utf-8')
    def sign(self, message, priv_key):
        # Tạo chữ ký số bằng Private Key
        return rsa.sign(message.encode('utf-8'), priv_key, 'SHA-256').hex()

    def verify(self, message, signature_hex, pub_key):
        try:
            # Chuyển chữ ký từ hexa về bytes
            signature_bytes = bytes.fromhex(signature_hex)
            # Xác thực chữ ký bằng Public Key
            rsa.verify(message.encode('utf-8'), signature_bytes, pub_key)
            return True
        except rsa.VerificationError:
            return False