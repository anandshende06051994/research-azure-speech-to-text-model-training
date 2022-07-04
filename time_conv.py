# recTime = "00:02:09.020"

def convert_time_to_ms(recTime):
    h = int(recTime[0:2])
    m = int(recTime[3:5])
    s = int(recTime[6:8])
    ms = int(recTime[9:])

    # print(h)
    # print(m)
    # print(s)
    # print(ms)

    time_in_ms = ms + (s * 1000) + (m * 60 * 1000) + (h * 60 * 60 * 1000)
    # print(time_in_ms)

    return time_in_ms
