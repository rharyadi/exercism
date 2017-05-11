def is_leap_year(year):
    logic = [0,0,0]
    if year % 4 == 0: logic[0] = 1
    if year % 100 == 0: logic[1] = 1
    if year % 400 == 0: logic[2] = 1
    leap_decider = (logic[0]^logic[1])|logic[2]
    if leap_decider: return True
    else: return False
