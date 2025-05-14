from pydantic import BaseModel
from datetime import date



class ReportBase(BaseModel):
    scale: str
    title: str
    report_link: str

class ReportCreate(ReportBase):
    pass

class Report(ReportBase):
    id: int

    class Config:
        orm_mode = True