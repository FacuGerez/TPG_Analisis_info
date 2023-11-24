from fastapi import HTTPException
from sqlalchemy.orm import Session
from assignment_model import AssignmentCreate
from assignment_repository import AssignmentRepository
from assignment_table import Assignment


class AssignmentService:
    def __init__(self, db: Session):
        self.assignment_repository: AssignmentRepository = AssignmentRepository(db)

    def get_assignments_by_ticket(self, ticket_id: int) -> list[[Assignment]]:
        return self.assignment_repository.get_assignments_by_ticket(ticket_id)

    def get_assignments_by_task(self, task_id: int) -> list[[Assignment]]:
        return self.assignment_repository.get_assignments_by_task(task_id)

    def get_assignment(self, assignment_id: int) -> Assignment:
        return self.assignment_repository.get_assignment(assignment_id)

    def create_assignment(self, assignment: AssignmentCreate, ticket_id: int) -> Assignment:
        assignment_data = assignment.dict()
        assignment_data.update({
            "ticket_id": ticket_id
        })
        assignment_new = Assignment(**assignment_data)
        return self.assignment_repository.save_assignments(assignment_new)

    def update_assignment(self, assignment_id: int, assignment: AssignmentCreate):
        assignment_update = self.assignment_repository.get_assignment(assignment_id)
        if assignment_update is None:
            raise HTTPException(status_code=404, detail="The assignment wasnt found")
        assignment_update.state = assignment.state
        assignment_update.priority = assignment.priority
        assignment_update.severity = assignment.severity
        assignment_update.title = assignment.title
        return self.assignment_repository.save_assignments(assignment_update)

    def delete_assignment(self, assignment_id: int):
        assignment_delety = self.assignment_repository.get_assignment(assignment_id)
        if assignment_delety is None:
            raise HTTPException(status_code=404, detail="The assignment wasnt found")
        return self.assignment_repository.delete(assignment_delety)
