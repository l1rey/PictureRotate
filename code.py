from PIL import Image


def main():
    print(im.mode)


im = Image.open("picture.jpg")


im_rotate = im.transpose(Image.Transpose.ROTATE_90)
im_rotate.save('picture90.jpg')
im.close()


if __name__ == '__main__':
    main()