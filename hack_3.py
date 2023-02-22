"""
generic script

a = @
e = 3
i = ¡
o = 0
u = v

text: "fooziman" output => "F00z¡m@N" 
text: "barziman" output => "B@rz¡m@N" 
text: "3q" output => "3Q" 
text: "qu" output => "Qv" 
text: "qux" output => "QvX" 
"""


def fn_hack_3(result):
    #result = "barziman"
    caracteres = {'a':'@', 'e':'3', 'i':'¡', 'o':'0', 'u':'v'}
    longitud_cadena = len(result)
    
    if result[0] in "1234567890":
        result = result.upper()
    else:
        result = result.capitalize() 
    
    for letra in result:
        if letra in caracteres:
            result = result.replace(letra,caracteres.get(letra))
            if longitud_cadena >= 3:
                result = result.replace(result[longitud_cadena-1], result[longitud_cadena-1].upper())
    return result
