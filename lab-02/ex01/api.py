from flask import Flask, request, jsonify
from cipher.caesar.caesar_cipher import CaesarCipher
from cipher.vigenere import VigenereCipher
app = Flask(__name__)
caesar = CaesarCipher()
vigenere_cipher = VigenereCipher()
@app.route("/api/caesar/encrypt", methods=["POST"])
def encrypt():
    data = request.json
    return jsonify({'encrypted_message': caesar.encrypt_text(data['plain_text'], int(data['key']))})

@app.route("/api/caesar/decrypt", methods=["POST"])
def decrypt():
    data = request.json
    return jsonify({'decrypted_message': caesar.decrypt_text(data['cipher_text'], int(data['key']))})
# VIGENERE CIPHER ALGORITHM
@app.route('/api/vigenere/encrypt', methods=['POST'])
def vigenere_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = data['key']
    # Gọi hàm mã hóa Vigenere
    encrypted_text = vigenere_cipher.vigenere_encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/vigenere/decrypt', methods=['POST'])
def vigenere_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = data['key']
    # Gọi hàm giải mã Vigenere
    decrypted_text = vigenere_cipher.vigenere_decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)