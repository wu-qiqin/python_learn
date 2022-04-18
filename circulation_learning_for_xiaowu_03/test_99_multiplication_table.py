"""
Created by hu-jinwen on 2022/4/4
"""
def multi_table ():

    row = 1

    while row <= 9:

        col = 1
        while col <= row:
            print("%d *%d = %d" % (col, row, row*col), end="\t")
            col += 1

        #print("%d" %row)
        print("")

        row += 1

