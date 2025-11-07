from qr_code_color import generate_qr_code
from qr_code_with_logo import generate_qr_code_logo
from PIL import ImageColor

print()
text = input("Enter The text ot URL to convert into QR Code: ")
filename = input("Enter the filename to save the qrcode: ")

color = ' '

#Get all colors supported by pillow
valid_colors = ImageColor.colormap.keys()

while(True): #letting the use choose
    color = input("Pick a color: ").lower()

    if color not in valid_colors :
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
