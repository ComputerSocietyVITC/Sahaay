from fastapi import APIRouter, Form
from fastapi.requests import Request
from pydantic import BaseModel
from pathlib import Path


class Department(BaseModel):
    department: str
    abbreviation: str


class delDepartment(BaseModel):
    department: str


admin = APIRouter()


@admin.get("/Show-all-departments")
def deptartments():
    from Logic.models import read_file

    DIR = str(Path(__file__).resolve().parent.parent) + r"\models\fixtures"
    data = read_file(DIR + "\dept.json")
    return data


@admin.post("/add-department")
def post_department(request: Request, param: Department):
    from Logic.models import UserModel, read_file, write_file

    user_data = UserModel.objects.get(username=request.user.username)
    if user_data.is_staff and request.method == "POST":
        DIR = str(Path(__file__).resolve().parent.parent) + r"\models\fixtures"
        data = read_file(DIR + "\dept.json")
        data.append([param.abbreviation, param.department])
        write_file(DIR + "\dept.json", data)
        return f"The following data has been added. {[param.abbreviation, param.department]}"


@admin.delete("/update-department")
def delete_department(request: Request, param: delDepartment):
    from Logic.models import read_file, write_file, UserModel

    user_data = UserModel.objects.get(username=request.user.username)
    if user_data.is_staff and request.method == "DELETE":
        DIR = str(Path(__file__).resolve().parent.parent) + r"\models\fixtures"
        data = read_file(DIR + "\dept.json")
        for i in data:
            if i[1] == param.department:
                data.remove(i)
        write_file(DIR + "\dept.json", data)
        return f"The following data has been removed. {[param.department]}"

@admin.put("/department")
def update_department(request: Request, param: Department):
    from Logic.models import read_file, write_file, UserModel

    user_data = UserModel.objects.get(username = request.user.username)
    if user_data.is_staff and request.method == "PUT":
        DIR = str(Path(__file__).resolve().parent.parent) + r"\models\fixtures"
        data = read_file(DIR + "\dept.json")
        for i in data:
            if i[0] == param.abbreviation:
                i[1] = param.department
                data.insert(data.index(i), i)
                data.pop(data.index(i)+1)
                write_file(DIR + "\dept.json", data)    
                return i 
