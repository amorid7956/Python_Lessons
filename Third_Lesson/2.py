def User_Data(**Key_args):
    print('Данные пользователя: ', Key_args)


u_data = input('Введите данные пользователя, разделённые пробелами в данном порядке'
               '(имя, фамилия, год рождения, город проживания, email, телефон): ').split()
try:
    User_Data(name=u_data[0], surname=u_data[1], year_birth=u_data[2],
              city=u_data[3], email=u_data[4], telephone=u_data[5])
except IndexError:
    print("Введите нужное количество аргументов.")
