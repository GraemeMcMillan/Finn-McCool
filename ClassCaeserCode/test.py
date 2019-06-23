


def caesar_code(message, key):
    message = str(message)
    key = int(key)
    alphabet1 = ''.join(chr(x) for x in range(32, 127))
    alphabet2 = alphabet1[key:]+alphabet1[:key]
    coded_message = ''
    for i in range(len(message)):
        x = alphabet1.find(message[i])
        coded_message += (alphabet2[x])
    print(coded_message)

x=26
y = 'Happy Programming with Python3'
caesar_code(y,x)
