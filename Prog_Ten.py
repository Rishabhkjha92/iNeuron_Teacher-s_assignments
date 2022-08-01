# 10. WAF which will be able to read an image file and show it to you

from PIL import Image
import click

click.clear()

#in case Image.open("") doesn't work use Image.open(r"")
var = Image.open(r"E:\Fun pics\2022\17-04-22\IMG_20220417_183706.jpg")
var.show()