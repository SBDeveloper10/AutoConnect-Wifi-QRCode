import qrcode


id = "Your Internet ID"
password = "Your Internet Password"
qrcode = qrcode.QRCode()
qrcode.add_data(f"{id}/{password}")
qrcode.make_image().save("1.png")
