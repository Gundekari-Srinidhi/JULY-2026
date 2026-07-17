class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bull = 0
        cows = 0
        d = {}
        for i in secret:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        l = list(guess)
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bull +=1
                l[i] = "*"
                d[secret[i]] -= 1
                if d[secret[i]] == 0:
                    del d[guess[i]]
        for i in l:
            if i in d and i in secret:
                d[i] -= 1
                if d[i] == 0:
                    del d[i]
                cows += 1
        return str(bull)+"A"+str(cows)+"B"


        
            