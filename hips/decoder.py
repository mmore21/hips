from cryptography.fernet import Fernet

print("Enter Key:")
key_str = input()
key_bytes = key_str.encode()

f = Fernet(key_bytes)
print("\nEnter Capture:")
capture_str = input()
capture_bytes = capture_str.encode()

print("\nMessage:")
print(f.decrypt(capture_bytes).decode())