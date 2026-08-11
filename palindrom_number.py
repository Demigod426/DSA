class Solution:
    def isPalindrome(self,x:int)->bool:
       
        if x<0:
            return False

        reversed_num=0 
        t=x   #temporary num

        while t>0:
            reversed_num=reversed_num*10+(t%10)
            t//=10      # "//" is flooring, meaning it removes the decimal part of the number

        return x==reversed_num