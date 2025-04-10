import json
class Mysqldatabase:
    def __init__(self):
        self.user=json.loads(open('./user.json',mode='r',encoding="utf8").read())
        self.student=json.loads(open('./student.json',mode='r',encoding="utf8").read())
    def check_login(self,username,password):

        for user in self.user:
            if username == user["username"]:
                if password == user["password"]:
                    return True,"登录成功"
                else:
                    return False,"密码错误"
            else:
                return False, "用户不存在"
    def all(self):
        return self.student

    def insert(self,student):
        self.student.append(student)

    def delete_by_name(self,name):
        for i in self.student:
            if i['name'] == name:
                self.student.remove(i)
                # print(i)
                return True,"删除成功"
        return  False,"用户不存在"

    def serach_name(self,name):
        for i in self.student:
            if i['name']==name:
                 pass
            else:
                return False,"该姓名不存在"

    def updata_by_stu(self,name,math,chinese,english):
        for i in self.student:
            print(i["name"] )
            if i["name"]==name:
                i["math"]=math
                i["math"]=chinese
                i["english"]=english
                return True,"修改成功"
        return False,"用户不存在"

db=Mysqldatabase()
if __name__ == '__main__':
    # print(db.check_login("admin","123456"))
    print(db.delete_by_name("张三1"))