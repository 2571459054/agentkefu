from core.base_agent import Agent

class OrchestratorAgent(Agent):
    def __init__(self, bus):
        super().__init__("Orchestrator", bus)
        bus.subscribe("parsed_ticket", self.route)

    def route(self, ticket):
        if ticket["intent"] == "general":
            self.bus.publish("self_service", ticket)
        else:
            self.bus.publish("domain_process", ticket)
