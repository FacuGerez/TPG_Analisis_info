from pydantic import BaseModel


class AssignmentBase(BaseModel):
    task_id: int


class AssignmentCreate(AssignmentBase):
    pass


class AssignmentUpdate(AssignmentBase):
    pass


class Assignment(AssignmentBase):
    id: int
    ticket_id: int

    class Config:
        orm_mode = True
