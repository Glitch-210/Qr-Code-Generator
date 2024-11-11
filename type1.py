import qrcode as qr
img = qr.make("Hello Avengers")
img.save("image.png")