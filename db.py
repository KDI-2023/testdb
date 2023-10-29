import os
import json
from copy import deepcopy as dcp
from .const import *

dirname = os.path.dirname(os.path.abspath(os.path.expanduser(__file__)))

data = json.loads(open(os.path.join(dirname, 'uuid_all.json'), 'rb').read())
alias = json.loads(open(os.path.join(dirname, 'alias.json'), 'rb').read())


def unknown(s: str) -> dict:
    return {
        UID: s,
        ALIAS: list(),
        TYPE: UNKNOWN,
        LINK: dict(),
    }


def get_info(s: str) -> str:
    return dcp(data.get(s, unknown(s)))


def get_linked(s: str) -> str:
    ans = dcp(data.get(s, unknown(s)))
    ans[LINK] = {i: [get_info(k) for k in ans[LINK][i]] for i in ans[LINK]}
    return ans


def s_uid(s: str) -> list:
    ans = list()
    for i in alias:
        if s in i:
            ans += alias[i]
    return list(set(ans))


def s_linked(s: str) -> dict:
    return {i: get_linked(i) for i in s_uid(s)}


def unknown(s: str) -> dict:
    return {
        UID: s,
        ALIAS: list(),
        TYPE: UNKNOWN,
        LINK: dict(),
    }


def get_info(s: str) -> str:
    return dcp(data.get(s, unknown(s)))


def get_linked(s: str) -> str:
    ans = dcp(data.get(s, unknown(s)))
    ans[LINK] = {i: [get_info(k) for k in ans[LINK][i]] for i in ans[LINK]}
    return ans


def s_uid(s: str) -> list:
    ans = list()
    for i in alias:
        if s in i:
            ans += alias[i]
    return list(set(ans))


def s_linked(s: str) -> dict:
    return {i: get_linked(i) for i in s_uid(s)}
