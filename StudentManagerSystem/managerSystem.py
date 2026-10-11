from student import *
class StudentManager(object):
    def __init__(self):
        self.student_list = []

    def run(self):
        self.load_student()
        while True:
            self.show_menu()
            menu_num = int(input("请输入你需要的功能序号："))
            if menu_num == 1:
                self.add_student()
            elif menu_num == 2:
                self.del_student()
            elif menu_num == 3:
                self.modify_student()
            elif menu_num == 4:
                self.search_student()
            elif menu_num == 5:
                self.show_student()
            elif menu_num == 6:
                self.save_student()
            elif menu_num == 7:
                break

    @staticmethod
    def show_menu():
        print("请选择如下功能：")
        print("1:添加学员")
        print("2:删除学员")
        print("3:修改学员信息")
        print("4:查询学员信息")
        print("5:显示所以学员信息")
        print("6:保存学员信息")
        print("7:退出")



    def add_student(self):
        name = input("请输入您的姓名：")
        geder = input("请输入您的性别：")
        tel = input("请输入您的手机号：")
        student = Student(name, geder, tel)
        self.student_list.append(student)
        print(student)

    def del_student(self):
        del_name = input("请输入要删除的学生的姓名：")
        for i in self.student_list:
            if i.name == del_name:
                self.student_list.remove(i)
                break
        else:
            print("查无此人！")
        print(self.student_list)

    def modify_student(self):
        modify_name = input("请输入要修改的学员的姓名：")
        for i in self.student_list:
            if i.name == modify_name:
                i.name = input("请输入学员的姓名：")
                i.gender = input("请输入学员性别：")
                i.tel = input("请输入学员手机号：")
                print(f"修改该学员信息成功，姓名{i.name}，性别{i.gender}，手机号{i.tel}")
                break
        else:
            print("查无此人！")

    def search_student(self):
        search_name = input("请输入要查询的学员的姓名：")
        for i in self.student_list:
            if i.name == search_name:
                print(f"姓名{i.name}，性别{i.gender}，手机号{i.tel}")
                break
        else:
            print("查无此人！")

    def show_student(self):
        print("姓名\t性别\t手机号\t")
        for i in self.student_list:
            print(f"{i.name}\t{i.gender}\t{i.tel}")

    def save_student(self):
        f = open("student.data","w",encoding = "utf-8")
        new_list = [i.__dict__ for i in self.student_list]
        print(new_list)
        f.write(str(new_list))
        f.close()

    def load_student(self):
        try:
            f = open("student.data","r",encoding = "utf-8")
        except:
            f = open("student.data","w",encoding = "utf-8")
        else:
            data = f.read()
            new_list = eval(data)
            self.student_list = [Student(i["name"],i["gender"],i["tel"]) for i in new_list]
        finally:
            f.close()