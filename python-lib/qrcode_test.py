# https://note.nkmk.me/python-pillow-qrcode/
# pip install qrcode, pillow
import qrcode
img = qrcode.make("test text")

print(type(img))
print(img.size)

img.save("/mnt/c/Users/user/Downloads/qrcode_test.png")
