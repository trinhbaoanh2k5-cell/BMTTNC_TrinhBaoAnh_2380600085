from flask import Flask, request, jsonify
from cipher.caesar.caesar_cipher import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
from cipher.playfair import PlayfairCipher
from cipher.transposition import TranspositionCipher

app = Flask(__name__)

# Khởi tạo các thuật toán
caesar = CaesarCipher()
vigenere_cipher = VigenereCipher()
rail_fence_cipher = RailFenceCipher()
playfair_cipher = PlayfairCipher()
transposition_cipher = TranspositionCipher()

# --- ROUTES CAESAR, VIGENERE, RAILFENCE, PLAYFAIR GIỮ NGUYÊN ---
# (Lược bớt cho gọn, Bảo Anh giữ lại code cũ của các bài này nhé)

# --- TRANSPOSITION CIPHER ROUTES ---
@app.route('/api/transposition/encrypt', methods=['POST'])
def transposition_encrypt():
    data = request.json
    plain_text = data.get('plain_text')
    key = int(data.get('key'))
    encrypted_text = transposition_cipher.encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/transposition/decrypt', methods=['POST'])
def transposition_decrypt():
    data = request.json
    cipher_text = data.get('cipher_text')
    key = int(data.get('key'))
    decrypted_text = transposition_cipher.decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)