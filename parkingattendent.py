available=[
    [1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0]
    ]
def carParking(available):
    row=0
    column=0
    l=[]
    #iterate through each row
    for row in available:
        count=0
        #iterate through each column in each row and count how many empty spots are in each row
        for j in row:
            if j==0:
                count+=1
        l.append(count)
    #iterate though list l to see which row has the most empty spots, return the row number 
    for i in range(len(l)):
        if int(l[i])>row:
            row=l[i]
            #iterate through the available's most emply row, then return the first 0 column
            for r in range(len(available)):
                for j in available[row]:
                    if j==0:
                        column=available.index(j)
                    
            
    print(row)
    print(column)

carParking(available)
