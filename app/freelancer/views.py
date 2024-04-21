from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.db.models import Q

from .models import Freelancer, Direction
from .forms import InfoForm
from customer.models import Task as CustomerTask


@login_required
def main(request):
    return render(request, 'freelancer/main.html')


@login_required
def profile(request):
    freelancer_instance, created = Freelancer.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = InfoForm(request.POST, instance=freelancer_instance)
        if form.is_valid():
            form.save()
            return redirect('freelancer-main')
    else:
        form = InfoForm(instance=freelancer_instance)
    return render(request, 'freelancer/profile.html', {'form': form})


@login_required
def works(request):
    records = CustomerTask.objects.exclude(customer=request.user.customer)

    filters = Q()

    directions = request.GET.getlist('directions')
    if directions:
        filters &= Q(directions__name__in=directions)

    min_amount = request.GET.get('min_amount')
    if min_amount:
        filters &= Q(amount__gte=min_amount)

    max_amount = request.GET.get('max_amount')
    if max_amount:
        filters &= Q(amount__lte=max_amount)

    records = records.filter(filters)

    return render(
        request,
        'freelancer/works.html',
        {'records': records, 'filters': Direction.objects.all()}
    )