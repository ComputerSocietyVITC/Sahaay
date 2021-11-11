from starlette.status import HTTP_200_OK, HTTP_202_ACCEPTED, HTTP_404_NOT_FOUND
from fastapi import Request, APIRouter, File
from fastapi.datastructures import UploadFile
from pydantic import BaseModel


class IssueTable(BaseModel):
    Issue_Name: str
    Issue_Tags: list[str]
    Issue_description: str
    isActive: bool
    uniqueID: str
    LinkedIssue_id: str
    User_id: str


class IssueTableNew(BaseModel):
    Issue_Name: str
    Issue_Tags: list[str]
    Issue_description: str
    isActive: bool
    uniqueID: str
    User_Id: str


issues = APIRouter()


@issues.get("/get-all-issues")
def show_all_issues():
    from Logic.models import Issues

    return list(Issues.objects.all())


@issues.get("/get-issue/{issue_id}")
def get_specific_issue(issue_id: str):
    from Logic.models import Issues

    specific_issue = Issues.objects.get(Issue_Name=issue_id)
    return specific_issue


@issues.post("/post-new-issue")
def post_new_issue(request: Request, table: IssueTableNew):
    from Logic.models import Issues, UserModel

    instance = Issues(
        Issue_Name=table.Issue_Name,
        Issue_description=table.Issue_description,
        Issue_Tags=table.Issue_Tags,
        isActive=table.isActive,
        uniqueID=table.uniqueID,
        User_id=UserModel.objects.get(username=request.user.username).id,
    )
    instance.save()
    return {HTTP_200_OK:"New issue was added"}


@issues.delete("/delete-issues")
def delete_an_issue(id: str):
    from Logic.models import Issues
    try:
        instance = Issues.objects.get(uniqueID=id)
        instance.delete()
        return {HTTP_202_ACCEPTED : f"{id} was deleted"}
    except Exception:
        return {HTTP_404_NOT_FOUND:"Image not added"}


@issues.post("/add-image")
def create_file(unique_id: str, file: UploadFile = File(...)):
    from Logic.models import Issues
    try:
        instance = Issues.objects.get(uniqueID = unique_id)
        instance.Issues_image = file.file.read()
        instance.save() #Images aren't being loaded on to POSTGRES
        return {HTTP_202_ACCEPTED:"New image was added."}
    except Exception:
        return {HTTP_404_NOT_FOUND:"Image not added"}


@issues.post("/post-linked-issue")
def post_a_linked_issue(issuesTable: IssueTable):
    from Logic.models import Issues, UserModel
    if len(Issues.objects.filter(uniqueID=issuesTable.LinkedIssue_id)):
        instance = Issues(
            Issue_Name=issuesTable.Issue_Name,
            Issue_description=issuesTable.Issue_description,
            Issue_Tags=issuesTable.Issue_Tags,
            isActive=issuesTable.isActive,
            uniqueID=issuesTable.uniqueID,
            User_id=UserModel.objects.get(Reg_no=issuesTable.User_id).id,
            LinkedIssue_id=Issues.objects.get(uniqueID=issuesTable.LinkedIssue_id).id,
        )
        instance.save()
        return {HTTP_200_OK:"New issue was saved."}

    else:
        return {HTTP_404_NOT_FOUND:"Instance not found"}

