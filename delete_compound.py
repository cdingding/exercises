
def no_compound(lst):
    # sorted_list = sorted(lst, key=len)
    # bb = list(reversed(lst)) #have to use list() to get the list
    # cc = sorted_list[::-1]
    temp_list = []
    for index, word in enumerate(lst):
        for later_word in lst[index+1:]: #use index +1, otherwise will compare with itself.
            if later_word in word and word not in temp_list:
                temp_list.append(word)
                print word, later_word
                print temp_list
            print temp_list
            break
    print temp_list
    final_list = [x for x in lst if x not in temp_list]
    return final_list

alist = ['whatsoever', 'so', 'ever', 'person', 'per', 'son']
print no_compound(alist)


