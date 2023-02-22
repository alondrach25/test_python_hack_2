"""
generic script

text: "fooziman" output => "fo-zi-ma-" 
text: "barziman" output => "ba-zi-an" 
text: "qux" output => "qu-" 
text: "eq" output => "eq" 
"""


def fn_hack_5(result):
    #result = "barziman"
    if result.find("oo")!= 1:
        longitud_cadena = len(result)
    else:
        long = len(result)
        result = result[0:int(long/2)+1]+"i"+result[int(long/2)+1:]
        longitud_cadena = len(result)
    
    cadena = result[0:2]    
    i = 3
    while (i<= longitud_cadena):
        if longitud_cadena > 2:
            cadena = cadena +'-'+ result[i:i+2]
            i = i+3
    result = cadena    
    return result
