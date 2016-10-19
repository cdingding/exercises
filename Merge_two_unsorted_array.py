a = ['are','you','there']
b = " how are you".split()
c = list(set(b+a))
print c
rt = []
for i in xrange(len(c)):
    indexes_a = [x for x,y in enumerate(c) if y in a]
    indexes_b = [m for m,n in enumerate(c) if n in b]
print indexes_a
print indexes_b
print '----'
for i in range(len(c)-1):
    if indexes_a[i] < indexes_b[i]:
        rt.append(a[i])
    elif indexes_b[i] < indexes_a[i]:
        rt.append(b[i])
    elif b[i] not in rt:
        rt.append(b[i])
# print rt

# aa = [0,1,2,3,4]
# for i in aa:
#     if i <= 2:
#         print 'less', i
#         continue
#     if i < 4:
#         print 'less less', 3
#         continue
#     print 'A'

def merge(a,b):
    rta = []
    rtb = []
    final = []
    for i in range(len(a)-1):
        rta.append(a[0:2])
        a.pop(0)
    for i in range(len(b)-1):
        rtb.append(b[0:2])
        b.pop(0)
    for i, pair in enumerate(rta):
        if pair not in rtb:
            final += pair
        else: final += rtb[i]
    return final

a = ['are','you','there']
b = "how are you".split()
print merge(a,b)

