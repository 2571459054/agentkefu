from core.base_agent import Agent

class DomainCoordinator(Agent):
    def __init__(self, bus):
        super().__init__("DomainCoordinator", bus)
        bus.subscribe("domain_process", self.process)

    def process(self, ticket):
        result = {
            "ticket": ticket,
            "decision": "approve_refund" if ticket["intent"] == "refund" else "investigate"
        }
        print("[Domain]", result)
        self.bus.publish("final_result", result)
