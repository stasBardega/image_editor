from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance

with Image.open("1..jpg") as pic_original:
    pic_original.show()
    print("Розмір:", pic_original.size)
    print("Формат:",pic_original.format)
    print("Тип:", pic_original.mode)
    pic_gray = pic_original.convert("L")
    pic_gray.save("gray.jpg")
    pic_gray.show()
    pic_blured = pic_original.filter(ImageFilter.BLUR)
    pic_blured.save("blured.jpg")
    pic_blured.show()
    pic_up = pic_original.transpose(Image.FLIP_LEFT_RIGHT)
    pic_up.save("up.jpg")
    pic_up.show()

    pic_contrast = ImageEnhance.Contrast(pic_original)
    pic_contrast = pic_contrast.enhance(1.5)
    pic_contrast.save("file.jpg")
    pic_contrast.show()