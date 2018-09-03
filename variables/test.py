student_list =    [{'grades':(1,2,3)},
    {'grades':(0,0,0)},
    {'grades':(2,10,55)}
    ]


def average_grade_all_students(student_list):
    total =0
    count = 0
    for student in student_list:
        count += len(student['grades'])
        total = total +sum(student['grades'])
    print("Total {}".format(count))
    return total/count



print(average_grade_all_students(student_list))
