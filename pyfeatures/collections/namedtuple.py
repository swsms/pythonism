from collections import namedtuple

Job = namedtuple('Job', [
    'title',
    'skills',
    'month_salary'
])

py_dev_job = Job(title='Python Developer',
                 skills=['Python', 'Git'],
                 month_salary=10000)

print(py_dev_job)  # Job(title='Python Developer', skills=['Python', 'Git'], month_salary=10000)
print(py_dev_job.title)  # Python Developer
print(py_dev_job[1])     # ['Python', 'Git']

Person = namedtuple('Person', 'name age looking_for_job', defaults=(False, ))

john = Person(name='John', age=40)
print(john)  # Person(name='John', age=40, looking_for_job=True)

print(john._fields)    # ('name', 'age', 'looking_for_job')
print(john._asdict())  # OrderedDict([('name', 'John'), ('age', 40), ('looking_for_job', False)]
print(john._replace(name='John Smith'))

samantha = Person._make(['Samantha Stone', 30, True])
print(samantha)  # Person(name='Samantha Stone', age=30, looking_for_job=True)
