'''weight'''
def sta():
    '''weight station'''
    avg = float(input())
    txt = 'yes'
    wheel = []
    for _ in range(3):
        wheel.append(float(input()))
    wheel.append(4*avg - (wheel[0] + wheel[1] + wheel[2]))
    for i in wheel:
        if avg*4 > 15000:
            print('Overweight')
            txt = 'no'
            break
        elif  i < 0.5*avg or i > 1.5*avg:
            print('Unbalance')
            txt = 'no'
            break
    if txt == 'yes':
        print('Pass %.2f' %(4*avg - (wheel[0] + wheel[1] + wheel[2])))
sta()
