from sqlalchemy.orm import Session
from app.assignment_table import Assignment


class AssignmentRepository:
    def __init__(self, db: Session):
        self.db: Session = db

    def get_assignment(self, assignment_id: int) -> Assignment:
        return self.db.query(Assignment).get(assignment_id)

    def get_assignments_by_ticket(self, ticket_id: int) -> list[Assignment]:
        return self.db.query(Assignment).filter(Assignment.ticket_id == ticket_id).all()

    def get_assignments_by_task(self, task_id: int) -> list[Assignment]:
        return self.db.query(Assignment).filter(Assignment.task_id == task_id).all()

    def save_assignments(self, assignment: Assignment) -> Assignment:
        self.db.add(assignment)
        self.db.commit()
        self.db.refresh(assignment)
        return assignment

    def delete(self, assignment: Assignment):
        self.db.delete(assignment)
        self.db.commit()
        return True
