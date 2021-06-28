import time

running = False
var=0

def changeRun(run):
    global running
    running = run


def selection_sort(s, drawData, timeTick):
    for i in range(0,len(s)-1):
        drawData(s, ['blue' if x == i 
                     else 'red' for x in range(len(s))])
        time.sleep(timeTick)
        var = i
        p=0
        mini=s[-1]
        for j in range(i,len(s)):
            drawData(s, ['yellow' if x == j else 'blue' if x == var
                     else 'red' for x in range(len(s))])
            time.sleep(timeTick)
            if s[j]<=mini:
                mini=s[j]
                p=j
        s[i],s[p]=s[p],s[i]
        drawData(s, ['green' if x == i else 'grey' if x == p
                      else 'red' for x in range(len(s))])
        time.sleep(timeTick)    



# Selection sort step


def selection_sort_step(s, drawData):
    global running
    if(running):
        for i in range(0,len(s)-1):
            drawData(s, ['blue' if x == i 
                        else 'red' for x in range(len(s))])
            time.sleep(2)
            var = i
            p=0
            mini=s[-1]
            for j in range(var,len(s)):
                drawData(s, ['yellow' if x == j else 'blue' if x == var
                        else 'red' for x in range(len(s))])
                time.sleep(2)
                if s[j]<=mini:
                    mini=s[j]
                    p=j
            s[i],s[p]=s[p],s[i]
            drawData(s, ['green' if x == i else 'grey' if x == p
                        else 'red' for x in range(len(s))])
            time.sleep(2)
            running = False