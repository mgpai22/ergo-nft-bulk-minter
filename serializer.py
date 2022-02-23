import base64


# program to serialize register entries

def decoder(string):  # my attempt at decoded. This is not used
    if string[:2] == '0e':
        string = string[2:]
    bytes_object = bytes.fromhex(string)
    ascii_string = bytes_object.decode("ASCII")
    return ascii_string


def encoder(string):  # encodes to bytes
    str = string.encode("UTF-8")
    return base64.b16encode(str).decode('utf-8')


def encodeToVLQ(n: int):  # encodes int to VLQ
    v = vlq(n)
    r = '0e' + ''.join(['{0:02x}'.format(i) for i in v])
    return r


def vlq(i: int):  # encodes int to VLQ
    ret = []
    while i != 0:
        b = i & 0x7F
        i >>= 7
        if i > 0:
            b |= 0x80
        ret.append(b)
    return ret


def hashSerializer(data):  # specifically for serializing sha256
    return '0e20' + str(data)


def serializer(data): # takes data and encodes length to VLQ and concatenates it with the bytes of the data
    return encodeToVLQ(len(data)) + encoder(data)
