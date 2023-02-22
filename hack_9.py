"""
text: {"foo":"fookziman","bar":"barziman"} output => {"Foo":"Fooziman"}
"""


def fn_hack_9(result):
    #result = {"foo":"fookziman","bar":"barziman"}
    result.popitem()
    result = {k.capitalize(): v.capitalize().replace("k","") for k, v in result.items()}
    return result
