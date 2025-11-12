class TrafficAgent:
    def decide(self, light_color):
        light = light_color

        if light == "Red":
            return "Stop"
        elif light == "Yellow":
            return "Slow"
        elif light == "Green":
            return "Go"
        
agent = TrafficAgent()

print(agent.decide('Red'))
print(agent.decide('Green'))