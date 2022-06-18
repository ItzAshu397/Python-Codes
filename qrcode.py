import pyqrcode
import png
from pyqrcode import QRCode

link = "https://mathrockz.netlify.app"

url = pyqrcode.create(link)
url.png("qrcode.png", scale=8)
print('Done')