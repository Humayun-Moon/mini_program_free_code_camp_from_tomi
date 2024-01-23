import qrcode

def qrcode_generator(text):

    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border = 5

    )

    qr.add_data(text)
    qr.make(fit= True)
    ima = qr.make_image(fill_color = "black", back_color = "white")
    ima.save('my_image.png')

qrcode_generator("https://www.youtube.com")    