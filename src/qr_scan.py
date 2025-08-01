import cv2
import matplotlib.pylab as plt
import pyzbar.pyzbar as pyzbar
import webbrowser
# img = cv2.imread('../img/frame.png')
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cap = cv2.VideoCapture(0)
visited_urls = set() 
while (cap.isOpened()):
    ret, img = cap.read()
    if not ret:
        continue

    # img = cv2.imread('../img/frame.png')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    decoded = pyzbar.decode(gray)
    for d in decoded:
        x, y, w, h = d.rect

        barcode_data = d.data.decode('utf-8')
        barcode_type = d.type

        # print(d.data.decode('utf-8'))
        # barcode_data = d.data.decode('utf-8')
        # print(d.type)
        # barcode_type = d.type
        
        
        text = '%s (%s)' % (barcode_data, barcode_type)

        #cv2.rectangle(img, (d.rect[0], d.rect[1]), (d.rect[0] + d.rect[2], d.rect[1] + d.rect[3]), (0,255,0), 20)
        cv2.rectangle(img, (x,y), (x + w, y + h), (0, 255, 0), 2)
        #cv2.putText(img, text, (d.rect[0], d.rect[1] -50), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 2, cv2.LINE_AA)
        cv2.putText(img, text, (x,y), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 2, cv2.LINE_AA) 
        if barcode_data.startswith("http://") or barcode_data.startswith("https://"):
            if barcode_data not in visited_urls:
                webbrowser.open(barcode_data)
                visited_urls.add(barcode_data)
    
    
    cv2.imshow('camera', img)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cap.release()
cv2.waitKey(0)
cv2.destroyAllWindows()

# plt.imshow(img)
#plt.imshow(gray, cmap='gray')
#plt.show()

# 디코딩
# decoded = pyzbar.decode(gray)
# print(decoded)

# for d in decoded:
#     print(d.data.decode('utf-8'))
#     barcode_data = d.data.decode('utf-8')
#     print(d.type)
#     barcode_type = d.type

#     text = '%s (%s)' % (barcode_data, barcode_type)

#     cv2.rectangle(img, (d.rect[0], d.rect[1]), (d.rect[0] + d.rect[2], d.rect[1] + d.rect[3]), (0,255,0), 20)
#     cv2.putText(img, text, (d.rect[0], d.rect[1] -50), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 2, cv2.LINE_AA)

# plt.imshow(img)
# plt.show()