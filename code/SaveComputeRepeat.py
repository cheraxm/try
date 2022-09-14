"""SaveComputeRepeat"""
def main():
    """days, hours, minutes, seconds, milliseconds"""
    start = 492137954293754252786
    millisecond = start
    seconds = millisecond//1000
    millisecond = millisecond%1000
    minute = seconds//60
    seconds = seconds%60
    hours = minute//60
    minute = minute%60
    days = hours//24
    hours = hours%24
    print(days, hours, minute, seconds, millisecond)
main()
