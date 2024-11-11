import qrcode as qr
from PIL import Image

qr1 = qr.QRCode(version=1,error_correction=qr.constants.ERROR_CORRECT_H,box_size=10,border=6)
qr1.add_data("https://github.com/Glitch-210/Qr-Code-Generator")
qr1.make(fit=True)

img = qr1.make_image(fill_color="black",back_color="white")
img.save("name11.png")