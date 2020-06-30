def equal(x,y):
    count = 0
    if(y>x):
        while(y!=x):
            if(y % 2==0):
                if(x*2 > y):
                    x-=1
                else:
                    x*=2
            else:
                a=y+1
                if (x*2 > a): x-=1
                else: x*=2
            count+=1
        print("số bước cần thực hiện là " +str(count) + " bước")
    else:
        print("Y phải lớn hơn X")

equal(6,7) # 4 bước
equal(4,5) # 3 bước
equal(1,3) # 3 bước
equal(15,16) # 8 bước
equal(3,8) # 4 bước
