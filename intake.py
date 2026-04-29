import random
from core.base_agent import Agent

class IntakeAgent(Agent):
    def __init__(self, bus):
        super().__init__("Intake", bus)

    def process(self, ticket):
        text = ticket["text"]

        if "退款" in text:
            intent = "refund"
        elif "没收到" in text:
            intent = "delivery_issue"
        else:
            intent = "general"

        enriched = {
            **ticket,
            "intent": intent,
            "urgency": random.choice(["low", "medium", "high"]),
            "confidence": round(random.uniform(0.6, 0.95), 2)
        }

        print("[Intake]", enriched)
        self.bus.publish("parsed_ticket", enriched)
