'''
course_search is a Python script using a terminal based menu to help
students search for courses they might want to take at Brandeis
'''

from schedule import Schedule
import sys

schedule = Schedule()
schedule.load_courses()
schedule = schedule.enrolled(range(5,1000)) # eliminate courses with no students

TOP_LEVEL_MENU = '''
quit
reset
term  (filter by term)
coursenum (filter by coursenum, e.g. COSI 103a)
instructor (filter by instructor)
subject (filter by subject, e.g. COSI, or LALS)
title  (filter by phrase in title)
description (filter by phrase in description)
timeofday (filter by day and time, e.g. meets at 11 on Wed)
status (filter by course status)
'''

terms = {c['term'] for c in schedule.courses}

def topmenu():
    '''
    topmenu is the top level loop of the course search app
    '''
    global schedule
    while True:         
        command = input(">> (h for help) ")
        if command=='quit':
            return
        elif command in ['h','help']:
            print(TOP_LEVEL_MENU)
            print('-'*40+'\n\n')
            continue
        elif command in ['r','reset']:
            schedule.load_courses()
            schedule = schedule.enrolled(range(5,1000))
            continue
        elif command in ['t', 'term']:
            term = input("enter a term:"+str(terms)+":")
            schedule = schedule.term([term]).sort('subject')
        elif command in ['c','course']:
            num = input ("enter the course number:")
            schedule = schedule.coursenum([num])
        elif command in ['i','instructor']:
            email = input("enter the instructor's email:")
            schedule = schedule.email([email])
        elif command in ['s','subject']:
            subject = input("enter a subject:")
            schedule = schedule.subject([subject])
        elif command == 'title':
            title = input("enter a title:")
            schedule = schedule.title([title])
        elif command == 'description':
            des = input("enter a description:")
            schedule = schedule.description([des])
        elif command == 'status':
            ''' Author: Xianzhen Zhao '''
            status = input("enter a status:")
            schedule = schedule.status([status])
        elif command == 'times':
            ''' Author: Kelly Zhang '''
            times = input("timeofday:")
            schedule = schedule.times([times])
        elif command == 'section':
            '''Author: Zheyu Yan  Date: Feb. 17th'''
            section = input("enter the section:")
            schedule = schedule.section([section])

        else:
            print('command',command,'is not supported')
            continue

        print("courses has",len(schedule.courses),'elements',end="\n\n")
        print('here are the first 10')
        for course in schedule.courses[:10]:
            print_course(course)
        print('\n'*3)

def print_course(course):
    '''
    print_course prints a brief description of the course 
    '''
    print(course['subject'],course['coursenum'],course['section'],
          course['name'],course['term'],course['instructor'])

if __name__ == '__main__':
    topmenu()

