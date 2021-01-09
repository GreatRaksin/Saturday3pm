from PIL import Image, ImageFilter


sample = Image.open('img.jpg')
# sample.show() - показать изображение
resized_image = sample.resize((1280, 720))  # изменить размер изображения (ширина, высота)
resized_image.save('resized.jpg')  # сохранить изображение ('имя.расширение')

''' Создать 360 копий изображения, повернуть их на один градус (каждую)
for angle in range(1, 361):
    image_name = 'rotated_' + str(angle) + '.jpg'
    new_image = resized_image.rotate(angle)
    new_image.save('./rotation/' + image_name)
'''

edges = resized_image.filter(ImageFilter.FIND_EDGES)
edges.show()