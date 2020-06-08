### Описание
Selenium-тест покрывающий следующие два кейса:

ТК01:  
- Открыть сайт https://itmegastar.com/;  
- Перейти на страницу “Команда”;  
-  Проверьте наличие текста на странице “Семён Якушев”.

ТК02:    
* Открыть сайт https://itmegastar.com/;  
* Перейти на страницу “Контакты;  
* Перевести курсор в блоке «Напишите нам» на поле «Имя»;  
* Ввести своем имя.
         
### Требования:

[Python](https://www.python.org/) версии 3.8 или выше  
[tox](https://tox.readthedocs.io/en/latest/)  
[google chrome](https://www.google.com/chrome/) или chromium
[chromedriver](https://chromedriver.chromium.org/) соответствующей версии путь до которого прописан в переменной PATH  
[allure-commandline](https://docs.qameta.io/allure/#_installing_a_commandline) для генерации и просмотра отчета. 

### Развертывание и запуск
```
git clone https://github.com/koluzhenkov/pytest-selenium-test-example.git
cd pytest-selenium-test-example
tox
```
Для генерации и просмотра отчета:  
```allure serve reports```
