class LocationNode(object):
    
    def __init__(self, LocationName, location=(0,0), isgoal=False):
        self.name = LocationName 
        self.location = location
        self.isgoal = isgoal
        self.childnodes = []
        self.childnodeswithcost = dict()
        
    def printNode(self):
        return (self.name)
            
    def isgoalState(self):
        return self.isgoal
    