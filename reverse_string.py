def reverse_string(string):
  result = ''
  for index, item in enumerate(string):
    result = result + string[-(index+1)]
  return result
print reverse_string('Ding')

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
print reverse_string("Madam, I'm Adam")
print reverse_simple("Madam, I'm Adam")
print reverse_str('ding')
print reverse1('ding')
print reverse1("Madam, I'm Adam")
