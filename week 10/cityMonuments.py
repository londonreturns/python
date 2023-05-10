try:
    monuments = {
        'kathmandu': 'Pashupatinath',
        'pokhara': 'Fewa Lake',
        'nepalgunj': 'Bageshwori Temple',
        'birgunj': 'Birgunj Ghanta Ghar'
    }
    city = input("Enter city: ")
    city = city.lower()
    if city not in ('kathmandu',
                    'pokhara',
                    'nepalgunj',
                    'birgunj'):
        raise ValueError
    print(monuments[city])
except ValueError:
    print('Invalid city')