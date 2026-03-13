from flask import Flask, render_template, request
from cipher.caesar.caesar_cipher import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
from cipher.playfair.playfair_cipher import PlayfairCipher
from cipher.transposition import TranspositionCipher

app = Flask(__name__)

# Khởi tạo các class
caesar = CaesarCipher()
vigenere = VigenereCipher()
railfence = RailFenceCipher()
playfair = PlayfairCipher()
transposition = TranspositionCipher()

@app.route("/")
def home():
    return render_template('index.html')

# --- ROUTE HIỂN THỊ TRANG ---
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

# --- LOGIC XỬ LÝ (ĐÃ ĐỒNG BỘ URL) ---
@app.route("/caesar/<action>", methods=['POST'])
def caesar_logic(action):
    key = int(request.form['inputKey'])
    if action == 'encrypt':
        text = request.form['inputPlainText']
        result = caesar.encrypt_text(text, key)
    else:
        text = request.form['inputCipherText']
        result = caesar.decrypt_text(text, key)
    return f"<h3>Caesar {action} Result</h3>Result: {result}"

@app.route("/vigenere/<action>", methods=['POST'])
def vigenere_logic(action):
    key = request.form['inputKey']
    if action == 'encrypt':
        text = request.form['inputPlainText']
        result = vigenere.vigenere_encrypt(text, key)
    else:
        text = request.form['inputCipherText']
        result = vigenere.vigenere_decrypt(text, key)
    return f"<h3>Vigenere {action} Result</h3>Result: {result}"

@app.route("/railfence/<action>", methods=['POST'])
def railfence_logic(action):
    key = int(request.form['inputKey'])
    if action == 'encrypt':
        text = request.form['inputPlainText']
        result = railfence.rail_fence_encrypt(text, key)
    else:
        text = request.form['inputCipherText']
        result = railfence.rail_fence_decrypt(text, key)
    return f"<h3>Rail Fence {action} Result</h3>Result: {result}"

@app.route("/playfair/<action>", methods=['POST'])
def playfair_logic(action):
    key = request.form['inputKey']
    if action == 'encrypt':
        text = request.form['inputPlainText']
        result = playfair.playfair_encrypt(text, key)
    else:
        text = request.form['inputCipherText']
        result = playfair.playfair_decrypt(text, key)
    return f"<h3>Playfair {action} Result</h3>Result: {result}"

@app.route("/transposition/<action>", methods=['POST'])
def transposition_logic(action):
    key = int(request.form['inputKey'])
    if action == 'encrypt':
        text = request.form['inputText']
        result = transposition.encrypt(text, key)
    else:
        text = request.form['inputCipherText']
        result = transposition.decrypt(text, key)
    return f"<h3>Transposition {action} Result</h3>Result: {result}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)