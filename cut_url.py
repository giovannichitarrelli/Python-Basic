# pip install pyshorteners

import pyshorteners as ps

url = "https://github.com/giovannichitarrelli"

cut = ps.Shortener().tinyurl.short(url)

print(cut)
