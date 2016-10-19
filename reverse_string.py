def reverse_string(string):
  str_len = len(string)
  result = ''
  for index, item in enumerate(string):
    result = result + string[-(index+1)]
  return result
print reverse_string('Ding')

def reverse_string1(string):
  str_len = len(string)
  i = str_len
  result = ''
  while i>0:
    result = result + string[i-1]
    i -=1
  return result
print reverse_string1("Madam, I'm Adam")