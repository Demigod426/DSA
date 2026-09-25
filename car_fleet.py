#STACK
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair=[[p,s] for p,s in zip(position,speed)]
        stack=[]

        for p,s in sorted(pair)[::-1]:#REVERSAL (RIGHT TO LEFT)
            stack.append((target-p)/s)
            if len(stack)>=2 and stack[-1]<=stack[-2]:#COMPARES THE TOP 2 ELEMENTS 
                stack.pop()
        return len(stack)


#ITERATION (SAME TC & SC BUT DIFFICULT TO IMPLEMENT IMO)
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair=[(p,s) for p,s in zip(position,speed)]
        pair.sort(reverse=True)

        fleets=1
        prevTime=(target-pair[0][0])/pair[0][1]
        for i in range(1,len(pair)):
            currCar=pair[i]
            currTime=(target-currCar[0])/currCar[1]
            if currTime>prevTime:
                fleets+=1
                prevTime=currTime
        return fleets