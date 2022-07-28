from config import ADMINS

def is_admin(id_: int) -> bool:
    return id_ in ADMINS
 