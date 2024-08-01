def send_email(message, recipient, *,sender="university.help@gmail.com"):
    list_domain = [".com", ".ru", ".net"]

    is_at_recipient = recipient.count("@")
    is_at_sender = sender.count("@")

    recipient_lower = recipient.lower()
    sender_lower = sender.lower()

    recipient_sliced = recipient.split("@")[1]
    sender_sliced = sender.split("@")[1]

    valid_domain_recipient = any(ele in recipient_sliced for ele in list_domain)
    valid_domain_sender = any(ele in sender_sliced for ele in list_domain)

    domains_valid = valid_domain_sender == valid_domain_recipient
    emails_valid = is_at_recipient + is_at_sender
    validations = domains_valid and emails_valid == 2

    if not validations:
        print(f"Невозможно отправить письмо с адреса {sender_lower} на адрес {recipient_lower}")
    elif sender_lower == recipient_lower:
        print(f"Нельзя отправить письмо самому себе!")
    elif sender != "university.help@gmail.com":
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender_lower} на адрес {recipient_lower}.")
    else:
        print(f"Письмо успешно отправлено с адреса {sender_lower} на адрес {recipient_lower}.")
    return


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')


