import sys
import sys
class Graphs:
    def __init__(self):
        self.nodes=[]
        self.graph=[]
        self.nodeCount=0

    def addNode(self,v):
        pass

    def addEdge_Undirected_Unweighted(self,v1,v2):
        pass
        

    def addEdge_Undirected_Weighted(self,v1,v2,weight):
        pass


    def addEdge_Directed_Weighted(self,v1,v2,weight):
        pass

    
    def printGraph(self):
        pass
            
    def deleteGraph(self,v):
       pass

if __name__ =='__main__':

    obj=Graphs()
    while True:
        print("\n1. (Insertion) add a node using adjacency matrix representation")
        print("2. (Insertion) add a edge using adjacency matrix representation")
        print("3. (Insertion) add a edge undirected weighted graph")
        print("4. (Insertion) add a edge directed weighted graph")
        print("5. Print Graph")
        print ("6. Delete Operation")
        print("®. Exit\n")
        n=int(input("Enter any choice: "))
        if n==1:
            obj. addNode ()
        elif n==2:
            obj.addEdge_Undirected_Unweighted ()
        elif n==3:
            obj.addEdge_Undirected_Weighted ()
        elif n==4:
            obj. addEdge_Directed_Weighted ()
        elif n==5:
            obj. printGraph()
        elif n==6:
            obj. deleteGraph()
        elif n==0:
            sys.exit(0)