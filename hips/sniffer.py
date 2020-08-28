from cryptography.fernet import Fernet
import subprocess as sub

print("Enter Key:")
key_str = input()
key_bytes = key_str.encode()

f = Fernet(key_bytes)

cmd = ""

while True:
    print("\n(0) Exit\n(1) Capture")
    cmd = input()

    if cmd == "0":
        break

    encoded_msg = ""
    fragments = []
    p = sub.Popen(('sudo', 'tcpdump', '-l', '-nnvvXSs', '0', 'icmp'), stdout=sub.PIPE)
    for row in iter(p.stdout.readline, b''):

        raw_data = row.rstrip()
        str_data = raw_data.decode("utf-8")

        fragments.append(str_data.split(' ')[-1])

        encoded_msg = ''.join(fragments)

        pos = encoded_msg.find("gAAAAA")

        if encoded_msg.endswith("="):
            captured_str = encoded_msg[pos:]
            print(captured_str)
            break


    capture_bytes = captured_str.encode()
    print("\nMessage:")
    print(f.decrypt(capture_bytes).decode())