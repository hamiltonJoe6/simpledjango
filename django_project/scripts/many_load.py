import csv

from hello.models import Person, Course, Membership

def run():
	fhand = open('hello/load.csv')
	reader = csv.reader(fhand)

	Person.objects.all().delete()
	Course.objects.all().delete()
	Membership.objects.all().delete()

	for row in reader:
		print(row)

		p, created = Person.objects.get_or_create(email=row[0])
		c, created = Course.objects.get_or_create(title=row[2])

		r = Membership.LEARNER
		if row[1] == 'I' : r = Membership.INSTRUCTOR
		m = Membership(role=r,person=p,course=c)
		m.save()
