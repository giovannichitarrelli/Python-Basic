
import pyqrcode

url = pyqrcode.create("https://github.com/giovannichitarrelli")

url.png("qrcode.png", scale=8)

print(url.terminal(quiet_zone=1))
