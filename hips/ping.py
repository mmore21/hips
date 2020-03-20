from cryptography.fernet import Fernet
from pythonping import ping

print("Enter Message:")
key = Fernet.generate_key()
f = Fernet(key)

msg_str = input()
msg_bytes = msg_str.encode()

token = f.encrypt(msg_bytes)

response = ping('192.168.1.1', count=1, payload=bytes(token), verbose=True)

print("Enter Capture:")
capture_str = input()
capture_bytes = capture_str.encode()
print(f.decrypt(capture_bytes))