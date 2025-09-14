import qrcode
from pyzbar.pyzbar import decode
from PIL import Image


myqr = qrcode.make("https://www.youtube.com/watch?v=PyDn2gU9DJo")
myqr.save("myqr.png", scale= 8)
myqr1 = qrcode.make("https://www.linkedin.com/in/souradeep-acharyya-8b993a243?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app ")
myqr1.save("myqr1.png", scale=7)
myqr2 = qrcode.make("https://www.linkedin.com/in/abhishek-mallick09?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app ")
myqr2.save("myqr2.png", scale=7)
myqr3 = qrcode.make("https://www.linkedin.com/in/aritra-das-26062a289?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app ")
myqr3.save("myqr3.png", scale =7)
s=input("Enter an URL :- ")
myqrExample = qrcode.make(s)
myqrExample.save("myqrExample.png", scale= 7)
b = decode(Image.open("myqr.png"))
print(b[0].data.decode("ascii"))
