# key concept: can compare two dictionary(hashmap)

def valid_anagram(s,t):
    dict1={}
    dict2 ={}
    
    for i in s:
        if i in dict1:
            dict1[i]+=1
            
        else:
            dict1[i]=1
            
    for i in t:
        if i in dict2:
            dict2[i]+=1
            
        else:
            dict2[i]=1
            
    return dict1 == dict2

print(valid_anagram("anagram", "nagaram"))