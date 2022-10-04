import os
import random
from pathlib import Path
from PIL import Image
from django.shortcuts import render

BASE_DIR = Path(__file__).resolve().parent.parent

def carousel(request):
    k = 0
    imgfiles = {}
    imgpath = os.path.join(BASE_DIR, 'static', 'images')
    obj = os.listdir(imgpath)
    for i in obj:
        if not os.path.isdir(i):
            img = Image.open(os.path.join(imgpath, i))
            if img.format:
                imgfiles[k] = i
                k+=1
    firstimg = imgfiles[random.randint(0,len(imgfiles))]

    return render(request, 'index.html', {'images':imgfiles, 'firstimg':firstimg})