## Description.
- Тестовый проект для собеседования в компанию Workmate.
- Главная фишка - медианная сумма трат на кофе по каждому студенту.

### С чего начать?

```yaml
git clone <URL>
```

Виртуалка (*Windows*).
```yaml
python -m venv venv
source venv/Scripts/activate
```
Обновление pip.
```yaml
python -m pip install --upgrade pip
```
Зависимости.
```yaml
pip install -r requirements.txt
```

Виртуалка (*Linux*).
```yaml
python3 -m venv venv
source venv/bin/activate
```
Обновление pip.
```yaml
python3 -m pip install --upgrade pip
```
Зависимости.
```yaml
pip install -r requirements.txt
```

## Нужные таблицы для теста уже в репе, поэтому
Для запуска скрипта:
```yaml
python main.py --files math.csv physics.csv programming.csv --report median-coffee
```

![Вывод скрипта](Code_NlHcxWiTNj.png)
