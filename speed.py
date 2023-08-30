
# pip install speedtest-cli
import speedtest

test = speedtest.Speedtest()
down = test.download()
upload = test.upload()

print(f"Velocidade de download: {down}")
print(f"Velocidade de upload: {upload}")
