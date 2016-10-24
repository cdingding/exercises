
items = range(-2, 3)
print items

items_map = map(lambda x: x+1, items)
print items_map

item_filter = filter(lambda x: x !=0, items)
print item_filter

item_reduce = reduce(lambda x, y: x * y, item_filter)
print item_reduce

# Use map to get abbreviation

phrase = 'I am Changsong Ding'
letters = map(lambda x: x[0].upper(), phrase.split())
print 'letters:', letters

red = reduce(lambda x, y: x + y, letters)
print 'red: ',red

# or use ''.join()
abbr = ''.join(letters)
print abbr
print abbr[::-1]
letters.reverse() # inplace change, does not return, or return None
print letters
letters.reverse()
print ''.join([x[0].upper() for x in phrase.split()]) # list comprehension


