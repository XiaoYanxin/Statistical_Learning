import numpy as np
class perceptron():
    def __init__(self,x,y,a=1):
        self.x = x
        self.y = y
        self.w = np.zeros(x.shape[1])
        self.b = 0
        self.a = 1
    def sign(self,x,w,b):
        if np.dot(x,w)+b>=0:
            return 1
        else:
            return -1
    def train(self):
        count = 0
        pass_n = 0
        x = self.x
        y = self.y
        w = self.w
        b = self.b
        a = self.a
        N = self.x.shape[0]
        while pass_n!=N:
            i = count%3
            if y[i]*self.sign(x[i],w,b)>0:
                pass_n+=1
            else:
                pass_n = 0
                w = w+a*y[i]*x[i]
                b = b+a*y[i]
            count+=1
            if count==10000:
                print('not linear partition')
                return (0,0)
        print(w,b,count)
        return w,b

if __name__ == '__main__':
    # x = np.array([[3,3],[4,3],[1,1]])
    # y = np.array([[1],[1],[-1]])
    x = np.array([[0,1],[1,0],[0,0],[1,1]])
    y = np.array([[1],[1],[0],[0]])
    test = perceptron(x,y)
    w,b = test.train()
    print('w = ',w,'\n','b = ',b)