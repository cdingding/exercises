
s = 'abc'
result = []
for x in s:
    for y in s:
        result.append((x,y))
print result

s = '10'
result = []
for x in s:
    for y in s:
        for z in s:
            result.append((x,y,z))
print len(result)
print [''.join(x) for x in result]