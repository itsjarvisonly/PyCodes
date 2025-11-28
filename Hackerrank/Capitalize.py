s = "hello   world"
names = s.split(" ")
s = []
for i in names:
    if len(i)>0: #we did this to check if the i(word) is a whitespace
        word = list(i)
        word = list(word[0].capitalize()) + word[1:]
    else: #if it is a whitespace we would just consider the same as word 
        word = i
    s.append("".join(word))
s = " ".join(s)
print(s)
    
        
    
