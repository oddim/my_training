def send_email(message, recipient, *, sender = "university.help@gmail.com"):
    sends = [recipient, sender]
    permits = ['@', '.com', '.net', '.ru']
    n = 0
    s = 0
    for i in range(0, len(sends)):
        for j in range(0, len(permits)):
            if permits[j] in sends[i]:
                n = n + 1
    if not n == 4:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif sender == recipient and n == 4:
        print('Нельзя отправить письмо самому себе!')
    elif sender == "university.help@gmail.com" and n == 4:
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
    elif n == 4: # для двух эл. почт по 1 "@" и по 1 домену
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')

send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')

send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')





