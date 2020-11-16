from cryptography.fernet import Fernet

# Get existing Fernet key
def get_fernet_key():
    print("Enter Key:")
    key_str = input()
    key_bytes = key_str.encode()
    return Fernet(key_bytes)

# Enter the encoded capture
def get_encoded_capture():
    print("\nEnter Capture:")
    capture_str = input()
    return capture_str.encode()

# Decrypt and output the encrypted message
def decrypt_message(key, encoded_message):
    print("\nMessage:")
    print(key.decrypt(encoded_message).decode())

if __name__ == "__main__":
    f = get_fernet_key()
    capture_bytes = get_encoded_capture()
    decrypt_message(key=f, encoded_message=capture_bytes)
