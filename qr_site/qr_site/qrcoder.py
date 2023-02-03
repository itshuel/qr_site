import os
import qrcode
import random 
import string 
import time
from settings import STATICFILES_DIRS

while (True):
	def random_string_generator(str_size, allowed_chars): 
		return ''.join(random.choice(allowed_chars) for x in range(str_size)) 
	chars = string.ascii_letters + string.punctuation 
	size = 12 
	data = "kvvu{"+random_string_generator(size, chars)+"}"
	filename = "site.png"
	img = qrcode.make(data)
	img.save(os.path.join(STATICFILES_DIRS[0], 'imgs/image.png'))
	time.sleep(3)