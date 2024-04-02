from PIL import Image, ImageFilter

if __name__ == "__main__":
    before = Image.open("bridge.jpg")
    after = before.filter(ImageFilter.BoxBlur(1))
    after.save("out.bmp")
    
