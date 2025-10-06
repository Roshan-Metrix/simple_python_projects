import qrcode 
from PIL import Image

qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size=10,border=4,)
data = input("Enter the name, link etc. to create QR : ")
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill_color="black",back_color="white")
img.save("wscude_yt.png")

# first install qr , pillow modules using pip 
# compile and add the link for generating its QR

