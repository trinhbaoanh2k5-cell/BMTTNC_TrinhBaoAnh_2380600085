from flask import Flask, request, jsonify
from cipher.caesar.caesar_cipher import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
from cipher.playfair.playfair_cipher import PlayfairCipher
from cipher.transposition import TranspositionCipher

app = Flask(__name__)

# Khởi tạo các class logic
caesar = CaesarCipher()
vigenere = VigenereCipher()
railfence = RailFenceCipher()
playfair = PlayfairCipher()
transposition = TranspositionCipher()

# --- CAESAR CIPHER ---
@app.route("/api/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    data = request.json
    return jsonify({"encrypted_message": caesar.encrypt_text(data['plain_text'], int(data['key']))})

@app.route("/api/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    data = request.json
    return jsonify({"decrypted_message": caesar.decrypt_text(data['cipher_text'], int(data['key']))})

# --- VIGENERE CIPHER ---
@app.route("/api/vigenere/encrypt", methods=["POST"])
def vigenere_encrypt():
    data = request.json
    return jsonify({"encrypted_message": vigenere.vigenere_encrypt(data['plain_text'], data['key'])})

@app.route("/api/vigenere/decrypt", methods=["POST"])
def vigenere_decrypt():
    data = request.json
    return jsonify({"decrypted_message": vigenere.vigenere_decrypt(data['cipher_text'], data['key'])})

# --- RAIL FENCE CIPHER ---
@app.route("/api/railfence/encrypt", methods=["POST"])
def railfence_encrypt():
    data = request.json
    return jsonify({"encrypted_message": railfence.rail_fence_encrypt(data['plain_text'], int(data['key']))})

@app.route("/api/railfence/decrypt", methods=["POST"])
def railfence_decrypt():
    data = request.json
    return jsonify({"decrypted_message": railfence.rail_fence_decrypt(data['cipher_text'], int(data['key']))})

# --- PLAYFAIR CIPHER ---
@app.route("/api/playfair/creatematrix", methods=["POST"])
def playfair_matrix():
    data = request.json
    return jsonify({"matrix": playfair.generate_matrix(data['key'])})

@app.route("/api/playfair/encrypt", methods=["POST"])
def playfair_encrypt_api():
    data = request.json
    return jsonify({"encrypted_message": playfair.playfair_encrypt(data['plain_text'], data['key'])})

@app.route("/api/playfair/decrypt", methods=["POST"])
def playfair_decrypt_api():
    data = request.json
    return jsonify({"decrypted_message": playfair.playfair_decrypt(data['cipher_text'], data['key'])})

# --- TRANSPOSITION CIPHER ---
@app.route("/api/transposition/encrypt", methods=["POST"])
def trans_encrypt():
    data = request.json
    return jsonify({"encrypted_message": transposition.encrypt(data['plain_text'], int(data['key']))})

@app.route("/api/transposition/decrypt", methods=["POST"])
def trans_decrypt():
    data = request.json
    return jsonify({"decrypted_message": transposition.decrypt(data['cipher_text'], int(data['key']))})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)