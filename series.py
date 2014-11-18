
def slices(numbers,l):
    posibilities=[]
    position=1
    end= 0
    start=0
    if(len(numbers) <l or l<=0):
        raise ValueError("not enough numbers");
    
    
    while((len(numbers)-position+1)>=l):
        end=position-1+l
        start=position-1
        
        posibilities.append(makeList(numbers[start:end])) 
        position+=1

    return posibilities
    
def makeList(numbers):
    listNum=[]
    
    for n in numbers:
        listNum.append(int(n))
    
    return listNum  

    
    
print slices("01234", 0)
    