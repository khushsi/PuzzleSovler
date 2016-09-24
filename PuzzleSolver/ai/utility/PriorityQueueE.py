from Queue import  PriorityQueue
import copy

class PriorityQueueE(object):
    def __init__(self):
        self.queuemain = PriorityQueue()
        self.queueshuffle = PriorityQueue()
        self.objectdicti = dict()
        
    def put(self, (pri,dobj)):
        d = dobj[len(dobj)-1]
        if(d in self.objectdicti.keys() ):
#             print self.queuemain.qsize()
            if ( self.objectdicti[d][0] > pri ):            
                while(not self.queuemain.empty()):
                    temp=self.queuemain.get()
                    if(temp[1] == d):
                        if(temp[0] > pri):
#                             print temp[0]
#                             print pri
                            self.queueshuffle.put((pri,temp[1]))
#                             print "I am here for duplicate entry"                        
                            self.objectdicti[d]=(pri,dobj)
                        else:
                            self.queueshuffle.put(temp)       
                    else:
                        self.queueshuffle.put(temp)
#                 print "shuffle queue" + str(self.queueshuffle.qsize())
                self.queuemain= copy.copy(self.queueshuffle)
#                 print "main queue" + str(self.queuemain.qsize())
                self.queueshuffle = PriorityQueue()
                
             
        else:  
            self.queuemain.put((pri,d))
            self.objectdicti[d]=(pri,dobj)

    def get(self):
#         print self.queuemain.qsize()
        pri,d = self.queuemain.get()        
        return self.objectdicti[d]
    
    def qsize(self):
        return self.queuemain.qsize()
    
    def getPath(self,d):
        if(self.objectdicti[d]):
            return self.objectdicti[d]
