list2Perm = [1, 2, 3]
listPerm = [[a, b, c]
            for a in list2Perm
            for b in list2Perm
            for c in list2Perm
            if ( a != b and b != c and a != c )
            ]
print listPerm

print '-----------'

def perm2(list2Perm):
    for a in list2Perm:
        for b in list2Perm:
            for c in list2Perm:
                if ( a != b and b != c and a != c ):
                    yield [a, b, c]


def perm3(list2Perm):
    result = []
    for a in list2Perm:
        for b in list2Perm:
            for c in list2Perm:
                if ( a != b and b != c and a != c ):
                    result.extend([[a, b, c]])
    return result



def perm4(list2Perm):
    result = []
    for a in list2Perm:
        for b in list2Perm:
            for c in list2Perm:
                if ( a != b and b != c and a != c ):
                    result.append([a, b, c ])
    return result

print perm4(list2Perm)
for perm in perm3(list2Perm):
    print perm