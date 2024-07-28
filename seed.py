import psycopg
import random
from faker import Faker
from random import choice, randint
from datetime import datetime, timedelta

conn_params = {
    'dbname': 'postgres',
    'user': 'postgres',
    'password': 'postgres',
    'host': 'localhost',  
    'port': 5432  
}

fake = Faker()

def create_fake_teachers(cursor, num):
    list_ids = []
    for _ in range(num): 
        name = fake.name()
        cursor.execute('INSERT INTO teacher (name) VALUES (%s) RETURNING id', (name,))
        id = cursor.fetchone()[0]
        list_ids.append(id)
    return list_ids
    
def create_fake_groups(cursor, num):
    list_ids = []
    for i in range(num):
        name = "group" + str(i)
        cursor.execute('INSERT INTO "group" (name) VALUES (%s) RETURNING id', (name,))
        id = cursor.fetchone()[0]
        list_ids.append(id)
    return list_ids

def create_fake_students(cursor, num, group_ids):
    list_ids = []
    for _ in range(num):  
        name = fake.name()
        group_id = random.choice(group_ids)
        cursor.execute('INSERT INTO student (name, group_id) VALUES (%s, %s) RETURNING id',
            (name, group_id))
        id = cursor.fetchone()[0]
        list_ids.append(id)
    return list_ids

        
def create_fake_subjects(cursor, num, teacher_ids):
    list_ids = []
    for i in range(num):
        name = "subject" + str(i)
        teacher_id = random.choice(teacher_ids)
        cursor.execute('INSERT INTO subject (name, teacher_id) VALUES (%s, %s) RETURNING id',
            (name, teacher_id))
        id = cursor.fetchone()[0]
        list_ids.append(id)
    return list_ids
        
def create_fake_grades(cursor, num, student_ids, subject_ids):
    for student_id in student_ids:
        for _ in range(num):
            value = random.randint(1, 10)
            date = fake.date()
            subject_id = random.choice(subject_ids)
            cursor.execute('INSERT INTO grade (student_id, subject_id, value, date) VALUES (%s, %s, %s, %s)',
                (student_id, subject_id, value, date))
        
        
if __name__ == '__main__':
    with psycopg.connect(**conn_params) as conn:
        with conn.cursor() as cur:    
            print("going to create fake data")
            teacher_ids = create_fake_teachers(cur, 5)
            print("teachers created")
            group_ids = create_fake_groups(cur, 3)
            print("groups created")
            student_ids = create_fake_students(cur, 50, group_ids)
            print("students created")
            subject_ids = create_fake_subjects(cur, 8, teacher_ids)
            print("sybjects created")
            create_fake_grades(cur, 20, student_ids, subject_ids)
            print("grades created")
            conn.commit()
            print("Success.")