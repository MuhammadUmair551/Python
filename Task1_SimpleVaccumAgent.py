class VaccumAgent:
    def decide(self, percept):
        location, status = percept
        if status == "dirty":
            return 'suck'
        elif status == 'clean':
            return 'move'
        
agent = VaccumAgent()

print(agent.decide(('A', 'dirty')))
print(agent.decide(('B', 'clean')))