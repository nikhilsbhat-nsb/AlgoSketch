import time

running = False


def changeRun(run):
    global running
    running = run


def bubble_sort(data, drawData, timeTick, l):
    for i in range(len(data)):
        for j in range(len(data) - i):
            drawData(data, ['yellow' if x == j or x == j +
                     1 else 'red' for x in range(len(data))])
            time.sleep(timeTick)
            a = data[j]
            if a != data[-1]:
                b = data[j+1]
                if(a > b):
                    data[j], data[j+1] = b, a
                    drawData(data, ['green' if x == j or x ==
                             j+1 else 'red' for x in range(len(data))])
                    time.sleep(timeTick)


def bubble_sort_step(data, drawData):
    global running
    if(running):
        for i in range(len(data)):
            for j in range(len(data) - i):
                if(running):
                    drawData(data, ['yellow' if x == j or x ==
                             j+1 else 'red' for x in range(len(data))])
                    time.sleep(2)
                    if running:
                        a = data[j]
                        if a != data[-1]:
                            b = data[j+1]
                            if(a > b):
                                data[j], data[j+1] = b, a
                                drawData(
                                    data, ['green' if x == j or x == j+1 else 'red' for x in range(len(data))])
                                running = False
