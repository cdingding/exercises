# Method 1
def switch(dt):
    d = {}
    for key, item in dt.iteritems():
        d[item] = key
    return d

if __name__== "__main__":
    dt = {'ding': 1, "changsong":2}
    print switch(dt)

    #Method 2:
    my_dict2 = dict((y,x) for x,y in dt.iteritems())
    print my_dict2