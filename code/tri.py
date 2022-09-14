"""teiangle1"""
def tri():
    """thx"""
    num1 = float(input())
    num2 = float(input())
    num3 = float(input())
    if num1 + num2 == num3 or num1 + num3 == num2 or num2 + num3 == num1:
        print('No') 
    else:
        print('Yes')
tri()
