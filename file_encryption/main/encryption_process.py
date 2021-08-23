from PyQt5.QtCore import endl
from cryptography.fernet import Fernet
import base64
import json

class encryption_pro:

    def __init__(self):
        self.key_dir_path = list()
        self.json_file_path = 'C:\ProgramData\security\data.api'
        self.file_list = dict()
        self.data = b''
        self.file_key = b''
        self.json_key = b''
        self.login_str = b'404_not_found'
        self.login_key_str = b''

    def login(self, path):
        try:
            with open(path, 'r') as key_file:
                data = key_file.read().split(',')
                login_fernet = Fernet(data[0].encode('ascii'))
                key = data[2].encode('ascii')
                print(data) 
            
            with open(self.json_file_path, 'r') as file:
                file_data = file.read().split(',')
                file_key = file_data[0].encode('ascii')

            if self.login_str == login_fernet.decrypt(key) and self.login_str == login_fernet.decrypt(file_key):
                self.json_key = data[0].encode('ascii')
                self.file_key = data[1].encode('ascii')
                self.login_key_str = login_fernet.encrypt(self.login_str)
                return 0

            else:
                return 1
                
        except Exception as e:
            print(e)

    def save_file_data(self):
        with open(self.json_file_path, 'w') as file:
            json_data = json.dumps(self.file_list, ensure_ascii=False, indent=4).encode('ascii')
            file_data = base64.b64encode(json_data)
            encrypt_data = self.json_fernet.encrypt(file_data)
            data = encrypt_data.decode('ascii')
            data = self.login_key_str.decode('ascii') + ',' + data
            file.write(data)
    
    def save_key(self):
        pass

    def load_file_data(self):
        with open(self.json_file_path, 'r') as file:
            data = file.read().split(',')
            file_data = data[1].encode('ascii')
            decode_data = self.json_fernet.decrypt(file_data)
            json_data = base64.b64decode(decode_data).decode('ascii')
            self.file_list = json.loads(json_data)
            print(self.file_list)
    
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
