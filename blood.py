"""Идеальный срок набора зачётных донаций с нуля; условия и источники в README."""

from calendar import monthrange
from datetime import date, timedelta

START_DATE = date(2026, 9, 6)
PLATELET_INTERVAL_DAYS = 14
REQUIRED_DONATIONS = {"Москва": 20, "Россия": 40}


def minimum_days(donations):
    # Ни один критерий не требует меньше 20/40 процедур, ни один интервал
    # не короче 14 дней. Тромбоциты засчитываются как кровь и достигают минимума.
    # Первая донация — день 0; сроки оформления награды не включены.
    return (donations - 1) * PLATELET_INTERVAL_DAYS


def quantity(value, forms):
    index = 2 if 11 <= value % 100 <= 14 else {1: 0, 2: 1, 3: 1, 4: 1}.get(value % 10, 2)
    return f"{value} {forms[index]}"


def calendar_duration(start, days):
    end = start + timedelta(days=days)
    months = (end.year - start.year) * 12 + end.month - start.month
    if end.day < min(start.day, monthrange(end.year, end.month)[1]):
        months -= 1
    year, month = divmod(start.year * 12 + start.month - 1 + months, 12)
    anchor = date(year, month + 1, min(start.day, monthrange(year, month + 1)[1]))
    years, months = divmod(months, 12)
    parts = (
        (years, ("год", "года", "лет")),
        (months, ("месяц", "месяца", "месяцев")),
        ((end - anchor).days, ("день", "дня", "дней")),
    )
    return ", ".join(quantity(value, forms) for value, forms in parts)


def main():
    for award, donations in REQUIRED_DONATIONS.items():
        days = minimum_days(donations)
        print(f"{award}: {calendar_duration(START_DATE, days)} ({days} дней)")
        print(f"    0 донаций крови, 0 донаций плазмы, {donations} донаций тромбоцитов")


if __name__ == "__main__":
    main()
