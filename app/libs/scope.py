"""
Created on 2018/6/14 22:24

"""
__Author__ = '阿强'


class Scope:
    allow_api = []
    allow_module = []

    def __add__(self, other):
        self.allow_api = self.allow_api + other.allow_api
        self.allow_api = list(set(self.allow_api))

        self.allow_module = self.allow_module + other.allow_module
        self.allow_module = list(set(self.allow_module))
        return self


class AdminScope(Scope):
    # allow_api = ['v1.user+super_get_user', 'v1.user+super_delete_user']
    allow_module = ['v1.user']

    def __init__(self):
        pass
        # self + UserScope()


class UserScope(Scope):
    allow_api = ['v1.user+get_user', 'v1.user+delete_user']


def is_in_scope(scope, endpoint):
    scope = globals()[scope]()
    splits = endpoint.split('+')
    red_name = splits[0]
    if endpoint in scope.allow_api:
        return True
    if red_name in scope.allow_module:
        return True
    else:
        return False
