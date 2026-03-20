import sys
import requests
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox

class RSAApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(RSAApp, self).__init__()
        # Đường dẫn trỏ vào file rsa.ui bạn vừa lưu
        uic.loadUi('ui/rsa.ui', self) 
        
        self.api_url = "http://127.0.0.1:5000/api/rsa"

        # Kết nối các nút bấm với hàm xử lý
        # Lưu ý: Tên phải khớp chính xác với ObjectName trong Qt Designer
        self.btn_gen_keys.clicked.connect(self.generate_keys)
        self.btn_encrypt.clicked.connect(self.encrypt)
        self.btn_decrypt.clicked.connect(self.decrypt)
        self.btn_sign.clicked.connect(self.sign)
        self.btn_verify.clicked.connect(self.verify)

    def generate_keys(self):
        res = requests.get(f"{self.api_url}/generate_keys")
        QMessageBox.information(self, "Thành công", res.json()['message'])

    def encrypt(self):
        msg = self.txt_plain_text.toPlainText()
        res = requests.post(f"{self.api_url}/encrypt", json={"message": msg})
        self.txt_cipher_text.setPlainText(res.json()['encrypted_message'])

    def decrypt(self):
        cipher = self.txt_cipher_text.toPlainText()
        res = requests.post(f"{self.api_url}/decrypt", json={"cipher_text": cipher})
        self.txt_plain_text.setPlainText(res.json()['decrypted_message'])

    def sign(self):
        msg = self.txt_info.toPlainText()
        res = requests.post(f"{self.api_url}/sign", json={"message": msg})
        self.txt_signature.setPlainText(res.json()['signature'])

    def verify(self):
        msg = self.txt_info.toPlainText()
        sign = self.txt_signature.toPlainText()
        res = requests.post(f"{self.api_url}/verify", json={"message": msg, "signature": sign})
        result = "Chữ ký HỢP LỆ ✅" if res.json()['is_verified'] else "Chữ ký GIẢ MẠO ❌"
        QMessageBox.information(self, "Xác thực", result)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = RSAApp()
    window.show()
    sys.exit(app.exec_())