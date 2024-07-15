# Разработай систему управления учетными записями пользователей для небольшой компании.
# Компания разделяет сотрудников на обычных работников и администраторов.
# У каждого сотрудника есть уникальный идентификатор (ID), имя и уровень доступа.
# Администраторы, помимо обычных данных пользователей, имеют дополнительный уровень доступа
# и могут добавлять или удалять пользователя из системы.
#
# Требования:1.Класс `User*: Этот класс должен инкапсулировать данные о пользователе:
# ID, имя и уровень доступа ('user' для обычных сотрудников).
# Класс Admin: Этот класс должен наследоваться от класса User.
# Добавь дополнительный атрибут уровня доступа, специфичный для администраторов ('admin').
# Класс должен также содержать методы add_user и remove_user,
# которые позволяют добавлять и удалять пользователей из списка
# (представь, что это просто список экземпляров User).


class User():
    def __init__(self, id, name, acs="user"):
        self.id = id
        self.name = name
        self.acs = acs

    def user_info(self):
        print(f"{self.name} {self.id} {self.acs}")



class Admin(User):
    def __init__(self, id, name, acs="user", admin_acs="admin"):
        super().__init__(id, name, acs)
        self.admin_acs = admin_acs
        self.acs = admin_acs
        self.users = []

    def add_user(self, user):
        self.users.append(user)
        print(f"Пользователь {user.name} добавлен")

    def del_user(self, user_id):
        user_to_remove = None
        for user in self.users:
            if user.id == user_id:
                user_to_remove = user
                break
        if user_to_remove:
            self.users.remove(user_to_remove)
            print(f"Пользователь {user_to_remove.name} удален")
        else:
            print(f"Пользователь {user_id} не найден")

    def list_users(self):
        for user in self.users:
            user.user_info()

# Создаем администратора
admin = Admin(id=1, name="Admin1")

# Создаем пользователей
user1 = User(id=2, name="User1")
user2 = User(id=3, name="User2")

# Администратор добавляет пользователей
admin.add_user(user1)
admin.add_user(user2)

# Выводим информацию о пользователях
admin.list_users()

# Администратор удаляет пользователя
admin.del_user(user_id=2)

# Выводим информацию о пользователях после удаления
admin.list_users()


