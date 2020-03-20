from cryptography.fernet import Fernet
from pythonping import ping

# Get IP address to ping
print("Enter IP Address:")
ip_addr = input()

# Generate key
print("\nGenerate New Key? (Y/n)")
gen_key_str = input().lower()
if gen_key_str == "y" or gen_key_str == "":
    key_bytes = Fernet.generate_key()
    print("\nPlease save the following key to a secure location. It cannot be regenerated.")
    print(key_bytes.decode())
else:
    print("\nEnter Key:")
    key_str = input()
    key_bytes = key_str.encode()

f = Fernet(key_bytes)

# Receive and encrypt message
print("\nEnter Message:")

msg_str = input()
msg_bytes = msg_str.encode()

token = f.encrypt(msg_bytes)

# Store encrypted message into ping payload
print("\nSending ping...")
response = ping(ip_addr, count=1, payload=bytes(token), verbose=True)