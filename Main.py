import qrcode

#qr code generator function
def generate_qr_code(text, filename, color): #function to genrate qrcode
     qr = qrcode.ORCode (
         version=1,
         box_size=10,
         border=5
     )
    # #qrcode make()
    # image_qrcode = qrcode.make(text)
    # #save the image
    # image_qrcode.save(filename+".jpg")


text = input("Enter The text ot URL to convert into QR Code: ")
filename = input("Enter the filename to save the qrcode: ")

color = ' '

while(True): #letting the use choose
    color = input("Pick a color (red, blue green, black): ")

    if color.lower() != 'red' and color.lower() != 'blue' and color.lower() != 'green' and color.lower() != 'black':
        print("Invalid Choice")
    else:
        break

generate_qr_code(text, filename, colorhttps://github.com/nazifatahsinturna)