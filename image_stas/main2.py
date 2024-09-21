from PIL import Image
from PIL import ImageFilter


class ImageEditor():

    #конструктор
    def __init__(self, filename):
        self.filename = filename   #ім'я файлу 
        self.original = None       #оригінал зображення
        self.changed = []          #список для збереження змінених зображень

    #Відкриває та відображає зображення
    def open(self):
        try:
            self.original = Image.open(self.filename)
        except:
            print("Файл не знайдено!")

        self.original.show()


    
        #дзеркальне відображення зображення
    def do_left(self):

        rotate = self.original.transpose(Image.FLIP_LEFT_RIGHT)
        self.changed.append(rotate)

        rotate.show()

    def do_cropped(self):

        box = (110, 100, 120, 45)
        cropped = self.original.crop(box)
        self.changed.append(cropped)

        cropped.show()



MyImage = ImageEditor('1..jpg')

MyImage.open()
MyImage.do_left()
MyImage.do_cropped()