__all__ = ["user_router", "admin_router", "issue_router", "comment_router"]
from .user_routes import user_router as user_router
from .admin_routes import admin as admin_router
from .issues_routes import issues as issue_router
from .commentsRoutes import comments as comment_router