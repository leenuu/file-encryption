from PyQt5.QtCore import endl
from cryptography import fernet
from cryptography.fernet import Fernet
import base64
import json

class encryption_pro:

    def __init__(self):
        self.dir_path = list()
        self.file_list = dict()
        self.data = b''
        self.file_key = b'xkJhItdCBlyCeyc20gmfgl3Xdq-j1oRvi2XFABHafts='
        self.json_key = b'kds2SWt2Hc6Sd9rb9rsnc0W__r2v3ZPPPMqviA1Fvn4='
        self.encrypy_str = b''
        self.decrypy_str = b''

        self.load_key()

    def set_dir(self):
        pass

    def edit_list(self):
        pass
    
    def save_file_data(self):
        with open('data.json', 'w') as file:
            json_data = json.dumps(self.file_list, ensure_ascii=False, indent=4)
            file.write(json_data)

    def load_file_data(self):
        pass
    
    def load_key(self):
        self.file_fernet = Fernet(self.file_key)
        self.json_fernet = Fernet(self.json_key)
        # self.file_list['file_key'] = self.file_key.decode('utf-8')
        # self.file_list["json_key"] = self.json_key.decode('utf-8')
      
    def open_data(self, file_name):
        with open(file_name, 'rb') as file:
            data = base64.b64encode(file.read())
        
        data = data.decode("ascii")
        return data

    def encode_cryption(self, file_name):
        with open(file_name, 'rb') as file:
            file_data = base64.b64encode(file.read()) 
            encrypt_data = self.file_fernet.encrypt(file_data)
            data = encrypt_data.decode('ascii')
        return data

    def decode_cryption(self, file_name, data):
        file_data = data.encode('ascii')
        decode_data = self.file_fernet.decrypt(file_data)
        base64_data = base64.b64decode(decode_data)
        with open(file_name, 'wb') as file:
            file.write(base64_data)



    







    