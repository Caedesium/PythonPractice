!#/usr/bin/env Python3

# This one was interesting. It's a QR code scanner, made for a fun project

import qrcode

def create_qr_code(data, filename):
    # Create a QRCode instance with specified parameters
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )

    # Add the data to the QRCode instance
    qr.add_data(data)

    # Generate the QR code matrix
    qr.make(fit=True)

    # Create an image from the QR code matrix
    image = qr.make_image(fill_color="black", back_color="white")

    # Save the QR code image to the specified filename
    image.save(filename)

def decode_qr_code(image_path):
    # Create a QRCode instance
    qr = qrcode.QRCode()

    # Open the QR code image file
    with open(image_path, "rb") as f:
        # Load the QR code image
        qr_img = qrcode.image.load(f)

        # Extract the data from the QR code image
        qr_img_data = qr.extract(qr_img)

        # Decode the extracted data
        return qr_img_data.data.decode()

def main():
    # Prompt the user to enter the data to encode in the QR code
    user_input = input("Enter the data to encode in the QR code: ")

    # Create a QR code image based on the user input
    create_qr_code(user_input, "qr_code.png")
    print("QR code created successfully.")

    # Decode the information from the generated QR code image
    decoded_data = decode_qr_code("qr_code.png")
    print("Decoded data:", decoded_data)

if __name__ == "__main__":
    main()
	
	

# The qrcode library is a Python library that provides functionality for generating QR (Quick Response) codes. QR codes are two-dimensional 
# barcodes that can store various types of data, such as text, URLs, contact information, and more. They are widely used for encoding and 
# decoding information in a compact and easily scannable format.

# The qrcode library allows you to create QR codes programmatically in your Python scripts. It offers a simple and straightforward API for 
# generating QR codes with various customization options.


# 1. Creating a QR code:
# First, you create an instance of the QRCode class from the qrcode module. You can specify parameters such as version, error 
#         correction level, box size, and border size.
# You add the data you want to encode to the QRCode instance using the add_data method.
# Next, you generate the QR code matrix using the make method. The library automatically determines the appropriate QR code 
#         version based on the data size and the specified parameters.
# The QR code matrix represents the black and white pattern of the QR code.
# You can then create an image from the QR code matrix using the make_image method, specifying the fill color for the black 
#         modules and the background color for the white modules.


# 2. Saving and displaying the QR code:
# Once you have the QR code image, you can save it to a file using the save method of the image object. Specify the desired filename 
#         and the file format (e.g., PNG, JPEG).
# The saved QR code image can be displayed, printed, or shared as needed.


# 3. Decoding a QR code:
# To decode a QR code, you use the extract method of the QRCode class.
# Open the QR code image file using the open function in binary read mode.
# Load the QR code image using the load method from qrcode.image. This creates an image object that represents the QR code.
# Extract the data from the QR code image using the extract method of the QRCode instance. This returns a DecodedData object.
# Finally, you can access the decoded data from the DecodedData object, typically as a string representation.


# The qrcode library is a convenient and easy-to-use tool for generating and decoding QR codes in Python. It simplifies the 
# process of working with QR codes and allows you to integrate QR code functionality into your applications, projects, or scripts
# with minimal effort.

