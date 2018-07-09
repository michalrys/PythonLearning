# 2018-07-09, M. Ryś
# InfoShare: day 13.
# uzycie pill'a
# ------------------------------------------------------------------------------

from PIL import Image

im = Image.open('e:\PYTHON\SZKOLENIE\MATERIALY\DAY_13\Foto\sesja.jpg')

print(im.size)
print(im.__dict__)

# zmiana rozmiaru
im.thumbnail((120, 120))
im.save('e:\PYTHON\SZKOLENIE\MATERIALY\DAY_13\Foto\sesja_test01.jpg', 'JPEG')

im.rotate(45).show()
