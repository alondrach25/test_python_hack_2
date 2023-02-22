"""
generic script

["1",2] => type string & type int
[0] => type int

text: ["a","b","c","d","e"] output => ["1",2,"3",4,"5"]
text: [] output => [0] 
"""


def fn_hack_7(result):
    #result = ["a","b","c","d","e"]
    longitud_cadena = len(result)
    i = 0
    cadena = list()
    while (i<= longitud_cadena):
        if (longitud_cadena == 1):
            cadena.insert(0,longitud_cadena-1)
            longitud_cadena = len(cadena)
            break
        else:   
            cadena[i:i+2] = [str(i+1),i+2]
            i = i+2
    result = cadena[0:longitud_cadena]  
    return result
print(fn_hack_7([0]))