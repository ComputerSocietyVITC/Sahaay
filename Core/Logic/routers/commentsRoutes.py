from fastapi import Request, APIRouter
from pydantic.main import BaseModel
from starlette.status import HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_202_ACCEPTED
from .abstraction import Create_new_comment

class CommentsTable(BaseModel):
    Comment: str
    uniqueId: str
    Reactions: list[str]

class editComments(BaseModel):
    Comment: str
    Reactions: list[str]

comments = APIRouter()

@comments.get("/all-comments")
def fetch_all_users():
    from Logic.models import CommentsTable
    return list(CommentsTable.objects.all())

@comments.post("/new-comment")
def new_comment(request: Request, comment: CommentsTable):
    Create_new_comment(comment, request)
    return {HTTP_200_OK: "New comment was added."}

@comments.patch("/edit-comment")
def edit_comment(comments: editComments, request: Request, id: str):
    from Logic.models import CommentsTable
    try:
        instance = CommentsTable.objects.get(uniqueID = id)
        instance.comments = comments.Comment
        instance.reactions = comments.Reactions[0]
        instance.save()
        return  {HTTP_202_ACCEPTED : f"{id} was deleted"}
    except Exception:
        return {HTTP_404_NOT_FOUND:"Image not added"}

