# app/endpoints/__init__.py

from .auth import router as auth_router
from .employee import router as employee_router
from .agronomists import router as agronomist_router
from .beds import router as beds_router
from .flower_base import router as flower_base_router
from .flower_plantings import router as planting_router
from .purchases import router as purchase_router
from .purchase_plan import router as purchase_plan_router
from .reports import router as report_router
from .resources import router as resource_router

routes = [
    (auth_router, "/auth", "Auth"),
    (employee_router, "/employees", "Employees"),
    (agronomist_router, "/agronomists", "Agronomists"),
    (beds_router, "/beds", "Beds"),
    (flower_base_router, "/flowers", "Flowers"),
    (planting_router, "/plantings", "Plantings"),
    (purchase_router, "/purchases", "Purchases"),
    (purchase_plan_router, "/purchase_plan", "Purchase Plan"),
    (report_router, "/reports", "Reports"),
    (resource_router, "/resources", "Resources"),
]
