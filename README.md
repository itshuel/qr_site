<b>QRКодер</b>

Время проверить твою реакцию! РасQRрь флаг!

Зайдя на страницу, мы видим QR-код. Если внимательно присмотреться, можно заметить, что он обновляется достаточно быстро. Значит нам нужно скачать его и раскодировать. Воспользуемся библиотеками Python для этого:

```python
import cv2
import requests
import urllib.request
def decode(img):
    img = cv2.imread(img)
    detector = cv2.QRCodeDetector()
    data, bbox, straight_qrcode = detector.detectAndDecode(img)
    if bbox is not None:
        print(f"QRCode data:\n{data}")
        n_lines = len(bbox)
    return data    

####### Загрузка изображения
img = "https://web7.kvvuctf.ru/static/imgs/image.png"
resource = urllib.request.urlopen(img)
out = open("image.png", 'wb')
out.write(resource.read())
out.close()
######## Декодирование и отправка изображения POST запросом
c = decode("image.png")
url = "https://web7.kvvuctf.ru/qr"
payload = {"flag":c}
r = requests.post(url=url,data=payload)
print(r.text)
```

Флаг: <b>kvvu{Sn4p_H1m_f4$sTeR}</b>
