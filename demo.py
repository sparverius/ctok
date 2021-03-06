# Reproduce the code in README.md.
from token import *

import ctok

tok = ctok.CTok(b"(hello+world)")
for token in tok:
    print(token)

print("Raw:")
tok = ctok.CTok(b"(hello+world)")
while True:
    token = tok.get_raw()
    print(token)
    if token[0] in (ENDMARKER, ERRORTOKEN):
        break
