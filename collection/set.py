countries_to_visit = {'China', 'USA', 'USA', 'Japan'}

print(len(countries_to_visit))  # 3
print(countries_to_visit)  # {'Japan', 'China', 'USA'}
print(countries_to_visit == {'China', 'Japan', 'USA'})  # True

# The following operations do not modify the initial set
print(countries_to_visit | {'French'})  # {'Japan', 'USA', 'French', 'China'}
print(countries_to_visit & {'China', 'USA'})  # {'USA', 'China'}
print(countries_to_visit - {'China', 'Japan'})  # {'USA'}
print(countries_to_visit ^ {'USA', 'India'})  # {'Japan', 'China', 'India'}

print(countries_to_visit.isdisjoint({'French', 'Germany'}))  # True
print(countries_to_visit.isdisjoint({'French', 'USA'}))  # False

# A.issubset(B)
print({'China', 'USA'} <= countries_to_visit)  # True
print({'Russia'} <= countries_to_visit)  # False
print(set() <= countries_to_visit)  # True

# A.issuperset(B)
print(countries_to_visit >= {'Japan'})  # True
print(countries_to_visit >= {'Japan', 'French'})  # False

# A.issubset(B) and A != B
print({'China', 'Japan'} < countries_to_visit)  # True
print({'China', 'USA', 'Japan'} < countries_to_visit)  # False

# A.issuperset(B) and A != B
print(countries_to_visit > {'China', 'Japan'})  # True
print(countries_to_visit > {'China', 'USA', 'Japan'})  # False
