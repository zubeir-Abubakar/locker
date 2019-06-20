import random 
class Password:

    password_list = []

    def __init__(self,smedia,first_name,last_name,user_name,password):
        
        self.smedia = smedia
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.password = password

    def save_password(self):
            Password.password_list.append(self)

    def delete_passwords(self):
            Password.password_list.remove(self)

    @classmethod
    def generate_password(cls):
        chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456'
        new_password = ''.join(random.sample(chars, 6))
        return new_password


    @classmethod
    def display_passwords(cls):
        return cls.password_list