

def bitOperator(x, y):
    counter = 0
    orString = ''
    andString = ''
    for i in range(len(x)):
            if (int(x[counter]) == 1) | (int(y[counter]) == 1):
                orString = orString + '1'
            else:
                orString = orString + '0'
            if (int(x[counter]) == 1)& (int(y[counter]) == 1):
                andString = andString + '1'
            else:
                andString = andString + '0'
            counter = counter + 1
            
            
    tup = (orString, andString);

    return tup

        






