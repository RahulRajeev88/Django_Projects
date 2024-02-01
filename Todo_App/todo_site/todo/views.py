from django.shortcuts import render, redirect



def task_list(request):
    context = {}
    return render(request,"task_list.html",context)


def task_update(request):
    context = {}
    return render(request,"task_list.html",context)


def task_delete(request):
    context = {}
    return render(request,"task_delete.html",context)


