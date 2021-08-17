from cryptography import fernet
from cryptography.fernet import Fernet
import base64
from io import BytesIO
from PIL import Image

# key = Fernet.generate_key()
# print(f'key: {key}')

dir = ""
data = b''
key = b'6pIZbq7DsV9-v6v_iQvm8gtgRZAOG2HS2vC7kAwG1LQ='

with open('test.png', 'rb') as img:
    data = base64.b64encode(img.read())

fernet = Fernet(key)
encrypy_str = fernet.encrypt(data)
decrypy_str = fernet.decrypt(encrypy_str)

with open("test_1.png", 'wb') as f:
    f.write(base64.b64decode(decrypy_str))



