"""
generic script

text: ["a","b","c","d","e"] output => ["e-5","d-4","c-3","b-2","a-1"]
text: ["a","b","c"] output => ["c-3","b-2","a-1"]
text: ["a","b","c","d"] output => ["4","3","2","1"]
text: ["a","b"] output => ["2","1"]
"""


def fn_hack_8(result):
    #result = ["a","b","c","d","e"]
    long_lista = len(result)
    contador = long_lista
    lista = list() 
    for i in range(long_lista):
        if (long_lista % 2 == 0):
            lista.insert(i,str(contador))
            contador -= 1
        else:
            lista.insert(i,result[contador-1]+'-'+str(contador))
            contador -= 1    
    result = lista         
    return result
