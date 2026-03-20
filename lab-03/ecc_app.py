import sys
import requests
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox

class ECCApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(ECCApp, self).__init__()
        # Load file giao diện ECC
        uic.loadUi('ui/ecc.ui', self)
        
        self.api_url = "http://127.0.0.1:5000/api/ecc"

        # Kết nối các nút bấm
        self.btn_gen_keys.clicked.connect(self.generate_keys)
        self.btn_sign.clicked.connect(self.sign)
        self.btn_verify.clicked.connect(self.verify)

    def generate_keys(self):
        res = requests.get(f"{self.api_url}/generate_keys")
        QMessageBox.information(self, "ECC", res.json()['message'])

    def sign(self):
        msg = self.txt_info.toPlainText()
        res = requests.post(f"{self.api_url}/sign", json={"message": msg})
        self.txt_signature.setPlainText(res.json()['signature'])

    def verify(self):
        msg = self.txt_info.toPlainText()
        sig = self.txt_signature.toPlainText()
        res = requests.post(f"{self.api_url}/verify", json={"message": msg, "signature": sig})
        
        if res.json()['is_verified']:
            QMessageBox.information(self, "Xác thực", "Chữ ký HỢP LỆ ✅")
        else:
            QMessageBox.critical(self, "Xác thực", "Chữ ký SAI ❌")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = ECCApp()
    window.show()
    sys.exit(app.exec_())