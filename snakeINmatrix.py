class Solution(object):
    def finalPositionOfSnake(self,n,commands):
        row=0
        col=0

        for command in commands:

            if command=="UP":
                row-=1
            elif command=="DOWN":
                row+=1
            elif command=="LEFT":
                col-=1
            else:  #RIGHT 
                col+=1

        return row*n+col           