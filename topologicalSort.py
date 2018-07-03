class Queue(object):
    def __init__ (self):
        self.list = []
    def enque(self):
        self.list.append()
    def deque(self):
        return(self.list.pop(0))
    def length(self):
        return len(self.list)
        
def createIndegreeCount():
    indegreeCount = {}
    for k,v in graph.items():
        indegreeCount[k] = 0
        for v in list(graph.values()):
            if k in v:
                indegreeCount[k] += 1
    return indegreeCount

def sortByQueue():
    pass

graph = {'A':['B','C'],
        'B':['D','E'],
        'C':['D','E'],
        'D':['E'],
        'E':[]}
        
indegreeCount = createIndegreeCount()
listQueue = []
queue = Queue(listQueue)
sortedList = []

    
print(indegreeCount)

#while len(sortedList) != len(indegreeCount):
for k,v in indegreeCount.items():
    if v == 0:
        queue.enque(k)
        for k2,v2 in graph.items():
            if k2 == k:
                for k3, v3 in indegreeCount.items():
                    for x in range(0,len(v2)):
                        if v2[x] == k3:
                            v3 -= 1
        sortedList.append(queue.deque())
    else:
        break
                               
    
print(sortedList)