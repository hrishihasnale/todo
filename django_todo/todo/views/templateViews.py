from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
import requests, json



def create_task(request):

    context = dict()
    todo_list = []
    if request.method == 'POST':
        username = request.POST.get('your_name', '')
        task = request.POST.get('task', '')
        description = request.POST.get('description', '')
        completed = request.POST.get('completed', False)

        url = 'http://127.0.0.1:8000/api/v1/todo/create/'
        body_param = {'username': username, 'task': task,'description':description,'completed':completed}

        res = requests.post(url, data=body_param)
        if res.status_code == 200:

            # Calling Todo list API
            url = 'http://127.0.0.1:8000/api/v1/todo/get_user_list/'
            body_param = {'username': username}

            res = requests.get(url, data=body_param)
            if res.status_code == 200:
                result = json.loads(res.text)
                todo_list = result
        else:
            print("Something went wrong!!")
    else:
        print("Invalid Request!!")

    context['todo_list'] = todo_list
    print(todo_list)
    return render(request, 'todoList.html', context=context)


def read_task(request):

    context = dict()
    todo_list = []
    if request.method == 'POST':
        username = request.POST.get('username', '')

        url = 'http://127.0.0.1:8000/api/v1/todo/get_user_list/'
        body_param = {'username': username}

        res = requests.get(url, data=body_param)
        if res.status_code == 200:
            result = json.loads(res.text)
            todo_list = result
        else:
            print("Something went wrong!!")

    else:
        print("Invalid Request!!")

    context['todo_list'] = todo_list
    return render(request, 'todoList.html', context=context)


def update_task(request):

    context = dict()
    todo_list = []

    if request.method == 'POST':

        task_id = request.POST.get('task_id', '')
        username = request.POST.get('update_your_name', '')
        task = request.POST.get('update_task', '')
        description = request.POST.get('update_description', '')
        completed = request.POST.get('update_completed', False)

        url = 'http://127.0.0.1:8000/api/v1/todo/update/'
        body_param = {'id':task_id, 'username':username, 'task':task, 'description':description, 'completed':completed}

        res = requests.post(url, data=body_param)
        if res.status_code == 200:

            # Calling Todo list API
            url = 'http://127.0.0.1:8000/api/v1/todo/get_user_list/'
            body_param = {'username': username}

            res = requests.get(url, data=body_param)
            if res.status_code == 200:
                result = json.loads(res.text)
                todo_list = result
        else:
            print("Something went wrong!!")

    else:
        print("Invalid Request!!")

    context['todo_list'] = todo_list
    return render(request, 'todoList.html', context=context)


def dalete_task(request):

    context = dict()
    todo_list = []

    if request.method == 'POST':
        username = request.POST.get('username', '')
        task_id = request.POST.get('id', '')

        url = 'http://127.0.0.1:8000/api/v1/todo/delete/'
        body_param = {'id': task_id}

        res = requests.post(url, data=body_param)
        if res.status_code == 200:

            # Calling Todo list API
            url = 'http://127.0.0.1:8000/api/v1/todo/get_user_list/'
            body_param = {'username': username}

            res = requests.get(url, data=body_param)
            if res.status_code == 200:
                result = json.loads(res.text)
                todo_list = result
        else:
            print("Something went wrong!!")

    else:
        print("Invalid Request!!")

    context['todo_list'] = todo_list
    return render(request, 'todoList.html', context=context)