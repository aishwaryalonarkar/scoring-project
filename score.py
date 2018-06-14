k=[1,1,5,5,5]
val=0
n1=k.count(1)
n5=k.count(5)

if n1>2:
    val+=1000
    n1=n1-3
         
else:
    for i in k:
        if k.count(i)>2:
            val+=100*i
            if i==5:
                    n5=n5-3
            break

if n5>0:
    for i in range (n5):
        val+=50

if n1>0:
    for i in range (0,n1):
        val+=100
        
print val


            
        

        
                


        
        
           
    
