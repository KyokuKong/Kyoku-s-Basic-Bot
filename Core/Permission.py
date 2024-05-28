import json
import os.path


class Permission:
    def __init__(self):
        self.SUPERUSER = []
        self.OPERATER = []
        self.TESTER = []

        self.SUPERGROUP = []
        self.SPECIALGROUP = []
        self.TESTGROUP = []

        self.user_perm_map = {
            "SUPERUSER": 3,
            "OPERATER": 2,
            "TESTER": 1
        }

        self.group_perm_map = {
            "SUPERGROUP": 3,
            "SPECIALGROUP": 2,
            "TESTGROUP": 1
        }

        # 初始化权限
        if not os.path.exists("permission.json"):
            self.save_perm_to_json()

        self.read_perm_from_json()

    def save_perm_to_json(self):
        with open("permission.json", 'w+', encoding="utf-8") as j:
            perm_dict = {
                "user": {
                    "SUPERUSER": self.SUPERUSER,
                    "OPERATER": self.OPERATER,
                    "TESTER": self.TESTER
                },
                "group": {
                    "SUPERGROUP": self.SUPERGROUP,
                    "SPECIALGROUP": self.SPECIALGROUP,
                    "TESTGROUP": self.TESTGROUP
                }
            }
            json.dump(perm_dict, j, ensure_ascii=False, indent=4)
            j.close()

    def read_perm_from_json(self):
        with open("permission.json", 'r', encoding="utf-8") as j:
            perm_dict = json.load(j)
            self.SUPERUSER = perm_dict["user"]["SUPERUSER"]
            self.OPERATER = perm_dict["user"]["OPERATER"]
            self.TESTER = perm_dict["user"]["TESTER"]
            self.SUPERGROUP = perm_dict["group"]["SUPERGROUP"]
            self.SPECIALGROUP = perm_dict["group"]["SPECIALGROUP"]
            self.TESTGROUP = perm_dict["group"]["TESTGROUP"]
            j.close()

    def get_permission_by_qqid(self, qqid: int) -> int:
        # 获取满足条件的权限等级
        perm_values = (value for key, value in self.user_perm_map.items() if qqid in getattr(self, key))
        # 返回最大权限等级，如果没有结果则返回0
        return max(perm_values, default=0)

    def get_permission_by_groupid(self, groupid: int) -> int:

        # 获取满足条件的权限等级
        perm_values = (value for key, value in self.group_perm_map.items() if groupid in getattr(self, key))
        # 返回最大权限等级，如果没有结果则返回0
        return max(perm_values, default=0)

    def is_permission(self, uid: int, utype: int, perm: int) -> bool:
        """
        判断用户所属的权限值是否满足要求，满足返回True，否则返回False
        :param uid: QqId或GroupId
        :param utype: 用户类型，0为QqId，1为GroupId
        :param perm: 目标权限值
        :return: 布尔值
        """
        if utype == 0:
            return self.get_permission_by_qqid(uid) >= perm
        elif utype == 1:
            return self.get_permission_by_groupid(uid) >= perm
        else:
            return False

    def add_user_perm(self, qqid: int, perm: str) -> bool:
        """
        添加用户权限
        :param qqid: qq号
        :param perm: 权限等级（字符串）
        :return: 布尔值
        """
        if perm in self.user_perm_map:
            getattr(self, perm).append(qqid)
            self.save_perm_to_json()
            return True
        else:
            return False

    def add_group_perm(self, groupid: int, perm: str) -> bool:
        """
        添加群组权限
        :param groupid: 群号
        :param perm: 权限等级（字符串）
        :return: 布尔值
        """
        if perm in self.group_perm_map:
            getattr(self, perm).append(groupid)
            self.save_perm_to_json()
            return True
        else:
            return False

    def del_user_perm(self, qqid: int, perm: str | int) -> bool:
        """
        删除用户权限
        :param qqid: qq号
        :param perm: 权限等级（字符串）
        :return: 布尔值
        """
        if perm in self.user_perm_map:
            getattr(self, perm).remove(qqid)
            self.save_perm_to_json()
            return True
        else:
            return False

    def del_group_perm(self, groupid: int, perm: str) -> bool:
        """
        删除群组权限
        :param groupid: 群号
        :param perm: 权限等级（字符串）
        :return: 布尔值
        """
        if perm in self.group_perm_map:
            getattr(self, perm).remove(groupid)
            self.save_perm_to_json()
            return True
        else:
            return False

    def update_permission(self):
        self.read_perm_from_json()
        return True


# 单例模式
perms = Permission()
