class LocationNode(object):
    
    def __init__(self, LocationName, location, isgoal=False):
        self.name = LocationName 
        self.location = location
        self.isgoal = isgoal
        self.childnodes = []
        self.childnodeswithcost = dict()
        
    def printNode(self):
        return (self.name)
            
    def isgoalState(self):
        return self.isgoal
    
    def getCost(self,tonode=None):
        
        if(tonode is not None):
            return self.childnodeswithcost[tonode]
        else:
            return 0
    