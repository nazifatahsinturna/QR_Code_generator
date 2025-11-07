from qr_code_color import generate_qr_code
from qr_code_with_logo import generate_qr_code_logo

print()
text = input("Enter The text ot URL to convert into QR Code: ")
filename = input("Enter the filename to save the qrcode: ")

color = ' '

while(True): #letting the use choose
    color = input("Pick a color (red, blue, green, black, indigo, navy): ")
    color = color.lower()

    if color!= "red" and color != "blue" and color != "green" and color != "black" and color != "indigo" and color != "navy" :
        print("Invalid Choice")
    else:
        break


choice = input("Enter 1 for QR code with logo and 2 for without it: ")
if choice == "1":
    generate_qr_code_logo(text, filename, color)
elif choice == "2":
    generate_qr_code(text, filename, color)
else:
    print("Invalid choice")
