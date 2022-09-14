"""Description"""
def description():
    '''wow'''
    text = input()
    line_1 = float(input())
    line_2 = float(input())
    line_3 = float(input())
    newlist = []
    if line_1 <= line_2 and line_1 <= line_3:
        newlist.append(line_1)
        if line_2 <= line_3:
            newlist.append(line_2)
            newlist.append(line_3)
        else:
            newlist.append(line_3)
            newlist.append(line_2)
    if line_2 <= line_1 and line_2 <= line_3:
        newlist.append(line_2)
        if line_1 <= line_3:
            newlist.append(line_1)
            newlist.append(line_3)
        else:
            newlist.append(line_3)
            newlist.append(line_1)
    if line_3 <= line_2 and line_3 <= line_1:
        newlist.append(line_3)
        if line_2 <= line_1:
            newlist.append(line_2)
            newlist.append(line_1)
        else:
            newlist.append(line_1)
            newlist.append(line_2)
    if text == 'Ascend':
        print('%.2f, %.2f, %.2f' %(newlist[0], newlist[1], newlist[2]))
    elif text == 'Descend':
        newlist.reverse()
        print('%.2f, %.2f, %.2f' %(newlist[0], newlist[1], newlist[2]))
description()
