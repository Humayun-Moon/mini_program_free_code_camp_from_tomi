from PIL import Image

def resize_image (size1, size2):
    image = Image.open('humayun.jpg')
    print(f"Current size : {image.size}") 

    resized_image = image.resize((size1, size2))

    resized_image.save('humayun-image-' + str(size1) + '.jpg')

size1 = int(input("Enter Witdh: "))    
size2 = int(input("Enter Length: "))    

resize_image(size1, size2)



    