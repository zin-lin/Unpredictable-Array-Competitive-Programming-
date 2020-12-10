from Statics.definations import replacer,addAll

testCase_Turns = int(input(":"))
for xox in range(testCase_Turns):
    var=[]
    n, q = list(map( int ,input(":").split(" ")))#Now we've got the number of items and the number of updates
    array = list(map(int, input(":").split(" ")))#Now we've got the required array
    #[region Checking the statements
    if len(array) != n: raise ValueError("Values of the numbers are unfortunately not the same")#endregion]
    for s in range(q):
        x,y = list(map(int, input(":").split(" ")))
        replacer(array,x,y)
        var.append(addAll(array))
    print(f"Case {xox+1}:")
    for i in var:print(i)
