from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import get_db
from assignment_model import AssignmentCreate
from assignment_service import AssignmentService

router = APIRouter(
    tags=["assignment"],
)


@router.post("/ticket/{ticket_id}/assignment")
async def create_assignment(ticket_id: int, assignment: AssignmentCreate, db: Session = Depends(get_db)):
    service_assignment: AssignmentService = AssignmentService(db)
    assignment_new = service_assignment.create_assignment(assignment, ticket_id)
    return assignment_new


@router.get("/ticket/{ticket_id}/assignments")
async def get_assignments(ticket_id: int, db: Session = Depends(get_db)):
    service_assignment: AssignmentService = AssignmentService(db)
    return service_assignment.get_assignments_by_ticket(ticket_id)


@router.get("/task/{task_id}/assignments")
async def get_assignments(task_id: int, db: Session = Depends(get_db)):
    service_assignment: AssignmentService = AssignmentService(db)
    return service_assignment.get_assignments_by_task(task_id)


@router.get("/assignment/{assignment_id}")
async def get_assigment(assignment_id: int, db: Session = Depends(get_db)):
    service_assignment: AssignmentService = AssignmentService(db)
    return service_assignment.get_assignment(assignment_id)


@router.put("/assignment/{assignment_id}")
async def update_assigment(assignment_id: int, assignment: AssignmentCreate, db: Session = Depends(get_db)):
    service_assignment: AssignmentService = AssignmentService(db)
    return service_assignment.update_assignment(assignment_id, assignment)


@router.delete("/assignment/{assignment_id}")
async def delete_assignment(assignment_id: int, db: Session = Depends(get_db)):
    service_assignment: AssignmentService = AssignmentService(db)
    return service_assignment.delete_assignment(assignment_id)
