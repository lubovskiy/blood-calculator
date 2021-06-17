moscow = False
russia = False

months = 1

while True:
    plasm = months
    blood = months // 12 * 5 + min([(months % 12 + 1) // 2, 5])

    if not moscow:
        if blood >= 20 or plasm >= 30 or (blood >= 13 and blood + plasm >= 20) or (blood < 13 and blood + plasm >= 30):
            moscow = True
            print('Moscow: ' + str(months // 12) + ' years, '+ str(months % 12) + ' months (' + str(months) + ' months)')
            print('    ' + str(blood) + ' blood, ' + str(plasm) + ' plasm donations')

    if not russia:
        if (blood > 25 and blood + plasm >= 40) or blood >= 40 or blood + plasm >= 60 or plasm >= 60:
            russia = True
            print('Russia: ' + str(months // 12) + ' years, '+ str(months % 12) + ' months (' + str(months) + ' months)')
            print('    ' + str(blood) + ' blood, ' + str(plasm) + ' plasm donations')

    if moscow and russia:
        break

    months += 1
