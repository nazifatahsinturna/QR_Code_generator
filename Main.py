import qrcode

#qr code generator function
def generate_qr_code(text, filename): #function to genrate qrcode
    #qrcode make()
    image_qrcode = qrcode.make(text)
    #save the image
    image_qrcode.save(filename+".jpg")


text = input("Enter The text ot URL to convert into QR Code: ")
filename = input("Enter the filename to save the qrcode: ")

generate_qr_code(text, filename)