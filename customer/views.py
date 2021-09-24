import json
from django.shortcuts import render, redirect
from django.views import View
from django.db.models import Q
from django.core.mail import send_mail
from .models import MenuItem, Category, OrderModel, CanteenList, Availability
from django.template.loader import render_to_string
from django.utils.html import strip_tags

class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/index.html')


class About(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/about.html')

class RestaurantLogin(View):
    def get(self, request, *args, **kwargs):
        return render(request,'restaurant/dashboard.html')

class Menu(View):
    def get(self, request, *args, **kwargs):
        menu_items = MenuItem.objects.all()

        context = {
            'menu_items': menu_items
        }

        return render(request, 'customer/menu.html', context)



class Order(View):
    def get(self, request, *args, **kwargs):

        appetizers = MenuItem.objects.filter(category__name__contains='Appetizer')
        entres = MenuItem.objects.filter(category__name__contains='Entre')
        desserts = MenuItem.objects.filter(category__name__contains='Dessert')
        drinks = MenuItem.objects.filter(category__name__contains='Drink')


        context = {
            'appetizers': appetizers,
            'entres': entres,
            'desserts': desserts,
            'drinks': drinks,
        }


        return render(request, 'customer/order.html', context)

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        email = request.POST.get('email')


        order_items = []



        


        items = request.POST.getlist('items[]')
        canteen_wise_data={}

        for item in items:

            menu_item = MenuItem.objects.get(pk=(int(item)))
            item_data = {
                'id': menu_item.pk,
                'name': menu_item.name,
                'price': menu_item.price,
                'canteen':menu_item.canteen

            }


            if menu_item.canteen.name in canteen_wise_data:
                canteen_wise_data[menu_item.canteen.name] += menu_item.price
            else:
                canteen_wise_data[menu_item.canteen.name] = menu_item.price


            order_items.append(item_data)

        price = 0


        for cant in canteen_wise_data:
            if canteen_wise_data[cant] != 0:
                price+=canteen_wise_data[cant]
                
        item_ids=[]
        for item in order_items:
            item_ids.append(item['id'])
        order = OrderModel.objects.create(

            price=price,
            name=name,
            email=email

        )
        order.items.add(*item_ids)
        print(canteen_wise_data)

        body = ('Thank you for your order! Your food is being made and will be delivered soon!\n'
                f'Your total: {price}\n'
                'Thank you again for your order!')
        html_message = render_to_string('customer/mail.html', {'price': price,'canteen': canteen_wise_data} )




        send_mail(
            'Thank You For Your Order!',
            body,
            'example@example.com',
            [email],
            html_message = html_message,

            fail_silently=False
        )

        for cant in canteen_wise_data:
            cant_obj=CanteenList.objects.get(name=cant)
            ordered_cant_items=[]
            for ord in order_items:
                if ord['canteen']==cant_obj:
                    
                    cant_data={
                        'item': ord['name'],
                        'price': ord['price']
                    }
                    ordered_cant_items.append(cant_data)
            body = ('We got an order for you' )

            html_message1 = render_to_string('customer/cantmail.html', {'menu_item': ordered_cant_items, 'name': name, 'total_price':canteen_wise_data[cant]})
            send_mail(
                'Order for You!',
                body,
                'example@example.com',
                [cant_obj.email],
                html_message=html_message1,

                fail_silently=False
            )






        return redirect('order-confirmation', pk=order.pk)


class OrderConfirmation(View):
    def get(self, request, pk, *args, **kwargs):
        order = OrderModel.objects.get(pk=pk)

        context = {
            'pk': order.pk,
            'items': order.items,
            'price': order.price,
        }

        return render(request, 'customer/order_confirmation.html', context)

    def post(self, request, pk, *args, **kwargs):
        data = json.loads(request.body)

        if data['isPaid']:
            order = OrderModel.objects.get(pk=pk)
            order.is_paid = True
            order.save()

        return redirect('payment-confirmation')


class OrderPayConfirmation(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/order_pay_confirmation.html')


class MenuSearch(View):
    def get(self, request, *args, **kwargs):
        query = self.request.GET.get("q")

        menu_items = MenuItem.objects.filter(
            Q(name__icontains=query) |
            Q(price__icontains=query)

            # Q(availability__icontains=query)
        )

        context = {
            'menu_items': menu_items
        }

        return render(request, 'customer/menusearch.html', context)


