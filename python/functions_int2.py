x = [[5, 2, 3], [10, 8, 9]]
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name': 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}
z = [{'x': 10, 'y': 20}]
x[1][0] = 15
students[0].update({'last_name': 'Bryant'})
sports_directory.update({'soccer':['Andres', 'Ronaldo', 'Rooney']})
z[0].update({'y': 30})




def iterateDictionary():
    students = [
             {'first_name':  'Michael', 'last_name': 'Jordan'},
             {'first_name': 'John', 'last_name': 'Rosales'},
             {'first_name': 'Mark', 'last_name': 'Guillen'},
             {'first_name': 'KB', 'last_name': 'Tonel'}
        ]
    print('firs_name -', (students[0]['first_name']), ',', 'last_name -', (students[0]['last_name']))
    print('firs_name -', (students[1]['first_name']), ',', 'last_name -', (students[1]['last_name']))
    print('firs_name -', (students[2]['first_name']), ',', 'last_name -', (students[2]['last_name']))
    print('firs_name -', (students[3]['first_name']), ',', 'last_name -', (students[3]['last_name']))
iterateDictionary()

