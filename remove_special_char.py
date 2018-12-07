# -*- coding: utf-8 -*-
import re
from unicodedata import normalize

try:
    input = raw_input
except NameError:
    pass

word = input('Ingrese palabra con caracteres especiales a normalizar: ')


# -> Remove accents and other special characters (excluding the ~ in the case of "Ñ" or 'ñ')
word = re.sub(
        r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1", 
        normalize('NFD', word), 0, re.I
    )

# -> NFC
word = normalize('NFC', word)

print("\n\n\nLa palabra sin acentos ni caracteres especiales es:\n\n\n" + word, "\n\n\n")