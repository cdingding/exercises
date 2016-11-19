class ReverseString(object):
    def __init__(self,st):
        self.st = st
    def reverse(self):
        st = list(self.st)
        l = len(st)
        start = 0
        while start < l:
            st[start], st[l-1] = st[l-1], st[start]
            start += 1
            l -= 1
        return ''.join(st)

class ReverseString1(object):
    def __init__(self,st):
        self.st = st
    def reverse(self):
        st =list(self.st)
        l = len(st)
        start = 0
        while start < l:
            st[start], st[l-1] = st[l-1], st[start]
            start += 1
            l -= 1
        return st

class ReverseString2(object):
    def reverse(self,st):
        st =list(st)
        l = len(st)
        start = 0
        while start < l:
            st[start], st[l-1] = st[l-1], st[start]
            start += 1
            l -= 1
        return st



def reverse_string(string):
  result = ''
  for index, item in enumerate(string):
    result = result + string[-(index+1)]
  return result

def reverse_string1(string):
  str_len = len(string)
  i = str_len
  result = ''
  while i > 0:
    result = result + string[i-1]
    i -=1
  return result

def reverse_simple(string):
  return string[::-1]

def reverse_str(string):
    rev_list=[]
    new_list=list(string)
    while new_list:
        rev_list += new_list[-1]
        new_list.pop()
    return ''.join(rev_list)

def reverse1(string):
    lst = list(string)
    i = len(lst)/2
    print i, len(lst)
    while i >= 0:
        lst[i], lst[-i-1] = lst[-i-1], lst[i]
        i -= 1
    return ''.join(lst)

print ReverseString('Ding').reverse()
# print reverse_string("Madam, I'm Adam")
# print reverse_simple("Madam, I'm Adam")
# print reverse_str('ding')
# print reverse1('ding')
# print reverse1("Madam, I'm Adam")
