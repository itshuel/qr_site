from django.shortcuts import render
from django.contrib.staticfiles import finders
import cv2
import os
import qrcode
import qrcode.image.svg
from .settings import STATICFILES_DIRS

def decode():
    filename = os.path.join(STATICFILES_DIRS[0], 'image.svg')
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
    if request.POST and request.POST.get('flag') == decode():
        pass
    return render(request, 'qrpage.html')