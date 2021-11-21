from typing import Optional,List
from pydantic import BaseModel,EmailStr
from fastapi import Request

class PydanticUserModel(BaseModel):
    password: str
    username: str
    first_name: str
    last_name: str
    email: EmailStr
    Reg_no: str

def patch_user_model(pseudouser, user: Optional[PydanticUserModel]):
    pseudouser.first_name = user.first_name
    pseudouser.last_name = user.last_name
    pseudouser.email = user.email
    pseudouser.username = user.username
    pseudouser.set_password(user.password)
    pseudouser.save()

def create_user_model(user: Optional[PydanticUserModel]):
    from Logic.models import UserModel
    pseudouser = UserModel(
            username=user.username,
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
            Reg_no=user.Reg_no,
        )
    pseudouser.set_password(user.password)
    pseudouser.save()

# End of User Models

class IssueTable(BaseModel):
    Issue_Name: str
    Issue_Tags: List[str]
    Issue_description: str
    isActive: bool
    uniqueID: str
    LinkedIssue_id: str
    User_id: str

class IssueTableNew(BaseModel):
    Issue_Name: str
    Issue_Tags: List[str]
    Issue_description: str
    isActive: bool
    uniqueID: str
    User_Id: str

def create_new_issue(request:Request,   table: Optional[IssueTableNew]):
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

def create_linked_issue(issuesTable: Optional[IssueTable]):
    from Logic.models import Issues, UserModel
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

##Comments
class CommentsTable(BaseModel):
    Comment: str
    uniqueId: str
    Reactions: list[str]

def Create_new_comment(request:Request, comment: Optional[CommentsTable]):
    from Logic.models import CommentsTable, UserModel
    instance = CommentsTable(
        uniqueID = comment.uniqueId,
        comment = comment.Comment,
        User_id = UserModel.objects.get(username = request.user.username).id,
        Reactions = comment.Reactions[0]
    )
    instance.save()