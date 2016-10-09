import os
from PIL import Image, ImageEnhance, ImageFilter
import pytesseract

def receipt_to_text(filename):
	path = filename
	img = Image.open(path)
	img = img.convert('RGBA')
	pix = img.load()
	# modify image to maximize the readability of text
	for y in range(img.size[1]):
		for x in range(img.size[0]):
			if pix[x, y][0] < 175 or pix[x, y][1] < 175 or pix[x, y][2] < 175:
				pix[x, y] = (0, 0, 0, 255)
			else:
				pix[x, y] = (255, 255, 255, 255)
	img.save('temp.jpg')
	im = Image.open("temp.jpg")
	im = im.filter(ImageFilter.MedianFilter())
	enhancer = ImageEnhance.Contrast(im)
	im = enhancer.enhance(2)
	im = im.convert('1')
	im.save('temp.jpg')

	text = pytesseract.image_to_string(Image.open('temp.jpg'))
	os.remove('temp.jpg')
	text = ''.join([i for i in text if not i.isdigit()])
	text = text.splitlines()
	return text