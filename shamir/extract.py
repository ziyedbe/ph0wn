from PIL import Image
import pytesseract


for i in range(1,8):
	im = Image.open('cropped/'+str(i)+'.jpg').convert('L')
	print(pytesseract.image_to_string(im, lang='eng', config='--psm 13 --oem 2 -c tessedit_char_whitelist=0123456789,()'))
