import cv2 
import pytesseract
import googlesearch 
from tkinter import *
import threading

path = r"Path To Executable"
pytesseract.pytesseract.tesseract_cmd = path

def web_search():
    root.destroy()
    
    img = cv2.imread(str(ent_input.get()))
    #Image Preproccesing
    cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    scale_percent = 80 
    width = int(img.shape[1] * scale_percent / 200)
    height = int(img.shape[0] * scale_percent / 200)
    dim = (width, height)
    img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

    d = pytesseract.image_to_data(img, output_type=pytesseract.Output.DICT)

    boxes, query = len(d['text']), " ".join(d['text'])
    for i in range(boxes):
        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    print(str(googlesearch.search(query)))
    cv2.imshow('OCR Web-Search', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def search_thread():
    thread = threading.Thread(target=ocr()).start()

root = Tk()
root.title("OCR Web-Search Tool")

ent_input = Entry(root)
ent_input.grid(row=1, column=0)
btn_submit = Button(root, text="Search", command=lambda: search_thread()).grid(row=2, column=0)
root.mainloop()
