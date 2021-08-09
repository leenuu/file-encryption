from cryptography import fernet
from cryptography.fernet import Fernet
import base64
import json

class encryption_pro:

    def __init__(self):
        self.dir_path = list()
        self.file_list = dict()
        self.data = b''
        self.key = b''
        self.encrypy_str = b''
        self.decrypy_str = b''
    
    def set_dir(self):
        pass

    def edit_list(self):
        pass
    
    def save_file_data(self):
        with open('data.dll', 'wb') as file:
            file = json.dumps(self.file_list)
    
    def load_file_data(self):
        pass


    def load_key(self):
        pass
        # self.key = Fernet.generate_key()
        # self.fernet = Fernet(self.key)
        # self.file_list['key'] = self.key

    def encode_cryption(self, file_name):
        with open(file_name, 'rb') as file:
            self.data = base64.b64encode(file.read())
        self.encrypy_str = self.fernet.encrypt(self.data)

    def decode_cryption(self, file_name):
        self.decrypy_str = self.fernet.decrypt(self.encrypy_str)
        with open(file_name, 'wb') as file:
            file.write(base64.b64decode(self.data))


    def encode_data_txt(self,file_name, data):
        with open(file_name, 'wb') as file:
            file.write(data)

    







    