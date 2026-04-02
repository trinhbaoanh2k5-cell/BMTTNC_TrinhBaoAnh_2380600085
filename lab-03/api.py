from flask import Flask, request, jsonify
from flask_cors import CORS
# Import cả 2 class logic
from cipher.rsa.rsa_cipher import RSACipher
from cipher.ecc.ecc_cipher import ECCCipher

app = Flask(__name__)
CORS(app)

# Khởi tạo công cụ
rsa_tool = RSACipher()
ecc_tool = ECCCipher()

# ================= RSA ROUTES =================

@app.route('/api/rsa/generate_keys', methods=['GET'])
def rsa_generate():
    rsa_tool.generate_keys()
    return jsonify({'message': 'Tạo cặp khóa RSA thành công!'})

@app.route('/api/rsa/encrypt', methods=['POST'])
def rsa_encrypt():
    data = request.json
    _, pub_key = rsa_tool.load_keys()
    result = rsa_tool.encrypt(data['message'], pub_key)
    return jsonify({'encrypted_message': result})

@app.route('/api/rsa/decrypt', methods=['POST'])
def rsa_decrypt():
    data = request.json
    priv_key, _ = rsa_tool.load_keys()
    result = rsa_tool.decrypt(data['cipher_text'], priv_key)
    return jsonify({'decrypted_message': result})

@app.route('/api/rsa/sign', methods=['POST'])
def rsa_sign():
    data = request.json
    priv_key, _ = rsa_tool.load_keys()
    signature = rsa_tool.sign(data['message'], priv_key)
    return jsonify({'signature': signature})

@app.route('/api/rsa/verify', methods=['POST'])
def rsa_verify():
    data = request.json
    _, pub_key = rsa_tool.load_keys()
    is_verified = rsa_tool.verify(data['message'], data['signature'], pub_key)
    return jsonify({'is_verified': is_verified})

# ================= ECC ROUTES =================

@app.route('/api/ecc/generate_keys', methods=['GET'])
def ecc_generate():
    ecc_tool.generate_keys()
    return jsonify({'message': 'Tạo cặp khóa ECC thành công!'})

@app.route('/api/ecc/sign', methods=['POST'])
def ecc_sign():
    data = request.json
    # ECC dùng SigningKey (sk) để ký
    sk, _ = ecc_tool.load_keys()
    signature = ecc_tool.sign(data['message'], sk)
    return jsonify({'signature': signature})

@app.route('/api/ecc/verify', methods=['POST'])
def ecc_verify():
    data = request.json
    # ECC dùng VerifyingKey (vk) để xác thực
    _, vk = ecc_tool.load_keys()
    is_verified = ecc_tool.verify(data['message'], data['signature'], vk)
    return jsonify({'is_verified': is_verified})

# ================= MAIN =================

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)