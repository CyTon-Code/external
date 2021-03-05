# external modules (plugins)

Here you can see external modules in development mode.

![plugins.png](logo_external.png)

Планируются такие модули-плагины:

1. Модуль для взаимодействий пользователя с встроенными модулями.
2. Модуль для взаимодействий пользователя с дополнительными модулями.
3. Модуль для использования команд из аргументов (обычно при запуске).
4. Модуль для использования внешних скриптов python, ANT.
5. Шаблон модуля — выводит "hello world!\n"
6. Вывод нужного текста, настройки к модулю - echo, @echo -set

<!--
7. Стандартные команды оперирующие с числами sum del...
8. типы и переменные (list, char, number) хранить как объекты склеенными с
  ключами в масиве пуш анд пул.
-->

Скрипт ANT - если смотреть на терминал как на интерпретатор, то думаю будет
  понятней, что такое скрипт. По сути это файл для выполнения команд по строчно
  (возможно аналогичен cmd).

Плагины — самые сложные модули. Есть ряд советов, даже правил, чтобы ANT
  работал коректно:
1. модули нельзя перемещать во время работы других модулей, без особой причины
  (касается всех типов модулей).
2. плагины — всегда особая причина.
Используя плагин перемещая, советую не выключать функцию сохранения предыдущего
   адреса в файл.
3. используя плагин копируя, советую: а) не носить вашему плагину такое же имя
   как у файла для копии. б) не выключать функцию для сохранения адреса в файл.
4. используя плагин записывая в sys.path, не убирайте функцию сохранения ситуации
   (был добавлен этот адрес в sys.path или нет, если да мы его после удалим).
 Этот способ использует дополнительный модуль, для извлечения папки в которой
   находится файл. (похожа на "получить имя"). Также в этом случае ваше имя
   функции должно быть main.
Я советую два способа, они противоположны, но одинаково важны.
1. перемещение — такой способ однозначно поможет, если приложение выключилось
то ANT сможет запустить его попросив разрешения у вас, зная какой плагин был
   последним.
2. sys.path - такой способ эффективен по скорости. чем меньше обращений к диску
тем больше скорость. Но риск потери знаний какой был последни велик, разве что
   вести log.


-эта документация была написана еще до написания конечной версии. Поэтому все
что здесь описывается не полностью описывает конечный продукт, также
документация будет оптимизироваться, а сам продукт будет подстраиваться под нее.
