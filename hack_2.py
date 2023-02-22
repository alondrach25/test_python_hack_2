"""
generic script

text: "fooziman" output => "fzmn" 
text: "barziman" output => "brzmn" 
text: "qux" output => "qx" 
"""
from collections import OrderedDict

def fn_hack_2(result):
    #result = "qux"
    result = list(result)
    lista_vocales = list("aeiouAEIOU")
    for i in result:
        if i in lista_vocales:
            indice = result.index(i)
            result[indice] = '*'
    result = list(OrderedDict.fromkeys(result))
    result.remove('*')
    result = "".join(result)
    return result
