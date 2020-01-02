input_s = ['3[abc]4[ab]c', '2[3[a]b]c']


# if '[' not in comp[l+1:r]:
#         return int(comp[0:l]) * comp[l+1:r]
a = '10[a]b'
b = '2[2[3[a]b]c]'
c = '3[abc]4[ab]c'

def findnth(haystack, needle, n):
    parts= haystack.split(needle, n+1)
    if len(parts)<=n+1:
        return -1
    return len(haystack)-len(parts[-1])-len(needle)

def decomp(comp):
    
    l = comp.find('[')
    r = comp.find(']')
    
    mul =int(comp[0:l])
    # Find how left brackets many are in between
    extra_l = comp[l+1:r].count('[')

    if extra_l == 0:
        
        return mul * comp[l+1:r] + comp[r+1:]
    else:
        # Find the nth right bracket
        nth_idx = findnth(comp, ']', extra_l)
        subset = comp[l+1: nth_idx]
        new_set = comp[:l+1] + decomp(subset) + comp[nth_idx:]

        return decomp(new_set)


def splitter(comp):
    comp_list = []
    
    alt = 0

    last_cut = 0
    new_alt = 0
    for idx, char in enumerate(comp):
        
        if char == '[':
            alt += 1
            risen = True
        if char == ']':
            alt -= 1

        if alt == 0 and idx != 0 and risen:
            comp_list.append(comp[last_cut:idx+1])
            last_cut = idx+1
            risen = False
    return comp_list
            
            
    
            
for comp in splitter(c):
    print(decomp(comp), end='')

        

        
        
    