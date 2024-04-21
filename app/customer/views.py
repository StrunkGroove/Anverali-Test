from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .models import Customer, Task
from .forms import InfoForm, AddTask
from freelancer.models import Freelancer


@login_required
def main(request):
    return render(request, 'customer/main.html')


@login_required
def profile(request):
    customer_instance, created = Customer.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = InfoForm(request.POST, instance=customer_instance)
        if form.is_valid():
            form.save()
            return redirect('customer-main')
    else:
        form = InfoForm(instance=customer_instance)
    return render(request, 'customer/profile.html', {'form': form})


@login_required
def freelancers(request):
    records = Freelancer.objects.exclude(user=request.user)
    return render(request, 'customer/freelancers.html', {'records': records})


@login_required
def tasks(request):
    customer_instance = Customer.objects.get(user=request.user)
    records = Task.objects.filter(customer=customer_instance)
    if request.method == 'POST':
        form = AddTask(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.customer = customer_instance
            task.save()
            return redirect('add-task')
    else:
        form = AddTask(initial={'customer': customer_instance})
    return render(request, 'customer/tasks.html', {'form': form, 'records': records})


@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = AddTask(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('add-task')
    else:
        form = AddTask(instance=task)
    return render(request, 'customer/edit_task.html', {'form': form})


@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('add-task')
    return render(request, 'customer/delete_task.html', {'task': task})