import time


def partition(data, head, tail, drawData, timeTick):
    border = head
    pivot = data[tail]

    drawData(data, getColorArray(len(data), head, tail, border, border))
    time.sleep(timeTick)
    for j in range(head, tail):
        if data[j] < pivot:
            drawData(data, getColorArray(
                len(data), head, tail, border, j, True))
            time.sleep(timeTick)
            data[border], data[j] = data[j], data[border]
            border = border + 1

        drawData(data, getColorArray(len(data), head, tail, border, j))
        time.sleep(timeTick)

# swap pivot with border values
    drawData(data, getColorArray(len(data), head, tail, border, tail, True))
    time.sleep(timeTick)
    data[border], data[tail] = data[tail], data[border]
    return border


def quick_sort(data, head, tail, drawData, timeTick):

    if head < tail:
        partitionIndx = partition(data, head, tail, drawData, timeTick)
    # Left partition
        quick_sort(data, head, partitionIndx-1, drawData, timeTick)
    # Right partition
        quick_sort(data, partitionIndx+1, tail, drawData, timeTick)


def getColorArray(datalen, head, tail, border, curIndx, isSwapping=False):
    colorArrary = []
    for i in range(datalen):
        # default color
        if i >= head and i <= tail:
            # current sorting partition
            colorArrary.append('gray')
        else:
            # non-sorting partition
            colorArrary.append('white')

        if i == tail:
            # pivot color
            colorArrary[i] = 'blue'
        elif i == border:
            # border color
            colorArrary[i] = 'red'
        elif i == curIndx:
            # current pointer color
            colorArrary[i] = 'yellow'

        if(isSwapping):
            if i == border or i == curIndx:
                colorArrary[i] = 'green'
    return colorArrary


# ************************************************
# Step by setp function
# ************************************************
running = False
cnt = 0


def changeRunQuick(run):
    global running
    running = run


def partition_step(data, head, tail, drawData, timeTick):
    global running
    border = head
    pivot = data[tail]

    drawData(data, getColorArray_step(len(data), head, tail, border, border))
    time.sleep(timeTick)
    for j in range(head, tail):
        if data[j] < pivot:
            drawData(data, getColorArray_step(
                len(data), head, tail, border, j, True))
            time.sleep(timeTick)
            data[border], data[j] = data[j], data[border]
            border = border + 1

        drawData(data, getColorArray_step(len(data), head, tail, border, j))
        time.sleep(timeTick)

    # swap pivot with border values
    drawData(data, getColorArray_step(
        len(data), head, tail, border, tail, True))
    time.sleep(timeTick)
    data[border], data[tail] = data[tail], data[border]
    # running = False
    return border, head


def quick_sort_step(data, drawData):
    global cnt
    if cnt == 0:
        head = 0
        tail = len(data)-1
        cnt = cnt+1
    global running
    timeTick = 0.2
    if running:
        if head < tail:
            partitionIndx, head = partition_step(
                data, head, tail, drawData, timeTick)
        # Left partition
            running = False
            if running:
                quick_sort_step(data, head, partitionIndx -
                                1, drawData, timeTick)
        # Right partition
                if running:
                    quick_sort_step(data, partitionIndx+1,
                                    tail, drawData, timeTick)


def getColorArray_step(datalen, head, tail, border, curIndx, isSwapping=False):
    colorArrary = []
    for i in range(datalen):
        # default color
        if i >= head and i <= tail:
            # current sorting partition
            colorArrary.append('gray')
        else:
            # non-sorting partition
            colorArrary.append('white')

        if i == tail:
            # pivot color
            colorArrary[i] = 'blue'
        elif i == border:
            # border color
            colorArrary[i] = 'red'
        elif i == curIndx:
            # current pointer color
            colorArrary[i] = 'yellow'

        if(isSwapping):
            if i == border or i == curIndx:
                colorArrary[i] = 'green'
    return colorArrary
