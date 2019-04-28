import numpy as np
import math
class KD_Node():
    def __init__(self,point = None,split = None,LL = None,RR = None):
        self.point = point
        self.split = split
        self.left = LL
        self.right = RR

# def find_middle(l):
#     li = sorted(l)
#     middle = li[len(li)//2]
#     i = l.index(middle)
#     return i

def creat_kdtree(points,split = 0):
    # array to list : arr.tolist()
    N = len(points)
    if N==0:
        return
    dim_N = len(points[0])
    split = split%dim_N
    points.sort(key=lambda x:x[split])
    mid = N//2
    root = KD_Node(points[mid],split = split)
    root.left = creat_kdtree(points[:mid],split=split+1)
    root.right = creat_kdtree(points[mid+1:],split=split+1)
    #print('finish one slplit')
    return root

def distance(p1,p2):
    d = 0
    for i in range(len(p1)):
        d+=(p1[i]-p2[i])**2
    return d**0.5

def preorder(root):
    l = []
    p = root
    stack = []
    while stack or p:
        if p:
            l.append(p.point)
            stack.append((p))
            p = p.left
        else:
            p = stack.pop()
            p = p.right
    print('finish order')
    return l

def midorder(root,l):#l as output
    if root==None:
        return
    midorder(root.left,l)
    l.append(root.point)
    midorder(root.right,l)

def kdt_search(root,point,k):
    nodes = []
    dis = []
    # visit = []
    stack = []
    temp = root
    while temp:
        stack.append(temp)
        s = temp.split
        if point[s]<temp.point[s]:
            temp = temp.left
        else:
            temp = temp.right
    node = stack.pop()
    # visit.append(node)
    nodes.append(node.point)
    dis.append(distance(node.point,point))
    while stack!=[]:
        par = stack.pop()
        # visit.append(par)
        d = distance(par.point, point)
        s = par.split
        max_d = max(dis)
        if d<max(dis) or len(nodes)<k:
            if len(nodes)==k:
                i = dis.index(max_d)
                del nodes[i]
                del dis[i]
            nodes.append(par.point)
            dis.append(d)
            max_d = max(dis)
        if abs(par.point[s]-point[s])<max_d or len(nodes)<k:
            if point[s]<par.point[s]:
                temp = par.right
            else:
                temp = par.left
            while temp:
                stack.append(temp)
                s = temp.split
                if point[s] < temp.point[s]:
                    temp = temp.left
                else:
                    temp = temp.right
            # if temp:
            #     stack.append(temp)
            # visit.append(node)
            # d = distance(node.point,point)
            # if d<max_d or len(nodes)<k:
            #     if len(nodes)==k:
            #         i = dis.index(max_d)
            #         del nodes[i]
            #         del dis[i]
            #     nodes.append(node.point)
            #     dis.append(d)
    return nodes,dis

def knn(x,point,k):
    for i in range(len(x)):
        d = distance(x[i],point)
        x[i]+=[d]
    x.sort(key = lambda x:x[-1])
    return x[:k]

if __name__ == '__main__':
    #x = [[7,2],[5,4],[9,6],[2,3],[4,7],[8,1],[13,11],[10,12],[11,42],[62,71],[87,53],[17,21],[23,29],[14,19],[8,13],[22,33]]
    x = np.random.randint(1,100,(200,5)).tolist()
    print(x)
    r = creat_kdtree(x)
    l_mid = []
    midorder(r,l_mid)
    print('midorder:',l_mid)  #test kdtree
    l_pre = preorder(r)
    print('preorder',l_pre)
    point = [1,10,20,30,40]
    k = 5
    nodes,dis = kdt_search(r,point,k)
    print('kdtree nodes:','distance:',nodes,dis)
    kn = knn(x,point,k)
    kn = np.array(kn)
    print('knn nodes:',kn[:,:-1].astype(np.uint8).tolist(),'distance:',kn[:,-1].tolist())
    print(max(dis)==kn[:,-1].tolist()[-1])


