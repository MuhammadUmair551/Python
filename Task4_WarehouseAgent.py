class WareHouseAgent:
    def __init__(self):
        self.picked_item = {}

    def decide(self, percept):
        location, has_Package = percept

        if location not in self.picked_item:
            self.picked_item[location] = False

        if has_Package == True and self.picked_item[location] == False:
              action = "pick"
              self.picked_item[location] = True
        elif self.picked_item[location] == True:
              action = "skip"
        else:
             action = "move"

        return action
    
wa = WareHouseAgent()   
print(wa.decide((("P1", True)))) 
print(wa.decide((("P1", True)))) 