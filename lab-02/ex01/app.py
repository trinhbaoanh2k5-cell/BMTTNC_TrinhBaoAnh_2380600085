from flask import Flask, render_template, request
from cipher.caesar.caesar_cipher import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
from cipher.playfair import PlayfairCipher
from cipher.transposition import TranspositionCipher

app = Flask(__name__)

# Khởi tạo các class logic
caesar = CaesarCipher()
vigenere = VigenereCipher()
railfence = RailFenceCipher()
playfair = PlayfairCipher()
transposition = TranspositionCipher()

@app.route("/")
def home():
    return render_template('index.html')

# --- ROUTES HIỂN THỊ TRANG ---
@app.route("/caesar")
def caesar_page(): return render_template('caesar.html')

@app.route("/vigenere")
def vigenere_page(): return render_template('vigenere.html')

@app.route("/railfence")
def railfence_page(): return render_template('railfence.html')

@app.route("/playfair")
def playfair_page(): return render_template('playfair.html')

@app.route("/transposition")
def transposition_page(): return render_template('transposition.html')

# --- ROUTE XỬ LÝ CAESAR ---
@app.route("/caesar/encrypt", methods=['POST'])
def c_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    result = caesar.encrypt_text(text, key)
    return f"<h3>Caesar Result</h3>Original: {text}<br>Key: {key}<br>Encrypted: {result}"

@app.route("/caesar/decrypt", methods=['POST'])
def c_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    result = caesar.decrypt_text(text, key)
    return f"<h3>Caesar Result</h3>Cipher: {text}<br>Key: {key}<br>Decrypted: {result}"

# --- ROUTE XỬ LÝ VIGENERE ---
@app.route("/vigenere/encrypt", methods=['POST'])
def v_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKey']
    result = vigenere.vigenere_encrypt(text, key)
    return f"<h3>Vigenere Result</h3>Original: {text}<br>Key: {key}<br>Encrypted: {result}"

@app.route("/vigenere/decrypt", methods=['POST'])
def v_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKey']
    result = vigenere.vigenere_decrypt(text, key)
    return f"<h3>Vigenere Result</h3>Cipher: {text}<br>Key: {key}<br>Decrypted: {result}"

# --- ROUTE XỬ LÝ RAIL FENCE ---
@app.route("/railfence/encrypt", methods=['POST'])
def r_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKey'])
    result = railfence.rail_fence_encrypt(text, key)
    return f"<h3>Rail Fence Result</h3>Original: {text}<br>Key: {key}<br>Encrypted: {result}"

@app.route("/railfence/decrypt", methods=['POST'])
def r_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKey'])
    result = railfence.rail_fence_decrypt(text, key)
    return f"<h3>Rail Fence Result</h3>Cipher: {text}<br>Key: {key}<br>Decrypted: {result}"

# --- ROUTE XỬ LÝ PLAYFAIR ---
@app.route("/playfair/encrypt", methods=['POST'])
def p_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKey']
    result = playfair.playfair_encrypt(text, key)
    return f"<h3>Playfair Result</h3>Original: {text}<br>Key: {key}<br>Encrypted: {result}"

@app.route("/playfair/decrypt", methods=['POST'])
def p_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKey']
    result = playfair.playfair_decrypt(text, key)
    return f"<h3>Playfair Result</h3>Cipher: {text}<br>Key: {key}<br>Decrypted: {result}"

# --- ROUTE XỬ LÝ TRANSPOSITION ---
@app.route("/transposition/encrypt", methods=['POST'])
def trans_encrypt():
    text = request.form['inputText']
    key = int(request.form['inputKey'])
    result = transposition.encrypt(text, key)
    return f"<h3>Transposition Result</h3>Original: {text}<br>Key: {key}<br>Encrypted: {result}"

@app.route("/transposition/decrypt", methods=['POST'])
def trans_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKey'])
    result = transposition.decrypt(text, key)
    return f"<h3>Transposition Result</h3>Cipher: {text}<br>Key: {key}<br>Decrypted: {result}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)