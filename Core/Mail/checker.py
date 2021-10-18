from typing import Optional, string
from types import Mail


def mail_checker(reg_no: string, mail: Optional[Mail]):
    email = reg_no.split("@")
    if reg_no[0:2] == email[0][-2:]:
        return True
