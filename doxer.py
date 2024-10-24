__version__ = (1, 1, 2)

#            © Copyright 2024
#           https://t.me/HikkTutor 
# 🔒      Licensed under the GNU AGPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html
#┏┓━┏┓━━┏┓━━┏┓━━┏━━━━┓━━━━━┏┓━━━━━━━━━━━━
#┃┃━┃┃━━┃┃━━┃┃━━┃┏┓┏┓┃━━━━┏┛┗┓━━━━━━━━━━━
#┃┗━┛┃┏┓┃┃┏┓┃┃┏┓┗┛┃┃┗┛┏┓┏┓┗┓┏┛┏━━┓┏━┓━━━━
#┃┏━┓┃┣┫┃┗┛┛┃┗┛┛━━┃┃━━┃┃┃┃━┃┃━┃┏┓┃┃┏┛━━━━
#┃┃━┃┃┃┃┃┏┓┓┃┏┓┓━┏┛┗┓━┃┗┛┃━┃┗┓┃┗┛┃┃┃━━━━━
#┗┛━┗┛┗┛┗┛┗┛┗┛┗┛━┗━━┛━┗━━┛━┗━┛┗━━┛┗┛━━━━━
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# load from: t.me:HikkTutor 
# meta developer:@HikkTutor 
# meta banner:https://t.me/HikkTutor
# name: Doxer 
from .. import loader, utils
import random
import asyncio
from telethon.tl.types import User

