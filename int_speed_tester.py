from speedtest import Speedtest

wifi = Speedtest()
print("Getting the Download Speed...")
download = wifi.download()
print(f"Download: {download / 1000000:.2f} Mbps")
print("Getting the Upload Speed...")
upload = wifi.upload()
print(f"Upload: {upload / 1000000:.2f} Mbps")
