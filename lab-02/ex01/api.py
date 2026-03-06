from flask import Flask, request, jsonify
from cipher.caesar.caesar_cipher import CaesarCipher

app = Flask(__name__)
caesar = CaesarCipher()

@app.route("/api/caesar/encrypt", methods=["POST"])
def encrypt():
    data = request.json
    return jsonify({'encrypted_message': caesar.encrypt_text(data['plain_text'], int(data['key']))})

@app.route("/api/caesar/decrypt", methods=["POST"])
def decrypt():
    data = request.json
    return jsonify({'decrypted_message': caesar.decrypt_text(data['cipher_text'], int(data['key']))})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)