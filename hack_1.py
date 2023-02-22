"""
generic script

text: "fooziman" output => "fOozIman" 
text: "qux" output => "qUx" 
text: "eq" output => "eq" 
"""


def fn_hack_1(result):
    #result = "fooziman"
    longitud_string = len(result)
    contador1 = 1
    contador2 = 0
    while (contador1 < longitud_string):
        if longitud_string > 2:
            result = result.replace(result[contador1], result[contador1].upper(),contador1)
            contador1=contador1+contador2+3
            contador2+=1
        else:
            break     
    return result
