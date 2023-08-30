import socket as s


hostn = s.gethostname()

IPAD = s.gethostbyname(hostn)

print(f"Endereço de IP: {IPAD}")
