from resources.auth import *
from resources.profile import *

routes = (
    (RegisterResource, "/register"),
    (LoginResource, "/login"),
    (ProfileResource, "/profile"),
    (ProfileSearchResource, "/profile"),
)