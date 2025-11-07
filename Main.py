from qr_code_color import generate_qr_code
from qr_code_with_logo import generate_qr_code_logo


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

generate_qr_code_logo(text, filename, color)