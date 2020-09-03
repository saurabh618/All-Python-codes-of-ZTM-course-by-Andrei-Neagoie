from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')
print(img)
print(img.format)
print(img.size)
print(img.mode)

filtered_img = img.filter(ImageFilter.BLUR)
filtered_img.save("./Pokedex/blur.png", "png")

filtered_img = img.filter(ImageFilter.SMOOTH)
filtered_img.save("./Pokedex/smooth.png", "png")

filtered_img = img.filter(ImageFilter.SHARPEN)
filtered_img.save("./Pokedex/sharpen.png", "png")

filtered_img = img.convert('L')  # it converts the image to grey scale, that is Black and White. Similarly RGB = Red Green Blue
filtered_img.save("./Pokedex/grey.png", "png")

# filtered_img.show()    # this opens the image in the default player

rotated_img = img.rotate(45)
rotated_img.save("./Pokedex/rotated.png", "png")

resized_img = img.resize((100,50))    # but this can ruin the aspect ratio hence we use thumbnail method
resized_img.save("./Pokedex/resized.png", "png")

box = (100,100,400,400)
cropped_img = img.crop(box)
cropped_img.save("./Pokedex/cropped_img.png", "png")

img.thumbnail((100,50))    # it will keep max. 50*50 aspect ratio, it can be like 30*50, but it won't exceed 50 pixels
img.save("./Pokedex/thumbnailed.png", "png")
