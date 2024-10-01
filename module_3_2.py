
def send_email(message, recipient, *, sender="university.help@gmail.com"):
    q = "university.help@gmail.com"
    e = (".com", ".net", ".ru")
    t = "Невозможно отправить письмо с адреса " + sender + " на адрес " + recipient
    z=0
    if '@' in recipient and sender:
        for j in e:
           if j in recipient:
               z += 1
           if j in sender:
               z += 1
    else:
        print(t)
    if z <= 1:
        print(t)
    elif sender == recipient:
        print("Нельзя отправить письмо самому себе!")
    elif sender == q:
        print("Письмо успешно отправлено с адреса " + sender + " на адрес " + recipient)
    else:
        print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса " + sender + " на адрес " + recipient)

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')

