def drawLine(tickLength, tickLabel=''):
    line = '-' * tickLength
    if tickLabel:
        line += ' ' + tickLabel
    print(line)

def drawInterval(centerLength):
    if centerLength > 0:
        drawInterval(centerLength-1)
        drawLine(centerLength)
        drawInterval(centerLength-1)

def drawRuler(numInches, majorLength):
    drawLine(majorLength, '0')
    for i in range(1, numInches+1):
        drawInterval(majorLength-1)
        drawLine(majorLength, str(i))






if __name__ == '__main__':
    drawRuler(6,3)
    print('=' * 30)