import qrcode
from PIL import Image


#qr code generator function with logo
def generate_qr_code_logo(text, filename, color): #function to genrate qrcode
    qr = qrcode.QRCode (
        version=2,
        box_size=10,
        border=2,
        error_correction=qrcode.constants.ERROR_CORRECT_H
    )

    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_image(fill_color=color, back_color='white')

    logo_path = input("Please, provide the logo path: ")
    try:#if it can't fild the logo
         logo = Image.open(logo_path)
    except FileNotFoundError:
         print("Cannot find logo")
         return
    
    qr_width, qr_height = img.size #getting height and width for qrcode

    logo_size = int(qr_width*0.2) #20% of qr code

    logo = logo.resize((logo_size, logo_size), Image.Resampling.LANCZOS) # resizing the logo

    #center the logo on the QR code

    pos = ((qr_width-logo_size) // 2), ((qr_height- logo_size) //2)

    img.paste(logo, pos) #pasting the logo on qrcode

   
    img.save(filename+".png")


text = input("Enter The text ot URL to convert into QR Code: ")
filename = input("Enter the filename to save the qrcode: ")

color = 'black'

