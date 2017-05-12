from itertools import groupby

def decode(msg):
    # 'X10YZ3X' will be grouped as ['X','10','YZ','3','X']
    msg = [''.join(c) for _,c in groupby(msg, key=str.isdigit)]
    decoded = []
    for i,item in enumerate(msg):
        if item.isdigit():
            # [...,'3',BN',..] will be
            # [...,'BB','BN',...]
            decoded.append((int(item)-1)*msg[i+1][0])
        else:
            decoded.append(item)
    return ''.join(decoded)
        

def encode(msg):
    encoded = []
    for k,g in groupby(msg):
        length = len(list(g))
        if length > 1:
            encoded.append(str(length))
        encoded.append(k)
    return ''.join(encoded)

