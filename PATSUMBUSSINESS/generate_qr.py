import qrcode

# Replace this with your IP address and port
url = 'http://192.168.0.103:8000'

# Generate QR Code
qr = qrcode.make(url)

# Save it to a file
qr.save('qr_code.png')

print("✅ QR code generated and saved as qr_code.png")
