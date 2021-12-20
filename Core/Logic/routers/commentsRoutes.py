from fastapi import Request, APIRouter
from pydantic.main import BaseModel
from starlette.status import HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_202_ACCEPTED


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
    from Logic.models import CommentsTable, UserModel
    instance = CommentsTable(
        uniqueID = comment.uniqueId,
        comment = comment.Comment,
        User_id = UserModel.objects.get(username = request.user.username).id,
        Reactions = comment.Reactions[0]
    )
    instance.save()
    return {HTTP_200_OK: "New comment was added."}

@comments.put("/edit-comment")
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

