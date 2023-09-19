from PIL import Image, ImageFilter

img= Image.open('./astro.jpg')
# print(img.size)
# print(img.mode)
# filtered_img= img.convert('L')
# rotated= filtered_img.rotate(90)
# rotated.save("rotate.png",'png')
img.thumbnail((400,200))
img.save('thumbnail.jpg')