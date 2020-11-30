import pyqrcode

QRstr="https://www.linkedin.com/in/shamim-imtiyaz-11a3406b/"
url=pyqrcode.create(QRstr)
url.png('imthi.png',scale=8)