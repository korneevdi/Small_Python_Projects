"""
I am a sportsman :)
I am a mid- and long-distance runner, and before races I often calculate the desired pace to get an idea of how fast I need to run to achieve my goal.
For this I use this program. With its help, you can calculate your running pace if you know the distance and desired finish time.
In addition, you can calculate the finishing time if you know the distance and pace of the run.
"""


# Calculate the desired pace
# This function takes a distance in km (float) and a time in the form "hh:mm:ss" (string)

def pace(dist, time):
    T = time.split(":")
    h = int(T[0])
    m = int(T[1])
    s = int(T[2])
    pace = (h*3600 + m*60 + s)/dist
    paceM = int(pace//60)
    paceS = pace%60
    print("Desired pace -", paceM, "min", paceS, "sec per km")


# Calculate the finish time
# This function takes a distance in km (float) and a pace in the form "mm:ss" (string)

def time(dist, pace):
    P = pace.split(":")
    M = int(P[0])
    S = int(P[1])
    time = (M*60 + S)*dist
    h = int(time//3600)
    m = int((time - h*3600)//60)
    s = time%60
    print("Finish time -", h, "h", m, "min", s, "sec")


# Application example
pace(10, "00:33:15")
time(10, "03:15")
