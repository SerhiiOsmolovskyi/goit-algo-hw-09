# Домашнє завдання: Видача решти касовим апаратом

## Опис завдання

У цьому завданні розроблено дві функції для касової системи, яка визначає оптимальний спосіб видачі решти покупцеві. Використовуються два підходи:

1. **Жадібний алгоритм** (`find_coins_greedy`): обирає найбільший доступний номінал монети, поки сума не буде видана повністю.
2. **Алгоритм динамічного програмування** (`find_min_coins`): знаходить мінімальну кількість монет для досягнення заданої суми.

## Алгоритми

### Жадібний алгоритм (`find_coins_greedy`)

- Починає з найбільшого номіналу монети.
- Віднімає від суми максимальну можливу кількість монет цього номіналу.
- Повторює цей процес для наступного меншого номіналу.
- Працює швидко, але не завжди дає оптимальне рішення.

**Часова складність**: `O(N)`, де `N` — кількість номіналів монет.

### Алгоритм динамічного програмування (`find_min_coins`)

- Використовує таблицю для збереження мінімальної кількості монет для кожної проміжної суми.
- Підходить до рішення поступово, використовуючи попередні обчислення.
- Гарантує мінімальну кількість монет.

**Часова складність**: `O(N * M)`, де `N` — кількість номіналів монет, `M` — сума, яку потрібно видати.

## Порівняння ефективності

Було протестовано обидва алгоритми на сумі `113`:

- **Жадібний алгоритм**:

  - Видав `{50: 2, 10: 1, 2: 1, 1: 1}`
  - Виконався швидко
  - Може не давати оптимальне рішення

- **Динамічне програмування**:
  - Видав `{50: 2, 10: 1, 2: 1, 1: 1}` (оптимальне рішення)
  - Виконався повільніше
  - Гарантовано мінімальна кількість монет

## Висновки

- **Жадібний алгоритм** швидший, але не завжди знаходить найменшу кількість монет.
- **Динамічне програмування** гарантує мінімальну кількість монет, але працює повільніше на великих сумах.
- У реальних касових системах можна комбінувати обидва підходи для ефективної роботи.
