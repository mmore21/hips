# hips - Hidden in Ping Sight

![GitHub](https://img.shields.io/github/license/mmore21/hips)

Steganography P2P system using encrypted payloads in ICMP ping packets.

## Usage

### Setup

The following requirements are needed to run hips:

* Python 3
* pipenv

After installing the necessary dependencies, clone or download this repository to a desired location. Ensure that you have the proper requirements before running the respective scripts. Administrative privileges are required to run certain portions of the program.

<pre>
git clone https://github.com/mmore21/hips.git
cd hips/
sudo pipenv install -r requirements.txt
</pre>

### Send Ping

To send an encrypted ping, run the following command:

<pre>
sudo pipenv run python3 hips/ping.py
</pre>

Example of the ping.py script:

<pre>
Enter IP Address:
192.168.1.1

Generate New Key? (Y/n)
Y

Please save the following key to a secure location. It cannot be regenerated.
qGp_wi8gZlWeCTjrBjf1cKje87QVwYf9GHHpzwAE8Vo=

Enter Message:
Hello world!

Sending ping...
Reply from 192.168.1.1, 108 bytes in 0.34ms
</pre>

### Decode Ping (Manual)

To decrypt an encrypted ping by manually intercepting the ping packet, run the following command:

<pre>
sudo pipenv run python3 hips/decoder.py
</pre>

Example of the decoder.py script:

<pre>
Enter Key:
qGp_wi8gZlWeCTjrBjf1cKje87QVwYf9GHHpzwAE8Vo=

Enter Capture:
gAAAAABedVaAwGNT-XwWxU5RaGHd9u8GdFDtslZsVPxH-CIzDTQA4eb6KmZeJZAU72fBCoiUs9JUqc6ChxHCAnQtJJNzUd7txA==

Message:
Hello world!
</pre>

The capture in the above example refers to the encrypted message within the payload of the captured ICMP message. A packet analyzer is required to capture the ping. An automated script using tcpdump as a packet analyzer is also described below.

### Decode Ping (Automated)

Note, this process requires a tcpdump installation:

<pre>
sudo apt install tcpdump
</pre>

To decrypt an enrypted ping using an automated tcpdump process, run the following command:

<pre>
sudo pipenv run python3 hips/sniffer.py
</pre>

## Requirements

Python 3 and pipenv are required to install install the requirements:

* cryptography
* pythonping

If not using the automated sniffer, a packet analyzer such as Wireshark or tcpdump will be required to capture the ping sent over the network.

## License

hips is available under the [MIT License](https://github.com/mmore21/hips/blob/master/LICENSE).

