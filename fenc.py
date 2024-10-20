
import sys
from Crypto.Cipher import AES
from Crypto import Random
import base64

BLOCK_SIZE = 16
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(
    BLOCK_SIZE - len(s) % BLOCK_SIZE
)
unpad = lambda s: s[: -ord(s[len(s) - 1:])]


def _r(fpath: str):
    return open(fpath).read()


def _rb(fpath: str):
    return open(fpath, 'rb').read()


def encrypt_str(raw, password):
    private_key = password.encode("utf-8")
    raw = pad(raw)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(private_key, AES.MODE_CFB, iv)
    return base64.b64encode(iv + cipher.encrypt(raw.encode("utf-8")))


if __name__ == '__main__':
    print()
    try:
        fpath = sys.argv[1]
        ekey = sys.argv[2]
        fc = _rb(fpath)
        fc = base64.b64encode(fc).decode()
        try:
            enc = encrypt_str(fc, ekey)
        except Exception as e:
            print(e)
            sys.exit(1)
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        print()
        print(enc)
        print()
        print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
    except:
        print('error: no file path provided')
        print()
