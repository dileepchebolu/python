#Write your code here
class Calculator():
    def __init__(self):
        pass
    def power(self,n,p):
        if p < 0 or n < 0:
            raise ValueError("n and p should be non-negative")
        elif p == 0:
            return 1
        else:
            return n ** p 

myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e) 