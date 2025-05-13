from g1 import Atbash, Cesar, Cod_URL, Rail_Fence, ROT13, Vigenere
from g2 import base16, base32, base64, base85
from g3 import XOR

if __name__ == "__main__":
    texto_ejemplo = "Este es un texto secreto"
    
    texto_codificado = base16.codificar_base16(texto_ejemplo)

    print(f"Texto codificado con Base16: {texto_codificado}")
    texto_decodificar = texto_codificado

    texto_decodificado = base16.decodificar_base16(texto_decodificar)
    print(f"Texto decodificado con Base16: {texto_decodificado}")
