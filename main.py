money = int(input("Введите сумму, которую вы планируете положить под проценты: "))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = []
for value in per_cent.values():
    deposit.append(int(money / 100 * value))
print('Максимальная сумма, которую вы можете заработать — %d' % max(deposit))
