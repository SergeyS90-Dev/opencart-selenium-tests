
# Автоматизированное тестирование OpenCart

Итоговая работа по автоматизации тестирования веб-приложений.

## О проекте

В рамках работы интернет-магазин OpenCart развёрнут локально с использованием Docker Compose.

Для проверки функциональности сайта написаны **10 автоматизированных тестов** на Python с применением Selenium WebDriver.

### Используемые технологии

- Python 3.12
- Selenium 4.51.0
- Google Chrome
- Docker Compose
- OpenCart 4.0.2
- MariaDB 11.2
- phpMyAdmin

## Запуск OpenCart

Для запуска необходимы Docker и Docker Compose.

В каталоге проекта выполнить:

```powershell
docker compose up -d
```

После запуска магазин доступен по адресу:

http://localhost:8081

Проверка контейнеров:

```powershell
docker compose ps
```

Остановка контейнеров:

```powershell
docker compose down
```

> Пароли базы данных в `docker-compose.yml` являются демонстрационными и предназначены исключительно для локального учебного окружения.

## Запуск автотестов

Необходимы Python, Google Chrome и доступный локально OpenCart.

Установка зависимостей:

```powershell
pip install -r requirements.txt
```

Запуск отдельного теста:

```powershell
python tests/test_category.py
```

Запуск всех тестов в Windows PowerShell:

```powershell
Get-ChildItem .\tests\test_*.py | Sort-Object Name | ForEach-Object {
    python $_.FullName
    if ($LASTEXITCODE -ne 0) { break }
}
```

## Проверяемая функциональность

Реализованы 10 тестов:

1. Добавление MacBook в корзину.
2. Открытие категории Desktops.
3. Проверка заголовка главной страницы.
4. Открытие карточки MacBook.
5. Проверка отображения цены товара.
6. Проверка формы регистрации.
7. Удаление товара из корзины.
8. Проверка наличия поля поиска.
9. Ввод текста в поле поиска.
10. Поиск товара iPhone.

## Результаты

При локальном запуске **19 октября 2026 года все 10 тестов завершились успешно**.

Подтверждающие скриншоты находятся в каталоге `screenshots`:

- `docker-containers.png` — запущенные Docker-контейнеры.
- `opencart-home.png` — главная страница локального магазина.
- `test-results.png` — результаты выполнения автотестов.

Отчёт по итоговой работе находится в каталоге `report`.
