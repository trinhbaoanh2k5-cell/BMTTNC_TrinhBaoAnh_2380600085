from flask import Flask, request, jsonify
from cipher.caesar.caesar_cipher import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
from cipher.playfair import PlayfairCipher

app = Flask(__name__)

# Khởi tạo các thuật toán
caesar = CaesarCipher()
vigenere_cipher = VigenereCipher()
rail_fence_cipher = RailFenceCipher()
playfair_cipher = PlayfairCipher()

# --- CAESAR CIPHER ROUTES ---
@app.route("/api/caesar/encrypt", methods=["POST"])
def encrypt():
    data = request.json
    return jsonify({'encrypted_message': caesar.encrypt_text(data['plain_text'], int(data['key']))})

@app.route("/api/caesar/decrypt", methods=["POST"])
def decrypt():
    data = request.json
    return jsonify({'decrypted_message': caesar.decrypt_text(data['cipher_text'], int(data['key']))})

# --- VIGENERE CIPHER ROUTES ---
@app.route('/api/vigenere/encrypt', methods=['POST'])
def vigenere_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = data['key']
    encrypted_text = vigenere_cipher.vigenere_encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/vigenere/decrypt', methods=['POST'])
def vigenere_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = data['key']
    decrypted_text = vigenere_cipher.vigenere_decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})

# --- RAIL FENCE CIPHER ROUTES ---
@app.route('/api/railfence/encrypt', methods=['POST'])
def railfence_encrypt():
    data = request.json
    plain_text = data['plain_text']
    num_rails = int(data['num_rails'])
    encrypted_text = rail_fence_cipher.rail_fence_encrypt(plain_text, num_rails)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/railfence/decrypt', methods=['POST'])
def railfence_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    num_rails = int(data['num_rails'])
    decrypted_text = rail_fence_cipher.rail_fence_decrypt(cipher_text, num_rails)
    return jsonify({'decrypted_text': decrypted_text})

# --- PLAYFAIR CIPHER ROUTES ---
@app.route('/api/playfair/encrypt', methods=['POST'])
def playfair_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = data['key']
    encrypted_text = playfair_cipher.playfair_encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/playfair/decrypt', methods=['POST'])
def playfair_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = data['key']
    decrypted_text = playfair_cipher.playfair_decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)