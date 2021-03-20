# Задание 7
# Представьте вы работаете в Банке, но Банк не работает по выходным.
# Если клиент захочет взять кредит в пятницу Вы должны сказать что сейчас это не возможно и вернуть ему время когда эта операция будет доступна.
# Пятницы выпали на 5, 12, 19, 26 числа.
# Если в дате которую введёт пользователь будет 5, 12, 19 или 26 число любого месяца вы должны вернуть ему дату в таком же формате как он и отправил.
# Напишите функцию которая спрашивает у пользователя дату в формате: ГГГГ-ММ-ДД ЧЧ:ММ
# 1. Если пользователь ввёл не верный формат Вы должны вернуть ему - "Неверный формат!"
# 2. Если пользователь всё ввёл верно верните ему дату которую он ввёл + 60 часов.
# 3. Можете использовать datetime module, можете использовать другие модули.
from datetime import date, timedelta
import time
def date():
    date_of_client=input('Введите дату (ГГГГ-ММ-ДД ЧЧ:ММ): ')
    try:
        valid_date=time.strptime(date_of_client, '%Y-%m-%d %H:%M')
        a=timedelta(hours=60)
        print (valid_date + a)
        
    except ValueError:
        print('Неверный формат!')
date()