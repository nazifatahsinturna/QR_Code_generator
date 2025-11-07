import qrcode

#qr code generator function
def generate_qr_code(text, filename, color): #function to genrate qrcode
    qr = qrcode.QRCode (
        version=1,
        box_size=10,
        border=2
    )

    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_image(fill_color=color, back_color='white')
    img.save(filename+".png")
