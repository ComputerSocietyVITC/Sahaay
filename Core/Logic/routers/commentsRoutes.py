from fastapi import Request, APIRouter
from pydantic.main import BaseModel
from starlette.status import HTTP_200_OK, HTTP_404_NOT_FOUND


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
    return f"New Comment was made! HTTP {HTTP_200_OK}"

@comments.put("/edit-comment")
def edit_comment(comments: editComments, request: Request, id: str):
    from Logic.models import CommentsTable
    try:
        instance = CommentsTable.objects.get(uniqueID = id)
        instance.comments = comments.Comment
        instance.reactions = comments.Reactions[0]
        instance.save()
        return f"Instance was saved! HTTP {HTTP_200_OK}"
    except Exception:
        return f"Instance not found! HTTP {HTTP_404_NOT_FOUND}"

