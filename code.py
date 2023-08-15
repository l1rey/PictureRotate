from PIL import Image


def main():
    print(im.format, im.size, im.mode)


im = Image.open("picture.jpg")

im_rotate = im.rotate(90)
im_rotate.save('picture90.jpg')
im.close()


if __name__ == '__main__':
    main()