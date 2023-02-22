"""
text: [{"a":"b"},{"c","d"},{"e":"f"}] output => [{"1":"2"},{"3","4"},{"5":"6"}]
"""


def fn_hack_10(result):
    #result = [{"a":"b"},{"c","d"},{"e":"f"}]
    long_result = len(result)
    lista = list()
    dicc = dict()
    conjunto = set()
    contador = 1
    for i in range(long_result):
        if (type(result[i]) is dict):
            dicc[str(contador)] = str(contador+1)
            lista.insert(i,dicc)
            dicc = dict()
        else:
            conjunto = {str(contador), str(contador+1)}
            lista.insert(i,conjunto) 
            conjunto = set()
        contador +=2
    result = lista    
    return result
