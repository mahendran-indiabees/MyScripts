# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
lst=["abc","abc","acb"]
max_row=len(lst)
max_col=len(lst[0])
PixelCount=0
for row in range(max_row):
    for col in range(max_col):
        row_min=row-1
        col_max=col+1
        AdjUp="Match"
        AdjRight="Match"
        if(row_min > -1):
            if lst[row][col] != lst[row_min][col]:
                AdjUp="NotMatch"
            else:
                AdjUp="Match"
        else:
            AdjUp="NotMatch"
            
        if(col_max < max_col):
            if lst[row][col] != lst[row][col_max]:
                AdjRight="NotMatch"
            else:
                AdjRight="Match"
        else:
            AdjRight="NotMatch"
           
        if AdjRight == "NotMatch" and AdjUp == "NotMatch":
            print("Increasing Color for position [{}][{}]".format(row,col))
            PixelCount=PixelCount+1
          
print("PixelCount is [{}]".format(PixelCount))
            
