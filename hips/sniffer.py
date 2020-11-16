import sys
import subprocess as sub
import decoder

def capture_packet():
    encoded_msg = ""
    fragments = []

    # Creates a pipe stream to a tcpdump process
    p = sub.Popen(('sudo', 'tcpdump', '-l', '-nnvvXSs', '0', 'icmp'), stdout=sub.PIPE)

    for row in iter(p.stdout.readline, b''):
        raw_data = row.rstrip()
        str_data = raw_data.decode("utf-8")

        fragments.append(str_data.split(' ')[-1])

        encoded_msg = ''.join(fragments)

        # Find encrypted message within the ping payload
        pos = encoded_msg.find("gAAAAA")

        if encoded_msg.endswith("="):
            captured_str = encoded_msg[pos:]
            print(captured_str)
            return captured_str 

    return ""

def run_loop(key):
    while True:
        print("\n(0) Exit\n(1) Capture")
        cmd = input()

        if cmd == "0":
            return

        captured_str = capture_packet()

        # Decrypt and output the encrypted message
        if captured_str:
            capture_bytes = captured_str.encode()
            decoder.decrypt_message(key=f, encoded_message=capture_bytes)

if __name__ == "__main__":
    f = decoder.get_fernet_key()
    run_loop(key=f)
