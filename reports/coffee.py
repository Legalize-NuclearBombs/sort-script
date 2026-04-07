from collections import defaultdict
from operator import itemgetter
from statistics import median

from .base import Report


class MedianCoffee(Report):
    def calculate(self, data: list[dict]):
        student_spending = defaultdict(list)
        for row in data:
            name = row.get('student')
            spent = row.get('coffee_spent')
            if name and spent:
                student_spending[name].append(float(spent))

        results = []
        for name, spends in student_spending.items():
            results.append([name, median(spends)])

        results.sort(key=itemgetter(1), reverse=True)
        return results
