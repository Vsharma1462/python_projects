import qrcode as qr
from PIL import Image

qr1=qr.QRCode(version=1,error_correction=qr.constants.ERROR_CORRECT_H,box_size=10,border=4,)

qr1.add_data("https://www.wscubetech.com/")
qr1.make(fit=True)

img=qr1.make_image(fill_color="red",back_color="white")
img.save("youtube2.png")
