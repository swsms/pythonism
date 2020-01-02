capitals_by_countries = {
    'China': 'Beijing',
    'France': 'Paris',
    'Japan': 'Tokyo',
}

print(len(capitals_by_countries))  # 3

# {'China': 'Beijing',
#  'France': 'Paris',
#  'Japan': 'Tokyo'}
print(capitals_by_countries)
print(capitals_by_countries.keys())  # dict_keys(['China', 'France', 'Japan'])
print(capitals_by_countries.values())  # dict_values(['Beijing', 'Paris', 'Tokyo'])

print(capitals_by_countries.get('China'))  # Beijing
print(capitals_by_countries.get('USA', 'Unknown'))  # Unknown

capitals_by_countries['Germany'] = 'Berlin'

# {'China': 'Beijing',
#  'France': 'Paris',
#  'Japan': 'Tokyo',
#  'Germany': 'Berlin'}
print(capitals_by_countries)

capitals_by_countries.pop('Japan')

# {'China': 'Beijing',
#  'France': 'Paris',
#  'Germany': 'Berlin'}
print(capitals_by_countries)

# China: Beijing
# France: Paris
# Germany: Berlin
for country, capital in capitals_by_countries.items():
    print(f'{country}: {capital}')
