from fastapi import APIRouter, Form
from fastapi.requests import Request
from pydantic import BaseModel
from pathlib import Path
import json

class Department(BaseModel):
    department: str
    abbreviation: str

class delDepartment(BaseModel):
    department: str


admin = APIRouter()

@admin.get("/Hello-world")
def HelloWorld():
    return f"Hello World"

@admin.get("/Show-all-departments")
def depts():
    from Logic.models import read_file
    DIR = str(Path(__file__).resolve().parent.parent) + r"\models\fixtures"
    data = read_file(DIR + '\dept.json')
    return data

@admin.post("/add-department")
def post_dept(request: Request, param: Department): 
    from Logic.models import UserModel, read_file, write_file
    user_data = UserModel.objects.get(username = request.user.username)
    if user_data.is_staff and request.method == 'POST':
            DIR = str(Path(__file__).resolve().parent.parent) + r"\models\fixtures"
            data = read_file(DIR + '\dept.json')
            data.append([param.abbreviation, param.department])
            write_file(DIR + '\dept.json', data)
            return f"The following data has been added. {[param.abbreviation, param.department]}"

@admin.delete("/department")
def del_dept(request: Request, param: delDepartment):
    from Logic.models import read_file, write_file, UserModel
    user_data = UserModel.objects.get(username = request.user.username)
    if user_data.is_staff and request.method == 'DELETE':
            DIR = str(Path(__file__).resolve().parent.parent) + r"\models\fixtures"
            data = read_file(DIR + '\dept.json')
            for i in data:
                if i[1] == param.department:
                    data.remove(i)
            write_file(DIR + '\dept.json', data)
            return f"The following data has been removed. {[param.department]}"
