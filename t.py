import base64
import sys

image_base64 = "../../Pictures/lastsnap.jpg"
sys.stdout = open("img_64.txt","w")

f = open(image_base64, "rwb")
str = base64.b64encode(f.read())
print(str)
sys.stdout.close()

