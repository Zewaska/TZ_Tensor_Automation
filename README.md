# TZ_Tensor_Automation

Скопируйте репозиторий на свой локальный компьютер, используя команду:

```
$ git clone https://github.com/Zewaska/TZ_Tensor_Automation.git
```


## Для запуска тестов:
### 1) Установить [Scoop](https://scoop.sh/): 

```
 $ Set-ExecutionPolicy RemoteSigned -scope CurrentUser
 $ irm get.scoop.sh | iex
 ``` 

### 2) Установить [Allure](https://docs.qameta.io/allure-report/) (Необходимо наличие java для дальнейшей работы):

```
 $ scoop install allure
``` 

### 3) Установить библиотеки:
```
 $ pip install -r requirements.txt
``` 
### 4) В терминале запустить тесты командой: 

```
 $ pytest --alluredir=reports/
```
### 5) После завершения тестирования, для просмотра отчета введите:
```
$ allure serve reports
```

![ScreenAllure1](https://i2.paste.pics/9b336476de36d0b747f75f981707187d.png)

![ScreenAllure2](https://i2.paste.pics/39f5ca1132d22e29e2aba99c14dbdbef.png)

![ScreenAllure3](https://i2.paste.pics/d78d45d17e8fc37de342c7bfb47cab55.png)
