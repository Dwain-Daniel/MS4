from django.shortcuts import render, redirect


def view_bag(request):
    return render(request, 'bag/bag.html')


def add_to_bag(request, workouts_id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if workouts_id in list(bag.keys()):
        bag[workouts_id] += quantity
    else:
        bag[workouts_id] = quantity

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)