from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from Base_App.models import BookTable, AboutUs, Feedback, ItemList, Items, Order
from django.contrib import messages
# Create your views here.

def HomeView(request):
    items =  Items.objects.all()
    list = ItemList.objects.all()
    review = Feedback.objects.all()
    return render(request, 'home.html',{'items': items, 'list': list, 'review': review})


def AboutView(request):
    data = AboutUs.objects.all()
    return render(request, 'about.html',{'data': data})


def MenuView(request):
    items =  Items.objects.all()
    list = ItemList.objects.all()
    return render(request, 'menu.html', {'items': items, 'list': list})


def order_item(request, item_id):
    item = get_object_or_404(Items, id=item_id)

    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        customer_name = request.POST.get('customer_name')
        contact_number = request.POST.get('contact_number')
        address = request.POST.get('address')
        pincode = request.POST.get('pincode')


        order = Order.objects.create(
            item=item,
            quantity=quantity,
            customer_name=customer_name,
            contact_number=contact_number,
            address=address,
            pincode=pincode
        )
        messages.success(request, 'Your order has been successfully placed!')

        return redirect('order_confirmation', order_id=order.id)



    context = {
        'item': item,
    }
    return render(request, 'order.html', context)



def order_confirmation(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'order_confirmation.html', {'order': order})


def BookTableView(request):
    if request.method == 'POST':
        name = request.POST.get('user_name')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('user_email')
        total_person = request.POST.get('total_person')
        booking_data = request.POST.get('booking_data')

        if name != '' and len(phone_number) == 10 and email != '' and total_person != 0 and booking_data != '':
            data = BookTable(Name=name, Phone_number=phone_number, Email=email,
                             Total_person=total_person, Booking_date=booking_data)
            data.save()

            return render(request, 'book_table.html', {'success': True})

    return render(request, 'book_table.html')



def FeedbackView(request):
    if request.method == 'POST':
        name = request.POST.get('user_name')
        description = request.POST.get('Description')
        rating = request.POST.get('total_person')
        image = request.FILES.get('image')  # For image file

        if name and description and rating:
            feedback = Feedback(Name=name, Description=description, Rating=rating, Image=image)
            feedback.save()

            # Pass a success flag to the template
            return render(request, 'feedback.html', {'success': True})

    return render(request, 'feedback.html')
