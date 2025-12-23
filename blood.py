import heapq

max_blood = 40
max_plasm = 60

last_start = 0
last_blood = 1
last_plasm = 2

intervals = {
    (last_start, last_blood): 0,
    (last_start, last_plasm): 0,
    (last_blood, last_blood): 60,
    (last_blood, last_plasm): 30,
    (last_plasm, last_blood): 14,
    (last_plasm, last_plasm): 14,
}

moscow = False
russia = False

dist = [
    [[float('inf')] * 3 for _ in range(max_plasm + 1)]
    for _ in range(max_blood + 1)
]
heap = [(0, 0, 0, last_start)]
dist[0][0][last_start] = 0

while True:
    if not heap:
        break

    days, blood, plasm, last = heapq.heappop(heap)
    if days != dist[blood][plasm][last]:
        continue

    total = blood + plasm

    if not moscow:
        if (
            blood >= 20
            or (blood >= 13 and plasm >= 20)
            or (blood < 13 and plasm >= 30)
            or plasm >= 30
        ):
            moscow = True
            months = days // 30
            years = months // 12
            rem_months = months % 12
            rem_days = days % 30
            print(
                'Moscow: ' + str(years) + ' years, ' + str(rem_months)
                + ' months, ' + str(rem_days) + ' days (' + str(days)
                + ' days)'
            )
            print('    ' + str(blood) + ' blood, ' + str(plasm) + ' plasma donations')

    if not russia:
        if (
            blood >= 40
            or plasm >= 60
            or (blood >= 25 and total >= 40)
            or (1 <= blood <= 24 and total >= 60)
        ):
            russia = True
            months = days // 30
            years = months // 12
            rem_months = months % 12
            rem_days = days % 30
            print(
                'Russia: ' + str(years) + ' years, ' + str(rem_months)
                + ' months, ' + str(rem_days) + ' days (' + str(days)
                + ' days)'
            )
            print('    ' + str(blood) + ' blood, ' + str(plasm) + ' plasma donations')

    if moscow and russia:
        break

    for next_last in (last_blood, last_plasm):
        if next_last == last_blood and blood >= max_blood:
            continue
        if next_last == last_plasm and plasm >= max_plasm:
            continue

        interval = intervals[(last, next_last)]
        next_blood = blood + (1 if next_last == last_blood else 0)
        next_plasm = plasm + (1 if next_last == last_plasm else 0)
        if next_blood > max_blood:
            next_blood = max_blood
        if next_plasm > max_plasm:
            next_plasm = max_plasm
        next_days = days + interval

        if next_days < dist[next_blood][next_plasm][next_last]:
            dist[next_blood][next_plasm][next_last] = next_days
            heapq.heappush(
                heap,
                (next_days, next_blood, next_plasm, next_last),
            )
