import stripe
from django.shortcuts import render, redirect
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY


def checkout(request):
    if request.method == 'POST':
        # Get the amount to be charged from the form data
        amount = request.POST['amount']

        # Create a Stripe Checkout session
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'name': 'My Item',
                'description': 'Description of my item',
                'amount': amount,
                'currency': 'usd',
                'quantity': 1,
            }],
            success_url=request.build_absolute_uri(
                reverse('success')) + '?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=request.build_absolute_uri(reverse('cancel')),
        )

        # Redirect the user to the Stripe Checkout page
        return redirect(session.url)
    else:
        return render(request, 'checkout.html')


def success(request):
    session_id = request.GET['session_id']

    # Retrieve the Stripe Checkout session
    session = stripe.checkout.Session.retrieve(session_id)

    # Verify the payment
    payment_intent = stripe.PaymentIntent.retrieve(session.payment_intent)
    if payment_intent.status == 'succeeded':
        # Payment succeeded, do something here
        return render(request, 'success.html')
    else:
        # Payment failed, do something here
        return render(request, 'failure.html')


def cancel(request):
    return render(request, 'cancel.html')
