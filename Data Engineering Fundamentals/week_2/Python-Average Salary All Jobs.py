from collections import defaultdict
salaries = [
    ("Software Engineer", 70000),
    ("Data Scientist", 80000),
    ("Software Engineer", 75000),
    ("Data Scientist", 85000),
    ("Project Manager", 90000),
    ("Software Engineer", 80000)
]

def calculate_avg_salary(salaries):
    job_salaries = defaultdict()
    for row in salaries:
        if row[0] not in job_salaries:
            job_salaries[row[0]] = [0,0]
            job_salaries[row[0]][0]+=1
            job_salaries[row[0]][1]+=row[1]
        else:
            job_salaries[row[0]][0]+=1
            job_salaries[row[0]][1]+=row[1]
    
    avg_salary = {}
    for job_title, data in job_salaries.items():
        avg_salary[job_title] = data[1]/data[0] 
    return avg_salary