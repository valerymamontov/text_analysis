##Обработка текста:

###Датасет с сайта study.mokoron.com
###Тональный словарь Rusentilex 

Задача 1: из всей базы данных (17 млн.строк) выгрузить пять отдельных csv-файлов.  
Правила, по которым выгружаются файлы:  

1. смайлик и слово противоположной тональности к смайлику
2. содержат по крайней мере два слова противоположной тональности из словаря
3. с частицами «не» или «ни» и смайлик   
4. со смайликом, но нет оценочных слов
5. с двумя разными смайликами.

Для каждого пункта надо создать csv-файл, в котором лежит список исходных твитов (без предобработки) + то, что там нашлось (если два слова – то будет две колонки).  
Название csv-файла в зависимости от правила:
1. emoticon_token
2. two_tokens
3. not_token
4. emoticon_no_token
5. two_emoticons