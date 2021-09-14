from PIL.ImageFont import ImageFont
from barcode import EAN13
from barcode.writer import ImageWriter


''' Criação de código de barra de forma não automatizada e tratada para ser salva no formato .png (por padrão salva em .svg)
cod = EAN13("123123123123", writer=ImageWriter())
cod.save("cod_bar")
'''
# Criação de código de barra de forma automatizada e tratada para ser salva no formato .png (por padrão salva em .svg)
code_product = {
    "milk": "551746511111",
    "rice": "661723511111",
    "noodle": "773745511111"
}

for product in code_product:
    code = code_product[product]
    code_bar = EAN13(code, writer=ImageWriter())
    code_bar.save(f"code_bar_{product}")
