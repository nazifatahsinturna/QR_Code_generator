import qrcode

#qr code generator function
def generate_qr_code(text, filename, color): #function to genrate qrcode
    qr = qrcode.QRCode (
        version=1,
        box_size=10,
        border=5
    )

    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_image(fill_color=color, back_color='white')
    img.save(filename+".png")



text = input("Enter The text ot URL to convert into QR Code: ")
filename = input("Enter the filename to save the qrcode: ")

color = ' '

while(True): #letting the use choose
    color = input("Pick a color (red, blue, green, black): ")

    if color.lower() != 'red' and color.lower() != 'blue' and color.lower() != 'green' and color.lower() != 'black':
        print("Invalid Choice")
    else:
        break

generate_qr_code(text, filename, color)