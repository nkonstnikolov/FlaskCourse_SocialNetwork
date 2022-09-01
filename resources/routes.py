from resources.auth import *
from resources.profile import *
from resources.message import *

routes = (
    (RegisterResource, "/register"),
    (LoginResource, "/login"),
    (ProfileResource, "/profile"),
    (ProfileSearchResource, "/profile"),
    (SendMessageResource, "/message"),
    (InboxResource, "/inbox"),
)