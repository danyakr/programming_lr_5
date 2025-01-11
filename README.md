# Currency Fetcher

## Описание проекта

### Основные функции:
1. **Запрос курсов валют**: С помощью API ЦБ РФ скрипт получает XML-данные и парсит их для извлечения информации о валютах.
2. **Хранение данных**: Курсы валют сохраняются в структуре `defaultdict`, чтобы обеспечить удобный доступ к информации по коду валюты.
3. **Визуализация**: Данные о курсах валют могут быть визуализированы в виде столбчатой диаграммы.
4. **Шаблон "Одиночка"**: Реализован для управления экземплярами класса `CurrencyFetcher`.

### Используемые технологии:
- **Python** для работы с API, обработки данных и создания визуализаций.
- **Модули**:
  - `requests` — для HTTP-запросов.
  - `xml.etree.ElementTree` — для обработки XML.
  - `matplotlib` — для построения графиков.
  - `collections.defaultdict` — для упрощенного управления данными.
 
1. **Запрос курсов валют**:
   ```python
   fetcher = CurrencyFetcher()
   result = fetcher.fetch_currencies(['R01235', 'R01239', 'R01820'])
   print(result)
   ```
   Вывод:
   ```
   [{'USD': ('Доллар США', ('74', '50'))}, {'EUR': ('Евро', ('79', '30'))}, {'JPY': ('Японская иена', ('0', '67'))}]
   ```

2. **Получение информации о валюте**:
   ```python
   print(fetcher.get_currency_info('USD'))
   ```
   Вывод:
   ```
   ('Доллар США', ('74', '50'), 1)
   ```

3. **Визуализация данных**:
   ```python
   fetcher.visualize_currencies()
   ```
   Программа сохранит график в файл `currencies.jpg` и отобразит его.

   ## Ограничения
- Для предотвращения частых запросов предусмотрена защита через параметр `cooldown`. По умолчанию минимальный интервал между запросами составляет 1 секунду.

![image](https://github.com/user-attachments/assets/c0089959-a018-4f0b-81aa-2bdb88fc113e)

![image](https://github.com/user-attachments/assets/1f1bb3e9-1802-4606-bfca-f386dd91f402)



Запуск тестов


![image](https://github.com/user-attachments/assets/7cb9ab76-dbf9-4b01-a827-bf9e6952743b)


