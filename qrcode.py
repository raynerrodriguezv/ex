# metodo #1

# pip install qrcode[pil]

# import qrcode



# import qrcode
# qr = qrcode.QRCode(version=1,
#                     error_correction=qrcode.constants.ERROR_CORRECT_L,
#                     box_size=50,
#                     border=1)

                     
# qr.add_data("https://towardsdatascience.com/generate-qrcode-with-python-in-5-lines-42eda283f325")
# qr.make(fit=True)

# img = qr.make_image(fill_color="black", back_color="white")
# img.save("foto_QR.png")


# metodo #2

# import qrcode# Link for website
# input_data = "https://towardsdatascience.com/face-detection-in-10-lines-for-beginners-1787aa1d9127"#Creating an instance of qrcode
# qr = qrcode.QRCode(
#         version=1,
#         box_size=10,
#         border=5)qr.add_data(input_data)
# qr.make(fit=True)img = qr.make_image(fill='black', back_color='white')
# img.save('qrcode001.png')