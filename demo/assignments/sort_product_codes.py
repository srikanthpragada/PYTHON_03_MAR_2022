codes = ['AB3453', 'DE23', 'CE90', 'XY1111', 'FH909']


def getcode(s):
    return int(s[2:])


for c in sorted(codes, key=lambda v: int(v[2:])):
    print(c)
