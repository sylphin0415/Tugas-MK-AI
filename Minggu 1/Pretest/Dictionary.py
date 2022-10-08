print('''
================================
    Kamus bahasa sumbawa
================================
''')
dict={
    'saya' : 'kaji',
    'kamu' : 'sia',
    'mandi' : 'maneng',
    'makan' : 'mangan',
    'tidur' : 'tunung'
}

terjemahan1, terjemahan2, terjemahan3, terjemahan4, terjemahan5=input("Masukkan kata yang ingin di terjemahkan: ").split('')
print('terjemahan: ',dict[terjemahan1], dict[terjemahan2], dict[terjemahan3],dict[terjemahan4], dict[terjemahan5])
