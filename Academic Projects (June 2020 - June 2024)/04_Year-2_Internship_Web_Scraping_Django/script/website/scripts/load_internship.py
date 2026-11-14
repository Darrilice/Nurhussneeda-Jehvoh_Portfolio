from internship.models import Intern_other
import csv


def run():
    with open('internship/scrap_other3.csv', encoding= 'utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header

        Intern_other.objects.all().delete()

        for col in reader:
            print(col)

            work = Intern_other(JOB_DESCRIPTION=col[1],COMPANY=col[2],LOCATION=col[3],EMPLOYMENT_RATE=col[4])
            work.save()