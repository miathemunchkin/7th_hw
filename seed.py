import random
from faker import Faker
from db import session 
from models import Teacher, Group, Subject, Grade, Student 

faker = Faker()

def create_fake_teachers(num):
    list_ids = []
    for _ in range(num): 
        name = faker.name()
        new_teacher = Teacher(fullname=name)
        session.add(new_teacher)
        session.commit()
        list_ids.append(new_teacher.id)
    return list_ids
    
def create_fake_groups(num):
    list_ids = []
    for i in range(num):
        name = f"group{i}"
        new_group = Group(name=name)
        session.add(new_group)
        session.commit()
        list_ids.append(new_group.id)
    return list_ids

def create_fake_students(num, group_ids):
    list_ids = []
    for _ in range(num): 
        new_student = Student(fullname=faker.name(), group_id=random.choice(group_ids))
        session.add(new_student)
        session.commit()
        list_ids.append(new_student.id)
    return list_ids
        
def create_fake_subjects(num, teacher_ids):
    list_ids = []
    for i in range(num):
        name = f"subject{i}"
        new_subject = Subject(name=name, teacher_id=random.choice(teacher_ids))
        session.add(new_subject)
        session.commit()
        list_ids.append(new_subject.id)
    return list_ids
        
def create_fake_grades(num, student_ids, subject_ids):
    for student_id in student_ids:
        for _ in range(num):
            new_grade = Grade(
                student_id=student_id,
                subject_id=random.choice(subject_ids),
                grade=random.uniform(60, 100),
                date=faker.date_between(start_date='-2y', end_date='today')
            )
            session.add(new_grade)
    session.commit()
        
        
if __name__ == '__main__':
    print("going to create fake data")
    teacher_ids = create_fake_teachers(5)
    print("teachers created")
    group_ids = create_fake_groups(3)
    print("groups created")
    student_ids = create_fake_students(50, group_ids)
    print("students created")
    subject_ids = create_fake_subjects(8, teacher_ids)
    print("subjects created")
    create_fake_grades(20, student_ids, subject_ids)
    print("grades created")
    print("Success.")
