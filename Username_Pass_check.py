class DuplicateUser(Exception):
  pass
class WeekPassword(Exception):
  pass
class User:
    user_name = set()
    
    def __init__(self, un, mob, pwd):
        self.un = un
        self.mob = mob
        self.pwd = pwd
        self.add_user()  # Call to add_user method
        self.validate()   # Call to validate method

    def add_user(self):
        if self.un in User.user_name:
            raise DuplicateUser ("User  already exists")
        else:
            User.user_name.add(self.un)

    def validate(self):
        uc = lc = num = sp = 0
        for i in self.pwd:
            if i.isupper():
                uc += 1
            elif i.islower():
                lc += 1
            elif i.isdigit():
                num += 1
            else:
                sp += 1
        if len(self.pwd) < 6 or uc == 0 or lc == 0 or num == 0 or sp == 0:
            raise WeekPassword("Password is weak")

def main():
    un = input("Enter the UserName:")
    mob = input("Enter the mob. no:")
    pwd = input("Enter the password:")
    try:
        u1 = User(un, mob, pwd)  # Create the user
    except DuplicateUser  as e:  # Correct exception handling
        print(e)
    except WeekPassword as e:
        print(e)
    else:
        print("Account created Successfully.")  # Corrected typo

main()