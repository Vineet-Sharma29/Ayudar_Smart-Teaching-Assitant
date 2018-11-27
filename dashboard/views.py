from django.shortcuts import render
from .models import Marks
from .models import csvfile,Enrollments
from django.http import HttpResponse
from .forms import file_class

from django.shortcuts import render



#
# def uselesspage(request):
#     return render(request, 'DB/uselesspage.html')


# df= initialise(marks,marks_header)
# Course = CourseStats(marks)
# Exam = ExamStats(marks)
# PersistentLabels = PersistentLabels()
# PerformanceLabels = PerformanceLabels()
# Needy_List = mainFunc()




def add_to_database(pat):
    path = 'media/media_/' + pat
    co_id = "ASE"
    pr_id = "SUBU"

    Marks.objects.filter(course_id=co_id).delete()
    Enrollments.objects.filter(course_id=co_id).delete()

    with open(path) as f:
        f1 = f.readline().split(",")
        f1[len(f1) - 1] = f1[len(f1) - 1].rstrip()

        return_firstline_as_tuple(f1)

        f.seek(0, 0)
        f_all = f.readlines()

        return_tuple(f_all)

        f_all[len(f_all) - 1] = f_all[len(f_all) - 1] + '\n'
        for i in range(1, len(f_all)):
            f_all[i] = f_all[i].rstrip()
            f2 = f_all[i].split(',')

            Enrollments.objects.create(course_id=co_id, student_id=f2[0], student_name=f2[1], prof_id=pr_id,
                                       status="not_needy")

            for j in range(0, len(f2) - 2):
                sid = f2[0]
                sname = f2[1]
                marks = f2[j + 2]
                qname = f1[j + 2]

                Marks.objects.create(student_name=sname, student_id=sid, marks=marks, q_name=qname, course_id=co_id,
                                     prof_id=pr_id)
    #
    # all_quiz_marks_in_a_course()
    # all_quiz_marks_in_all_courses()
    return 'done'

#
# def call():
#     print(Marks.objects.filter(q_name="q3"))


def return_tuple(line):
    req_tuple = ()
    for n in range(1, len(line)):
        line[n] = line[n].rstrip()
        x = tuple(line[n].split(','))
        req_tuple += (x,)
    print(req_tuple)

    # tup=tuple(a)
    # print(tup(0))

    # a[0]=tuple(a[0])
    # print(type(a[0]))

    # tup=tuple(a)
    #
    # print(tup(0))


def dashboard(request):
    form1 = file_class(request.POST, request.FILES or None)
    if request.method == 'POST':
        if form1.is_valid():
            form1.save()
            print(request.FILES['req_file'])
            file1 = str(request.FILES['req_file'])
            add_to_database(file1)
            return render(request, "dashboard/dashboard.html",{'form':form1})
        else:
            return HttpResponse("form is invalidd")
    else:
        form1 = file_class()
        return render(request, "dashboard/dashboard.html",{'form':form1})


# for student in students:
#     marks = tuple(row)
#     v = ag.initialize(marks, header)
#     CourseStat = CourseStats(marks)
#     ExamStat = ExamStats(marks)
#     Labels = PersistenLabels(v)
#
#

def needy_list(request):
    return render(request, "dashboard/needy_list.html")


def list_of_students(request):
    return render(request, "dashboard/list_of_students.html")


def custom_404(request):
    return render(request, "dashboard/404.html")

def all_quiz_marks_in_a_course():
    b=Marks.objects.filter(student_id="55", course_id="ASE", prof_id="SUBU").values_list('q_name','marks')
    print(b)
    print(type(b))



def all_quiz_marks_in_all_courses():
    print(Marks.objects.filter(student_id="55").values_list('course_id','q_name','marks'))



def return_firstline_as_tuple(fline):
    print(tuple(fline))



def return_tuple(line):
    req_tuple = ()
    for n in range(1, len(line)):
        line[n] = line[n].rstrip()
        x = tuple(line[n].split(','))
        req_tuple += (x,)
    print(req_tuple)
