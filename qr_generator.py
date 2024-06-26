import qrcode

#getting the user inputs
data = input("Enter the website link which the qr image should be created: ")

#create the qr code for the link given
qr = qrcode.QRCode(
    version = 1,
    box_size = 10,
    border = 5
)

#add data to qr code
qr.add_data(data)
qr.make(fit=True)

#create the qr code image
img = qr.make_image(fill = "black", back_color = "white")

#save the qr code
img.save("qr.png")

print("QR code is saved succesfully as qr_code.png for the website link ",data)
