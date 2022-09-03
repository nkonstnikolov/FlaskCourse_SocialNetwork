from resources.auth import *
from resources.profile import *
from resources.message import *

routes = (
    (RegisterResource, "/register"), #POST
    (LoginResource, "/login"), #POST
    (LogoutResource, "/logout"), #POST
    (DeleteAccountResource, "/delete"), #DELETE
    (ProfileResource, "/profile"), #POST
    (ProfileSearchResource, "/profile"), #GET
    (ProfileEditResource, "/profile"), #PUT
    (SendMessageResource, "/message"), #POST
    (InboxResource, "/inbox"), #GET
)