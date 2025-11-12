class ModelVaccumAgent:
    def __init__(self):
        self.state = {"A": "clean",  "B": "Dirty"}
    def decide(self, percept):
        location , status = percept
        self.state[location] = status

        if status == "Dirty":
            action = "suck"
            self.state[location] = "clean"
        else:
            if self.state["A"] == "clean" and self.state["B"] == "clean":
                action = "NoAction"
            else:
                action = "Move"
            
        return action
    
    
ag = ModelVaccumAgent()

print(ag.decide(("A", "Dirty"))) 
print(ag.decide(("A", "clean")))   
print(ag.decide(("A", "clean")))   
print(ag.decide(("B", "clean")))  