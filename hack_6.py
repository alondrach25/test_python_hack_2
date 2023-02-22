"""
generic script

["1","-"] => type string
["0"] => type string

text: ["a","b","c","d","e"] output => ["1","-","3","-","5"]
text: [] output => ["0"] 
"""


def fn_hack_6(result):
    #result = []
    longitud_cadena = len(result)
    i = 0
    cadena = list()
    while (i<= longitud_cadena):
        if (longitud_cadena == 0):
            cadena.insert(0,str(longitud_cadena))
            longitud_cadena = len(cadena)
            break
        else:   
            cadena[i:i+2] = [str(i+1),"-"]
            i = i+2
    result = cadena[0:longitud_cadena]    
    return result
