#Find smallest substring containing all chars of target.
# print(min_window("ADOBECODE", [’A’,’B’,’C’])) —> Output ADOBEC
# print(min_window("ADOBECODEBANC", [’A’,’B’,’C’])) —> Output BANC

def min_window(s1,target):
    result = []
    res = ''
    count=0
    for c in s1:
        if c in target:
            count+=1
        if count>0:res+=c
        if count==3:
            if len(result)>0:
                for i in result:
                    if len(i)>len(res):
                        result.pop()
                        result.append(res)
            else:
                result.append(res)
            res=''
            count=0
    
    print(result)
min_window("ADOBECODE", ['A','B','C'])
min_window("ADOBECODEBANC", ['A','B','C'])
            