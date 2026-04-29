from core.event_bus import EventBus
from agents.intake import IntakeAgent
from agents.orchestrator import OrchestratorAgent
from agents.domain.coordinator import DomainCoordinator
from agents.learner import LearnerAgent

def self_service_handler(ticket):
    print(f"[SelfService] Auto-reply: {ticket['text']}")

if __name__ == "__main__":
    bus = EventBus()

    intake = IntakeAgent(bus)
    orchestrator = OrchestratorAgent(bus)
    domain = DomainCoordinator(bus)
    learner = LearnerAgent(bus)

    bus.subscribe("self_service", self_service_handler)

    tickets = [
        {"id": 1, "text": "我要退款"},
        {"id": 2, "text": "怎么还没收到货"},
        {"id": 3, "text": "你们怎么搞的"},
    ]

    for t in tickets:
        intake.process(t)
