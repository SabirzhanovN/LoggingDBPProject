from django.db import connection
from django.shortcuts import render, redirect
from .service import send_message, client
from shopApp.models import LoggingMoves


def payment(request):
    return render(request, 'payment/payment.html')


def replenish_verdict(request):
    if request.method == 'POST':
        cash = request.POST['cash']

        if int(cash) > 0:
            message = (f"Payment for {request.user.username}\n"
                       f"From IP: {request.META.get('REMOTE_ADDR')}\n"
                       f"Email: {request.user.email if request.user.email else 'unknown'}\n"
                       f"{cash}$\n\n"
                       f"Confirm?")

            send_message(message)

        user = request.user
        user.balance = user.balance + int(cash)
        query1 = connection.queries[-1]['sql']

        user.save()
        query2 = connection.queries[-1]['sql']

        new_log = LoggingMoves.objects.create(
            ip_address=request.META.get('REMOTE_ADDR'),
            author=user.username,
            method='UPDATE',
            sql_query=f'{query1};\n{query2};',
            path=request.get_full_path(),
            verdict='SUCCESS',
            email=request.user.email
        )
        new_log.save()

        client.polling()

    return redirect('payment')

