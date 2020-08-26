roles = ["Super Admin", "Admin", "Editor"]

class User:
    def __init__(self, _name, _surname, _username, _role):
        self.name = _name
        self.surname = _surname
        self.username = _username
        self.role = _role

Farid = User("Farid", "Ahmad", "ahmadf", roles[0])
Samir = User("Samir", "Karimov", "karimovs", roles[1])
Ehmed = User("Ehmed", "Memmedov", "memmedove", roles[2])
Memmed = User("Memmed", "Qurbanov", "qurbanovm", roles[2])
Yasin = User("Yasin", "Ugur", "ugury", roles[2])

users = [Farid, Samir, Ehmed, Memmed, Yasin]

# admin selayiyyetli user her iki vezifeni icra ede biler
# editor selahiyyetli user sadece vezifeIkini icra ede biler
def vezifeBir():
    return f"{vezifeBir.__name__} vezifesini sadece Super Admin icra edebiler"

def vezifeIki():
    return f"{vezifeIki.__name__} vezifesini sadece Super Admin ve Admin icra edebiler"

def vezifeUc():
    return f"{vezifeUc.__name__} vezifesini sadece Super Admin, Admin ve Editor icra edebiler"

def vezifeDort():
    return f"{vezifeDort.__name__} vezifesini sadece Super Admin, Admin ve Editor icra edebiler"

def vezifeBes():
    return f"{vezifeBes.__name__} vezifesini sadece Super Admin, Admin ve Editor icra edebiler"




selahiyyetler = {
    'Super Admin': [vezifeBir(), vezifeIki(), vezifeUc(), vezifeDort(), vezifeBes()],
    'Admin': [vezifeIki(), vezifeUc(), vezifeDort(), vezifeBes()],
    'Editor': [vezifeUc(), vezifeDort(), vezifeBes()]
}


def vezifeleriTap(_role):
    for selahiyyet, vezife in selahiyyetler.items():
        if selahiyyet == _role:
            print(f"{username} {_role}-dir ve asagidaki selahiyyetlere sahibdir:")
            for v in vezife:
                print(v)


def vezifeleriYoxla(_role, _vezife):
    for selahiyyet, vezife in selahiyyetler.items():
        if _role == selahiyyet:
            for v in vezife:
                if v == _vezife:
                    print(f"{_role} selahiyyetinin {_vezife}-si var")
                    break
                else:
                    print("Teyinat tapilmadi")


username = input("Username daxil edin:")

finder = False
for user in users:
    if username == user.username:
        vezifeleriTap(user.role)
        finder = True
        break
if finder == False:
 print(f"{username} adında istifadeci yoxdur")






# 5 dene is teyin edin (funksiya)
# 3 ferqli selahiyyet teyin eliyin (SuperAdmin,admin,editor)
# vezifeler superadmin terefinden teyin olunmalidir