@loader.tds
class DoxerModule(loader.Module):
    """Модуль для фейк-доксинга пользователей чата
    
    Модуль полностью рандомный, все совпадения случайны"""
    strings = {'name': 'Doxer'}

    def __init__(self):
        self.is_doxing = False 

    async def doxcmd(self, message):
        """- Пробить пользователя в базе"""
        if self.is_doxing:
            await message.edit("<b>Доксинг уже выполняется. Пожалуйста, дождитесь завершения.</b>")
            return

        self.is_doxing = True 
        replied_message = None

        try:
            if message.reply_to_msg_id:
                replied_message = await message.get_reply_message()
                user = await message.client.get_entity(replied_message.from_id) 
                
                if isinstance(user, User):
                    if user.bot:
                        await message.edit(f"<b><a href='tg://user?id={user.id}'>{user.first_name}</a> является ботом, я могу доксить только людей.</b>")
                        return
                else:
                    channel_link = f"<a href='https://t.me/{replied_message.sender.username}'>{replied_message.sender.title}</a>" if replied_message.sender.username else replied_message.sender.title
                    await message.edit(f"<b>{channel_link} является каналом, я могу доксить только людей.</b>")
                    return
            else:
                command_text = message.raw_text.split(' ', 1)
                if len(command_text) > 1 and ('@' in command_text[1] or any(char.isdigit() for char in command_text[1])):
                    await message.edit("<b>Это пока не доступно, используйте докс через ответ на сообщение.</b>")
                    return
                await message.edit("<b>Вы забыли ответить на сообщение.</b>")
                return

            user_id = user.id if hasattr(user, 'id') else user 

            if user_id == message.from_id:
                await message.edit("<b>Вы не можете доксить себя.</b>")
                return

            await message.edit("<b>Запуск доксинга...</b>")
            await asyncio.sleep(2)

            progress_steps = random.sample(range(10, 101, 10), 5)
            for step in sorted(progress_steps):
                await message.edit(f"<b>Собираю данные...</b> [{'■' * (step // 10)}{'□' * (10 - step // 10)}] {step}%")
                await asyncio.sleep(1)

            await message.edit("<b>Вывожу...</b>")

            male_names = ["Александр", "Дмитрий", "Иван", "Максим", "Артем", "Сергей", "Юрий", "Роман", "Виталий", "Денис", "Алексей", "Владислав", "Никита", "Станислав", "Егор", "Федор", "Денис", "Антон", "Григорий", "Семен", "Павел", "Игорь", "Роман", "Анатолий", "Кирилл", "Даниил", "Ярослав", "Рустам", "Алексей", "Виктор", "Илья"]
            female_names = ["Мария", "Анна", "Екатерина", "Ольга", "Наталья", "Елена", "Татьяна", "Анастасия", "Дарья", "Ксения", "Светлана", "Ирина", "Людмила", "София", "Виктория", "Алёна", "Кристина", "Евгения", "Полина", "Маргарита", "Надежда", "Светлана", "Тамара", "Галина", "Анастасия", "Яна", "Зоя", "Элеонора", "Снежана", "Римма"]

            male_surnames = ["Смирнов", "Иванов", "Кузнецов", "Попов", "Соколов", "Лебедев", "Ковалев", "Петров", "Николаев", "Романов", "Федоров", "Алексеев", "Морозов", "Степанов", "Сидоров", "Козлов", "Тихонов", "Беляев", "Громов", "Яковлев"]
            female_surnames = ["Смирнова", "Иванова", "Кузнецова", "Попова", "Соколова", "Лебедева", "Ковалёва", "Петрова", "Николаева", "Романова", "Федорова", "Алексеева", "Морозова", "Степанова", "Сидорова", "Козлова", "Тихонова", "Беляева", "Громова", "Яковлева"]

            male_patronymics = ["Александрович", "Дмитриевич", "Иванович", "Максимович", "Артемович", "Сергеевич", "Юрьевич", "Романович", "Витальевич", "Денисович", "Никитич", "Станиславович", "Егорович", "Федорович", "Павлович", "Игоревич"]
            female_patronymics = ["Александровна", "Дмитриевна", "Ивановна", "Максимовна", "Артемовна", "Сергеевна", "Юрьевна", "Романовна", "Витальевна", "Денисовна", "Никитична", "Станиславовна", "Егоровна", "Федоровна", "Павловна", "Игоревна"]

            random_name = random.choice(male_names + female_names)
            if random_name in male_names:
                random_surname = random.choice(male_surnames)
                random_patronymic = random.choice(male_patronymics)
            else:
                random_surname = random.choice(female_surnames)
                random_patronymic = random.choice(female_patronymics)

            random_city = random.choice([
                "Москва", "Санкт-Петербург", "Казань", "Новосибирск", "Екатеринбург", "Минск", 
                "Алматы", "Ташкент", "Бишкек", "Астана", "Челябинск", "Саратов", "Нижний Новгород", 
                "Ростов-на-Дону", "Брест", "Волгоград", "Уфа", "Киев", "Молдова", "Томск", "Красноярск", 
                "Ижевск", "Тула", "Курск", "Самара", "Сочи", "Воронеж", "Омск", "Ставрополь", 
                "Ярославль", "Пенза", "Калуга", "Тверь", "Псков", "Орлов", "Таганрог", "Липецк", 
                "Симферополь", "Брянск", "Калининград", "Набережные Челны", "Астрахань", 
                "Черкесск", "Владикавказ", "Грозный", "Нальчик", "Петрозаводск", "Сыктывкар", 
                "Саранск", "Улан-Удэ", "Иркутск", "Душанбе", "Ереван", "Баку", "Чебоксары", 
                "Кострома", "Сыктывкар", "Набережные Челны", "Туапсе", "Алатырь", "Киров", 
                "Магнитогорск", "Таганрог", "Стерлитамак", "Салават", "Уфа", "Лермонтов", 
                "Симферополь", "Саров", "Нижневартовск", "Ставрополь", "Грозный"
            ])
            
            random_ip = f"192.168.{random.randint(0, 255)}.{random.randint(0, 255)}"
            random_phone = f"+7 (999) {random.randint(100, 999)}-{random.randint(1000, 9999)}"
            funny_nickname = random.choice([
                "Душнила", "Сёмга", "Дед инсульт", "Спамщик", "Мегачорт", "Мошенник", 
                "Бронированный вафельный стаканчик", "Чудо в перьях", "Агрессивный баклажан", 
                "Магический пердёж", "Сморщенный кусочек не понятно чего", "Дед-скуфик", 
                "Трисися", "Сиська потного индейца", "Тумбочка", "Капитан очевидность", 
                "Грозный метр с кепкой", "Диктатор", "Солевой магнат", 
                "Дилер", "Очередной Гений", "Пенсионер"
            ])

            user_rating = random.randint(1, 10)

            await asyncio.sleep(2)

            if replied_message:
                await message.edit(
                    f"<b>Вот всё что я нашел про {replied_message.sender.first_name}:</b>\n"
                    f"<b>ФИО:</b> <code>{random_name} {random_surname} {random_patronymic}</code>\n"
                    f"<b>Город:</b> <code>{random_city}</code>\n"
                    f"<b>IP-адрес:</b> <code>{random_ip}</code>\n"
                    f"<b>Телефон:</b> <code>{random_phone}</code>\n"
                    f"<b>Прозвище:</b> <code>{funny_nickname}</code>\n\n"
                    f"<b>ID:</b> <code>{user_id}</code>\n"
                    f"<b>Юзернейм:</b> <code>@{replied_message.sender.username or 'не указан, или не удалось найти'}</code>\n"
                    f"<b>Рейтинг:</b> <code>{user_rating}/10</code>"
                )
            else:
                await message.edit("<b>Не удалось получить информацию о пользователе.</b>")
        finally:
            self.is_doxing = False
