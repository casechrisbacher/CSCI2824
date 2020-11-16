def quantifierConverter(x):
    output = ''
    counter = 0
    for i in range(len(x)):
        if(x[counter] == u'\u2200'):
            output += 'for every'
        elif(x[counter] == u'\u2203'):
            output += 'there exists'
        else:
            output += x[counter]
        counter += 1
        
    return output