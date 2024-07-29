from sqlalchemy import func, desc
from sqlalchemy.orm import sessionmaker
from db import engine
from models import Student, Grade, Subject, Teacher, Group

Session = sessionmaker(bind=engine)
session = Session()

def select_1():
    return session.query(
        Student.fullname, 
        func.round(func.avg(Grade.grade), 2).label('avg_grade')
    ).join(Grade).group_by(Student.id).order_by(desc('avg_grade')).limit(5).all()

def select_2(subject_name):
    return session.query(
        Student.fullname, 
        func.round(func.avg(Grade.grade), 2).label('avg_grade')
    ).join(Grade).join(Subject).filter(Subject.name == subject_name).group_by(Student.id).order_by(desc('avg_grade')).limit(1).all()

def select_3(subject_name):
    return session.query(
        Group.name, 
        func.round(func.avg(Grade.grade), 2).label('avg_grade')
    ).join(Student).join(Grade).join(Subject).filter(Subject.name == subject_name).group_by(Group.id).all()

def select_4():
    return session.query(func.round(func.avg(Grade.grade), 2).label('avg_grade')).all()

def select_5(teacher_id):
    return session.query(Subject.name).filter(Subject.teacher_id == teacher_id).all()

def select_6(group_name):
    return session.query(Student.fullname).join(Group).filter(Group.name == group_name).all()

def select_7(subject_name, group_name):
    return session.query(
        Student.fullname, 
        Grade.grade
    ).join(Grade).join(Subject).join(Group).filter(
        Subject.name == subject_name, 
        Group.name == group_name
    ).all()

def select_8(teacher_id):
    return session.query(
        func.round(func.avg(Grade.grade), 2).label('avg_grade'), 
        Subject.name
    ).join(Subject).filter(Subject.teacher_id == teacher_id).group_by(Subject.id).all()

def select_9(student_id):
    return session.query(
        Subject.name
    ).distinct().join(Grade).filter(Grade.student_id == student_id).all()

def select_10(student_id, teacher_name):
    return session.query(
        Subject.name
    ).distinct().join(Grade).join(Teacher).filter(
        Grade.student_id == student_id, 
        Teacher.fullname == teacher_name
    ).all()

if __name__ == "__main__":
    print(select_1())
    print(select_2('subject2'))
    print(select_3('subject2'))
    print(select_4())
    print(select_5(1))
    print(select_6('group1'))
    print(select_7('subject1', 'group1'))
    print(select_8(1))
    print(select_9(1))
    print(select_10(1, 'John Doe'))
