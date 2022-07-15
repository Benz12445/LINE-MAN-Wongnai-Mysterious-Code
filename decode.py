import base64

if __name__ == '__main__':
    encodeTxt = "aWFuZ25vVzpOQU06RU5JTDp0YTpzdTpuaW9K"
    decode = base64.b64decode(encodeTxt)
    whatIsIt = "" 

    for i in range(len(decode) - 1, -1, -1):
       whatIsIt += chr(decode[i])

    print(whatIsIt)
