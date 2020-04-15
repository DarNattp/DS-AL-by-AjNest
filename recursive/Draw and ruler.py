def drawLine(tickLength, tickLabel=''): #creat line from receive data of other fuction.
    line = '-' * tickLength
    if tickLabel:
        line += ' ' + tickLabel
    print(line)

def drawInterval(centerLength): #define line and sent to drawLine funtion to creat line 
    if centerLength > 0:
        drawInterval(centerLength-1)
        drawLine(centerLength)
        drawInterval(centerLength-1)

def drawRuler(numInches, majorLength): #main in create ruler : numInches is number main of ruler. 
    drawLine(majorLength, '0')          #majorLength is range between main number of ruler.
    for i in range(1, numInches+1):
        drawInterval(majorLength-1)     #creat recursive line between main line or number
        drawLine(majorLength, str(i)) #creat line and number of main line


if __name__ == '__main__':
    drawRuler(6,3)
    print('=' * 30)