# This is a sample Python script.
import json
import icalendar
import pytz
from icalendar import Calendar, Event, vCalAddress, vText
import datetime
from datetime import datetime, timedelta
import pandas as pd
import requests



#read arrangement csv
week_arrangement = pd.read_csv('2020-2021-2.csv')
course_timetable = pd.read_csv('course_time.csv')

#get course_table json

with open('data.json') as data:
    course_list = json.load(data)


#init calendar
cal = Calendar()


def add_event():
    event = Event()
    event.add('summary', str(course_name))
    event_Y = int(row[1]['Y'])
    event_M = int(row[1]['M'])
    event_D = int(row[1]['D'])
    event_SH = int(course_timetable['SH'][int(course_no) - 1])
    event_SM = int(course_timetable['SM'][int(course_no) - 1])
    event_EH = int(course_timetable['EH'][int(course_no) - 1])
    event_EM = int(course_timetable['EM'][int(course_no) - 1])
    weekday = timedelta(days=(int(course_day) - 1))
    event.add('dtstart', (datetime(event_Y, event_M, event_D, event_SH, event_SM, 0,
                                   tzinfo=pytz.timezone('Asia/Shanghai')) + weekday))
    event.add('dtend', (datetime(event_Y, event_M, event_D, event_EH, event_EM, 0,
                                 tzinfo=pytz.timezone('Asia/Shanghai')) + weekday))
    # organizer = vCalAddress('MAILTO:tao-sls@sustech.edu.cn')
    # organizer.params['cn'] = vText(str(course_split1[1]))
    # event['organizer'] = organizer
    event['location'] = vText(str([x.strip() for x in course_split1[3].split('][')][1]))
    cal.add_component(event)

for course in course_list:

    #split course name
    #print(course['kbxx'])
    course_split1 = [x.strip() for x in course['kbxx'].split('\n')]
    course_name = course_split1[0]
    course_arrangement = course['key']
    # day of week
    course_day = course_arrangement.split("xq",1)[1][0]
    # no of day
    course_no = course_arrangement.split("jc",1)[1][0]

    #add course to ics

    #judge single/double week:
    course_week_type = 0
    if ("双" in course_split1[3]):
        course_week_type = 2
    elif ("单" in course_split1[3]):
        course_week_type = 1

    week_list = []
    for row in week_arrangement.iterrows():
        #single
        if (course_week_type == 0):
            # event = Event()
            # event.add('summary', str(course_name))
            # event_Y = int(row[1]['Y'])
            # event_M = int(row[1]['M'])
            # event_D = int(row[1]['D'])
            # event_SH = int(course_timetable['SH'][int(course_no)-1])
            # event_SM = int(course_timetable['SM'][int(course_no)-1])
            # event_EH = int(course_timetable['EH'][int(course_no)-1])
            # event_EM = int(course_timetable['EM'][int(course_no)-1])
            # weekday = timedelta(days=(int(course_day)-1))
            # event.add('dtstart', (datetime(event_Y, event_M, event_D, event_SH, event_SM, 0, tzinfo=pytz.timezone('Asia/Shanghai'))+weekday))
            # event.add('dtend',   (datetime(event_Y, event_M, event_D, event_EH, event_EM, 0, tzinfo=pytz.timezone('Asia/Shanghai'))+weekday))
            # # organizer = vCalAddress('MAILTO:tao-sls@sustech.edu.cn')
            # # organizer.params['cn'] = vText(str(course_split1[1]))
            # # event['organizer'] = organizer
            # event['location'] = vText(str([x.strip() for x in course_split1[3].split('][')][1]))
            # cal.add_component(event)
            add_event()
        # single week
        elif (course_week_type == 1 and (row[1]['NO'] % 2 == 1)):
            add_event()
        #double week
        elif (course_week_type == 2 and (row[1]['NO'] % 2 == 0)):
            add_event()





#dump ics
f = open('schedule.ics', 'wb')
f.write(cal.to_ical())
f.close()








