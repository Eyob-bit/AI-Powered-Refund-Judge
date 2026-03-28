# { "Depends": "py-genlayer:test" }
from genlayer import *

class RefundJudge(gl.Contract):
    # Persistent storage for our disputes
    disputes: TreeMap[u256, str] 

    def __init__(self):
        self.disputes = TreeMap()

    @gl.public.write
    def file_dispute(self, order_id: u256, complaint: str):
        """Allows a customer to file a complaint."""
        self.disputes[order_id] = complaint
        print(f"Dispute filed for Order {order_id}")

    @gl.public.view
    def resolve_with_ai(self, order_id: u256) -> str:
        """
        Uses GenLayer's AI consensus to judge the complaint.
        This is where the 'Intelligence' happens!
        """
        complaint = self.disputes.get(order_id, "No complaint found.")
        
        # This prompt is sent to the network's validators/LLMs
        prompt = f"As an objective judge, read this complaint: '{complaint}'. " \
                 f"If it sounds like a valid reason for a refund, reply 'REFUND'. " \
                 f"If it is vague or minor, reply 'DENIED'."
        
        # In a full GenLayer contract, this would trigger the Equivalence Principle
        return gl.ai.ask(prompt)