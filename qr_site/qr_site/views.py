from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.staticfiles import finders
import cv2
import os
import qrcode
import qrcode.image.svg
from .settings import STATICFILES_DIRS

def decode():
	# img.save(os.path.join(STATICFILES_DIRS[0], 'imgs/image.png'))
    filename = os.path.join(STATICFILES_DIRS[0], 'imgs/image.png')
    image = cv2.imread(filename)
    detector = cv2.QRCodeDetector()
    data, vertices_array, binary_qrcode = detector.detectAndDecode(image)
    if vertices_array is not None:
        return data
    else:
        return "There was some error"

def indexpage(request):
    return render(request, 'index.html')

def qrpage(request):
    flag = 'kvvu{Sn4p_H1m_f4$sTeR}'
    if request.POST and request.POST.get('flag') == decode():
        return render(request, 'flag.html', {'flag': flag})
    return render(request, 'qrpage.html')
