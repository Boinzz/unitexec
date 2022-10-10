# -*- coding: utf-8 -*-
from curses.ascii import isdigit
import re
from typing import Dict


def register_params_check(content):
    """
    TODO: 进行参数检查
    """
    if "username" in content.keys(): #content["username"] is None:
        if not re.match(r'^(((?<![0-9])[A-Za-z])|([0-9](?![A-Za-z]))){5,12}$', content["username"]):
            return "error: username", False
    else:
        return "username", False
    
    if "password" in content.keys():
        if not re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[*-^_])[A-Za-z\d*-^_]{8,15}$', content["password"]):
            return "error: password", False
    else:
        return "password", False
    
    if "nickname" not in content.keys():
        return "nickname", False

    if "url" in content.keys():
        if not re.match(r'^(?=(^https?://(.{0,48})$))https?://((?!-)[A-Za-z0-9-]{1,63}(?<!-)\.)+((?!-)[A-Za-z0-9-]{1,63}(?<!-))+([0-9](?![0-9]*$)|[A-Za-z])([A-Za-z0-9]|-(?!$))*$', content["url"]):
            return "error: url", False
    else:
        return "url", False

    if "mobile" in content.keys():
        if not re.match(r'^\+\d{2}\.\d{12}$', content["mobile"]):
            return "error: mobile", False
    else:
        return "mobile", False

    if "magic_number" in content.keys():
        if not content["magic_number"].isdigit():
            return "error: magic_number", False
    else:
        content["magic_number"] = '0'
        return "magic_number", False
    
    return "ok", True
