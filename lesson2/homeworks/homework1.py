"""
    Dichiarare due liste di numeri con cinque elementi ciascuna
    e creare una lista concatenata che le includa entrambe.

    BONUS: prendere gli elementi delle due liste dall'utente chiedendoli uno per uno.
"""

LENGTH = 5
list1 =  [None] * LENGTH
list2 = [None] * LENGTH

print('Insert elements of first list: ')
for i in range(0, LENGTH):
    list1[i] = int(input())

print('\nInsert elements of second list: ')
for i in range(0, LENGTH):
    list2[i] = int(input())

list_concat = [None] * LENGTH * 2

for i in range(0, LENGTH):
    list_concat[i] = list1[i]
    list_concat[i + LENGTH] = list2[i]

print('\n', list_concat)
