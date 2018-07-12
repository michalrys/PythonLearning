# 2018-07-11, M. Ryś
# InfoShare day 13 - środa
# github i git, argumenty programów, modyfikowanie zdjęć, krótkie podsumowanie
# obrazki
# ------------------------------------------------------------------------------
import sys

print(sys.argv)

from PIL import Image

file = sys.argv[1]
# 'Foto/sesja.jpg'

foto = Image.open(file)

# foto.show()
print(f'{foto.width} x {foto.height}')
print(foto.getpixel((100, 100)))

foto.effect_spread(10).show()



