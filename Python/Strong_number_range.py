'''A Strong Number is defined as a number where the sum of the factorials of its digits equals the original number itself.'''
def find_strong_numbers_in_range(a, b):
    for i in range (a,b+1):
        i1=i
        i2=0
        while i1>0:
            r=i1%10
            i3=1
            for j in range(1,r+1):
                i3=i3*j
            i2=i2+i3
            i1=i1//10
        if i2==i:
            print(i2)
        else:
            pass
x=int(input())
y=int(input())
find_strong_numbers_in_range(x,y)
