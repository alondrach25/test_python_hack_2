"""
generic script

text: "fooziman" output => "oozima" 
text: "barziman" output => "arzima" 
text: "qux" output => "qux" 
"""


def fn_hack_4(result):
    #result = "qux"
    longitud_cadena = len(result)
    if longitud_cadena > 3:
        result = result[1:longitud_cadena-1]

    return result
