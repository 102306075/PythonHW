#九九乘法
def multiple(x,y):
  
  for i in range(1,10):
    for j in range(x,y):
        result=str(j)+' x '+str(i)+" = "+str(i*j)
        #空格判斷
        if len(str(i*j))==1:
            result=result+"   "
        else:
            result=result+"  "    
        #end : 不換行
        print(result,end="")
    #換行
    print('')


#金字塔
def pry(k):
    i=0
    str(i)
    while (i<k):
        print (" "*(k-i)+"*"*(i*2+1))
        i=i+1
        

        