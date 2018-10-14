class Q1:
    def __init__(self):
        self.data=0

    def get(self,k):
        for p in range(0,len(k)):
            s=str(k[p])
            rea(s)

    def rea(self,s):
        
        
        count=0
        string=0
        #this code will be accepted for all string with Capital letters it's rejected all the symbols
        alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',' ']
        for i in range (0,len(s)):
            if s[i]==' ':
                count+=1
        if count>5:
            print("Invalid")
            sys.exit()
        for i in range (0,len(s)):
            for j in range(0,len(alphabet)):
                if s[i]==alphabet[j]:
                    string+=1
        if string==len(s):
            print("Valid")

k=["CH L","SU D"]
l=Q1()
l.get(k)
            
            
    
                    
    
        
