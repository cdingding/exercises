def hellotest(name, loud=False):
    if loud:
        print "Hello, %s!" %name.upper()
    else:
        print 'Hello Hello, %s!' %name

if __name__=='__main__':
    hellotest('ding', loud = True)