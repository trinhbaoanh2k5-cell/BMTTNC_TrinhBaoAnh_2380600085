import ecdsa
import os

class ECCCipher:
    def __init__(self):
        self.key_path = os.path.join(os.getcwd(), 'cipher', 'ecc', 'keys')
        if not os.path.exists(self.key_path):
            os.makedirs(self.key_path)

    def generate_keys(self):
        # Tạo khóa riêng (Signing Key) và khóa công khai (Verifying Key)
        sk = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
        vk = sk.get_verifying_key()
        
        with open(os.path.join(self.key_path, 'privateKey.pem'), 'wb') as f:
            f.write(sk.to_pem())
        with open(os.path.join(self.key_path, 'publicKey.pem'), 'wb') as f:
            f.write(vk.to_pem())

    def load_keys(self):
        with open(os.path.join(self.key_path, 'privateKey.pem'), 'rb') as f:
            sk = ecdsa.SigningKey.from_pem(f.read())
        with open(os.path.join(self.key_path, 'publicKey.pem'), 'rb') as f:
            vk = ecdsa.VerifyingKey.from_pem(f.read())
        return sk, vk

    def sign(self, message, sk):
        return sk.sign(message.encode('utf-8')).hex()

    def verify(self, message, signature_hex, vk):
        try:
            signature_bytes = bytes.fromhex(signature_hex)
            return vk.verify(signature_bytes, message.encode('utf-8'))
        except:
            return False