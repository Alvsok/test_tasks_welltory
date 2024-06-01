# Этот репозиторий ответ на задачу на позицию Python Developer №2

## Нужно было переписать модели сделав их код более эффективным, читаемым и безопасным и написать функции query_users и query_for_user

В репозитории представлены улучшенные модели в файле [models.py](https://github.com/Alvsok/test_tasks_welltory/blob/main/src/models.py) и реализация функций `query_users` и `query_for_user` в файле [utils.py](https://github.com/Alvsok/test_tasks_welltory/blob/main/src/utils.py).

# Иллюстрация работы кода

В в тестовую БД внесены следующие данные:

## Таблица `users`

| id  | name          | gender | age |
|-----|---------------|--------|-----|
| 1   | John Doe      | Male   | 30  |
| 2   | Jane Smith    | Female | 25  |
| 3   | Mike Brown    | Male   | 40  |
| 4   | Emily Davis   | Female | 35  |
| 5   | Laura Johnson | Female | 50  |

## Таблица `heart_rates`

| id  | user_id | timestamp                 | heart_rate |
|-----|---------|---------------------------|------------|
| 1   | 1       | 2024-05-30 22:22:00.785219| 60.5       |
| 2   | 1       | 2024-05-29 21:22:00.785229| 61.2       |
| 3   | 1       | 2024-05-28 20:22:00.785232| 62.1       |
| 4   | 2       | 2024-05-30 21:22:00.785831| 70.5       |
| 5   | 2       | 2024-05-29 20:22:00.785838| 71.3       |
| 6   | 2       | 2024-05-28 19:22:00.78584 | 72.7       |
| 7   | 3       | 2024-05-30 20:22:00.786351| 80.5       |
| 8   | 3       | 2024-05-29 19:22:00.786357| 81.6       |
| 9   | 3       | 2024-05-28 18:22:00.786359| 82.4       |
| 10  | 4       | 2024-05-30 19:22:00.787056| 90.5       |
| 11  | 4       | 2024-05-29 18:22:00.787064| 91.8       |
| 12  | 4       | 2024-05-28 17:22:00.787065| 92.6       |
| 13  | 5       | 2024-05-30 18:22:00.78778 | 100.5      |
| 14  | 5       | 2024-05-29 17:22:00.787786| 101.9      |
| 15  | 5       | 2024-05-28 16:22:00.787788| 102.8      |

# Результаты работы функций

## Функция `query_users`

### Test: Female users older than 30 with average heart rate above 70 in the last 30 days
- User: Emily Davis, Age: 35, Gender: Female
- User: Laura Johnson, Age: 50, Gender: Female

### Test: Male users older than 25 with average heart rate above 60 in the last 7 days
- User: John Doe, Age: 30, Gender: Male
- User: Mike Brown, Age: 40, Gender: Male

### Test: Female users older than 20 with average heart rate above 65 in the last 15 days
- User: Jane Smith, Age: 25, Gender: Female
- User: Emily Davis, Age: 35, Gender: Female
- User: Laura Johnson, Age: 50, Gender: Female

### Test: Male users older than 35 with average heart rate above 75 in the last 10 days
- User: Mike Brown, Age: 40, Gender: Male

## Функция `query_for_user`

### Test: Top 10 highest average heart rates for user 1 in the last 7 days
- Hour: 20, Avg Heart Rate: 62.1
- Hour: 21, Avg Heart Rate: 61.2
- Hour: 22, Avg Heart Rate: 60.5

### Test: Top 10 highest average heart rates for user 2 in the last 7 days
- Hour: 19, Avg Heart Rate: 72.7
- Hour: 20, Avg Heart Rate: 71.3
- Hour: 21, Avg Heart Rate: 70.5

### Test: Top 10 highest average heart rates for user 3 in the last 7 days
- Hour: 18, Avg Heart Rate: 82.4
- Hour: 19, Avg Heart Rate: 81.6
- Hour: 20, Avg Heart Rate: 80.5

### Test: Top 10 highest average heart rates for user 4 in the last 7 days
- Hour: 17, Avg Heart Rate: 92.6
- Hour: 18, Avg Heart Rate: 91.8
- Hour: 19, Avg Heart Rate: 90.5

### Test: Top 10 highest average heart rates for user 5 in the last 7 days
- Hour: 16, Avg Heart Rate: 102.8
- Hour: 17, Avg Heart Rate: 101.9
- Hour: 18, Avg Heart Rate: 100.5

# Исходное задание:

## Контекст
У вас есть код для выполнения запросов в базу данных с использованием sqlalchemy-core. Ваша задача — дописать запросы в функциях и максимально улучшить уже написанный код.

## Что надо сделать
* Улучшить текущий код, представленный в разделе [Пример кода](https://gist.github.com/mariia-m1/d54109f220a52963b2450c0c5075aeac#%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D1%80-%D0%BA%D0%BE%D0%B4%D0%B0) сделав его более эффективным, читаемым и безопасным
* Заменить комментарии в функциях на соответствующие SQL запросы.

## Пример кода
``` python
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float, DateTime, ForeignKey

engine = create_engine('postgresql://username:password@host:port/database_name')
metadata = MetaData()

users = Table(
    'users',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('gender', String),
    Column('age', String)
)

heart_rates = Table(
    'heart_rates',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('user_id', Integer, ForeignKey('users.id'), index=True),
    Column('timestamp', DateTime),
    Column('heart_rate', Float),
)

metadata.create_all(engine)

def query_users(min_age, gender, min_avg_heart_rate, date_from, date_to):
    # Напишите здесь запрос, который возвращает всех пользователей, которые старше'min_age' и 
    # имеют средний пульс выше, чем 'min_avg_heart_rate', на определенном промежутке времени
        # min_age: минимальный возраст пользователей
        # gender: пол пользователей
        # min_avg_heart_rate: минимальный средний пульс
        # date_from: начало временного промежутка
        # date_to: конец временного промежутка
    return
    
def query_for_user(user_id, date_from, date_to):
    # Напишите здесь запрос, который возвращает топ 10 самых высоких средних показателей 'heart_rate' 
    # за часовые промежутки в указанном периоде 'date_from' и 'date_to'
        # user_id: ID пользователя
        # date_from: начало временного промежутка
        # date_to: конец временного промежутка
    return
```
## Ожидаемый результат
* Подготовьте файл с кодом в удобном для вас формате, где будет ясно видно выполнение всех требований ТЗ и правильная работа кода.
* После завершения подготовки файла отправьте его на **ту же почту**, откуда вам пришел запрос на выполнение тестового задания.

## FAQ
### Что делать, если есть вопросы
Если наш ответ критически важен для принятия решения, то есть без него вы не можете продолжить следующий шаг, напишите на **ту почту**, откуда вам пришел запрос на выполнение тестового задания. В остальных случаях, пожалуйста, используйте имеющуюся информацию.

### Что мы будем оценивать
* Умение разобраться и предложить оптимальное решение.

### Время и срок выполнения задания
Ориентировочное время выполнения: мы предполагаем, что вы не потратите на это задание больше 30–60 минут.

Срок выполнения задачи составляет 5 рабочих дней: отсчет времени начинается на следующий день после получения вами задания. Если по каким-то причинам вы не можете выполнить тестовое задание в установленный срок, пожалуйста, сообщите об этом, написав на **ту почту**, откуда вам пришел запрос, указав, когда мы можем ожидать готовое задание.