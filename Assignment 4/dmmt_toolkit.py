class BSTNode:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None

class BST:
    def __init__(self):
        self.root=None

    def insert(self,key):
        def f(r,k):
            if r is None:
                return BSTNode(k)
            if k<r.key:
                r.left=f(r.left,k)
            else:
                r.right=f(r.right,k)
            return r
        self.root=f(self.root,key)

    def search(self,key):
        def f(r,k):
            if r is None:
                return False
            if r.key==k:
                return True
            if k<r.key:
                return f(r.left,k)
            return f(r.right,k)
        return f(self.root,key)

    def inorder(self):
        res=[]
        def f(r):
            if r:
                f(r.left)
                res.append(r.key)
                f(r.right)
        f(self.root)
        return res

    def delete(self,key):
        def f(r,k):
            if r is None:
                return r
            if k<r.key:
                r.left=f(r.left,k)
            elif k>r.key:
                r.right=f(r.right,k)
            else:
                if r.left is None and r.right is None:
                    return None
                if r.left is None:
                    return r.right
                if r.right is None:
                    return r.left
                t=self.min(r.right)
                r.key=t.key
                r.right=f(r.right,t.key)
            return r
        self.root=f(self.root,key)

    def min(self,n):
        while n.left:
            n=n.left
        return n

class Graph:
    def __init__(self):
        self.g={}

    def add_edge(self,u,v,w):
        if u not in self.g:
            self.g[u]=[]
        self.g[u].append((v,w))

    def print_graph(self):
        for i in self.g:
            print(i,"->",self.g[i])

    def bfs(self,s):
        vis=set([s])
        q=[s]
        res=[]
        while q:
            n=q.pop(0)
            res.append(n)
            for x,_ in self.g.get(n,[]):
                if x not in vis:
                    vis.add(x)
                    q.append(x)
        return res

    def dfs(self,s):
        vis=set()
        res=[]
        def f(n):
            vis.add(n)
            res.append(n)
            for x,_ in self.g.get(n,[]):
                if x not in vis:
                    f(x)
        f(s)
        return res

class HashTable:
    def __init__(self,size):
        self.size=size
        self.t=[[] for _ in range(size)]

    def h(self,key):
        return key%self.size

    def insert(self,key,val):
        i=self.h(key)
        for p in self.t[i]:
            if p[0]==key:
                p[1]=val
                return
        self.t[i].append([key,val])

    def get(self,key):
        i=self.h(key)
        for p in self.t[i]:
            if p[0]==key:
                return p[1]
        return None

    def delete(self,key):
        i=self.h(key)
        for j,p in enumerate(self.t[i]):
            if p[0]==key:
                self.t[i].pop(j)
                return

    def display(self):
        for i,b in enumerate(self.t):
            print("Index",i,":",b)

def main():
    print("BST TEST")
    b=BST()
    v=[55,35,75,25,45,65,85]
    for i in v:
        b.insert(i)
    print("Inorder:",b.inorder())
    print("Search 25:",b.search(25))
    print("Search 90:",b.search(90))
    b.delete(25)
    print("After deleting 25:",b.inorder())
    b.insert(68)
    b.delete(65)
    print("After deleting 65:",b.inorder())
    b.delete(55)
    print("After deleting 55:",b.inorder())

    print("\n GRAPH TEST")
    g=Graph()
    e=[('A','B',2),('A','C',4),('B','D',7),('B','E',3),('C','E',1),('D','F',5),('E','D',2),('E','F',6),('C','F',8)]
    for u,v,w in e:
        g.add_edge(u,v,w)
    g.print_graph()
    print("BFS from A:")
    print(" ".join(g.bfs('A')))
    print("DFS from A:")
    print(" ".join(g.dfs('A')))

    print("\n HASH TABLE TEST")
    h=HashTable(5)
    k=[11,16,21,6,13]
    for i in k:
        h.insert(i,i*10)
    h.display()
    print("Get 11:",h.get(11))
    print("Get 16:",h.get(16))
    print("Get 6:",h.get(6))
    h.delete(16)
    print("After deleting 16:")
    h.display()

if __name__=="__main__":
    main()