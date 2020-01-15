#Date: 1/15/2
import string
def ispangram(str1, alphabet=string.ascii_lowercase):
    
#one_liner    
    return len(alphabet) == len(''.join(set(str1.lower().replace(' ',''))))
    
#sorted_method_tested    
#    print(''.join(sorted(set(str1.lower().replace(' ','')))))
    
#another_onliner  
#    return set(alphabet) <= set(str1.lower())
    
#convenient method to understand
#     cmplist=[]
#     for i in str1.lower():
#         if i in alphabet:
#             cmplist.append(i)
#     return len(alphabet) == len(''.join(set(cmplist)))

print(ispangram("The quick brown fox jumps over the lazy dog"))
