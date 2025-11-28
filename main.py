import cv2
import numpy as np
from pyzbar.pyzbar import decode

# scanning QR code from the photo
qr = cv2.imread("qr1.png")
grayqr = cv2.cvtColor(qr,cv2.COLOR_BGR2GRAY)
for code in decode(qr):
    print(code.data.decode("utf-8"))
    corners = code.polygon
    corners = [(point.x, point.y) for point in corners]
    for i in range (len(corners)):
        cv2.line(qr, corners[i], corners[(i+1)%len(corners)], (245,201,242), 12)
cv2.imshow("QR", qr)
cv2.waitKey(0)
cv2.destroyAllWindows()

