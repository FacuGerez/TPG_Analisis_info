from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.assignment_model import AssignmentCreate, AssignmentUpdate
from app.assignment_repository import AssignmentRepository
from app.assignment_table import Assignment


class AssignmentService:
    def __init__(self, db: Session):
        self.assignment_repository: AssignmentRepository = AssignmentRepository(db)

    def get_assignments_by_ticket(self, ticket_id: int) -> list[Assignment]:
        return self.assignment_repository.get_assignments_by_ticket(ticket_id)

    def get_assignments_by_task(self, task_id: int) -> list[Assignment]:
        return self.assignment_repository.get_assignments_by_task(task_id)

    def get_assignment(self, assignment_id: int) -> Assignment:
        assignment: Assignment = self.assignment_repository.get_assignment(assignment_id)
        if assignment is None:
            raise HTTPException(status.HTTP_404_NOT_FOUND, detail="No se encontro la asignacion deseada")
        return assignment

    def create_assignment(self, assignment: AssignmentCreate, ticket_id: int) -> Assignment:
        assignment_data = assignment.dict()
        assignment_data.update({
            "ticket_id": ticket_id
        })
        assignment_new = Assignment(**assignment_data)
        return self.assignment_repository.save_assignments(assignment_new)

    def update_assignment(self, assignment_id: int, assignment: AssignmentUpdate) -> Assignment:
        assignment_update = self.get_assignment(assignment_id)
        assignment_update.task_id = assignment.task_id
        return self.assignment_repository.save_assignments(assignment_update)

    def delete_assignment(self, assignment_id: int):
        assignment_delety = self.get_assignment(assignment_id)
        return self.assignment_repository.delete(assignment_delety)

    def delete_by_ticket(self, ticket_id: int):
        assigments: list[Assignment] = self.get_assignments_by_ticket(ticket_id)
        for a in assigments:
            self.delete_assignment(a.id)
        return True

    def delete_by_task(self, task_id: int):
        assigments: list[Assignment] = self.get_assignments_by_task(task_id)
        for a in assigments:
            self.delete_assignment(a.id)
        return True
