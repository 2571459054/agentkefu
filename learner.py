import random
from core.base_agent import Agent

class LearnerAgent(Agent):
    def __init__(self, bus):
        super().__init__("Learner", bus)
        bus.subscribe("final_result", self.learn)

    def learn(self, result):
        score = random.random()
        print("[Learner] score:", round(score, 2))
        if score < 0.5:
            print("[Learner] optimizing...")
