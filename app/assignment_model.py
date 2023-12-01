from pydantic import BaseModel


class AssignmentBase(BaseModel):
    pass


class AssignmentCreate(AssignmentBase):
    pass


class AssignmentUpdate(AssignmentBase):
    task_id: int


class Assignment(AssignmentBase):
    id: int
    ticket_id: int
    task_id: int

    class Config:
        orm_mode = True
