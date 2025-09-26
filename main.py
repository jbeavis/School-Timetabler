# CSP Backtracking
import json 

# Variables:
# Get variables from JSON:
with open("data/dummyData_2.json") as f:
    data = json.load(f)

subjects = data["subjects"]
teachers = data["teachers"]
rooms = data["rooms"]

timeslots = ["9am", "10am", "11am", "1pm","2pm"]

days = ["Mon", "Tue", "Wed", "Thu", "Fri"]

# Code 
variables = []
for subject, info in subjects.items():
    for cls in info["classes"]:
        for i in range(info["frequency"]):
            variables.append(f"{cls}_{subject}_Lesson{i+1}")

# A domain is (time, day, room). Then assign a variable (class) to it, checking if it's valid
slots = []
for day in days:
    for time in timeslots:
        for room in rooms.keys():
            slots.append((day,time,room))

lessons = []
# Iterate through subjects. 
for s in subjects.keys():
    # Iterate through classes. 
    for c in subjects[s]["classes"]:
    # Create a new lesson for frequency per class
        for frequency in range(subjects[s]["frequency"]):
            lessons.append({f"{c}_{frequency+1}" : s})

domains = {}
for x in lessons:
    domains[list(x.keys())[0]] = slots

timetable = {}
# eg {("Mon", "9am", "Room1") : ("LessonName", "Mr Sawtell, "Maths")}

def main(timetable, lessons):
    if len(lessons) == 0:  # base case: no lessons left
        return timetable

    lesson = lessons[0]  # pick the first unassigned lesson
    className = list(lesson.keys())[0]
    subject = lesson[className]

    for day, time, room in domains[className]:
        # check teacher availability & room availability & subject clash
        subject = lesson[className]
        selectedTeacher = None
        for teacher in teachers.keys():
            clash = False
            # Do they teach this subject
            if subject not in teachers[teacher]["subjects"]:
                continue            
            # do they work on this day
            if day not in teachers[teacher]["days"]:
                continue
            #  is that teacher already teaching at this time/day
            for (d, t, r), (scheduledLesson, assignedTeacher, lessonSubject) in timetable.items():
                if d == day and t == time and assignedTeacher == teacher:
                    clash = True
                    break
            if clash == True:
                continue
            selectedTeacher = teacher
            break

        # is there a room that can do this,
        if subject not in rooms[room]:
            continue  # room can’t host this subject
        clash = False
        for (d, t, r), (scheduledLesson, assignedTeacher, lessonSubject) in timetable.items():
            if d == day and t == time and r == room:
                clash = True
                break
        if clash:
            continue
        selectedRoom = room
                
        lessonClash = False
        # is this subject already being taught at this time on this day
        for (d, t, r), (scheduledLesson, assignedTeacher, lessonSubject) in timetable.items():
            if t == time and d == day:
                if lessonSubject == subject:
                    lessonClash = True

        if selectedTeacher is None or selectedRoom is None or lessonClash:
            continue

        timetable[(day,time,selectedRoom)] = (lesson, selectedTeacher, subject)
        remaining = lessons[1:] # Shrink the list remove current
        result = main(timetable, remaining)
        if result is not None:
            return result
        timetable.pop((day,time,selectedRoom))  # backtrack

    return None  # only return None if no domain worked for this lesson

timetable = main(timetable, lessons)

def orderTimetable(timetable):
    # Define the order for days and times
    day_order = {day: i for i, day in enumerate(days)}
    time_order = {time: i for i, time in enumerate(timeslots)}

    # Sort timetable items by day and time
    sorted_items = sorted(
        timetable.items(),
        key=lambda x: (day_order[x[0][0]], time_order[x[0][1]], x[0][2])
    )

    for x in sorted_items:
        print(x)

orderTimetable(timetable)