from random import randint
class Url_shortener:
    myDb = {}
    myUrls = {}
    seed = [-1,-1,-1,0]
    def create_key(self):
        alphas = "abcdefghijklmnopqrstuvwxyz"
        key = ""
        for i in range(3,-1,-1):
            if(self.seed[i] != -1):
                key += alphas[self.seed[i]]
                
            else:
                break
        
        self.seed[3] += 1
        if(self.seed[3] == 26):
            self.seed[3] = 0
            for j in range(2,-1,-1):
                self.seed[j] += 1
                if(self.seed[j] < 26):
                    break
                else:
                    self.seed[j] = 0
        return key
        
    def shorten(self, long_url):
        if(long_url in self.myUrls):
            return self.myUrls[long_url]
        key = "short.ly/" + self.create_key()
        self.myDb[key] = long_url
        self.myUrls[long_url] = key
        return key
    
    def redirect(self, short_url):
        if(short_url in self.myDb):
            return self.myDb[short_url]
        return ""

u = Url_shortener()
for i in range(470000):
    print(u.shorten("gx" + str(i)))