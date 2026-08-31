# Write a program to accept an integer amount from user and tell minimum number of notes
#  needed for representing that amount.

amount = int(input('Enter amount : '))

note_2000 = amount // 2000
amount = amount % 2000

note_500 = amount // 500
amount = amount % 500

note_200 = amount // 200
amount = amount % 200

note_100 = amount // 100
amount = amount % 100

note_50 = amount // 50
amount = amount % 50

note_20 = amount // 20
amount = amount % 20

note_10 = amount // 10
amount = amount % 10

Minimum_note = note_2000 + note_500 + note_200 + note_100 + note_50 + note_20 + note_10

print(f'minimum numbers of notes are : {Minimum_note}')

