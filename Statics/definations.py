def replacer(List,x,y):
    for i in List:
        if i==x:
            List[List.index(i)]=y
            
def addAll(List):
    var = 0
    for i in range(len(List)-1):
        var += abs( List[i]-List[i+1])
    return var
