import qrcode
data = "https://www.youtube.com/watch?v=sbPFE4TdLyU"
qr = qrcode.QRCode(
    version=15,  
    box_size=10,
    border=5   
)
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill="black", back_color="white")
img.save("test.png")
print("✅ QR Code generated and saved as test.png")
