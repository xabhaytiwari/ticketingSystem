import random
import string
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth import get_user_model
from .form import CreateTicketForm, AssignTicketForm
from .models import Ticket

User = get_user_model()

def create_ticket(request):
    if request.method == 'POST':
        form = CreateTicketForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.customer = request.user
            while not var.ticket_id:
                id = ''.join(random.choices(string.digits, k = 6))
                try:
                    var.ticket_id = id
                    var.save()
                    subject = f'{var.ticket_title} #{var.ticket_id}'
                    message = 'Thank you for creating a ticket, we will assign an engineer soon.'
                    email_from = 'G.ONE@email.com'
                    recipient_list = [request.user.email, ]
                    send_mail(subject, message, email_from, recipient_list)
                    messages.success(request, 'Your ticket has been submitted. A Support Engineer would reach out soon. ')    
                    return redirect('customer-active-tickets')
                except IntegrityError:
                    continue
        else:
            messages.warning(request, 'Something went wrong. Check form for errors!')
            return redirect('create-ticket')
    else:
        form = CreateTicketForm()
        context = {'form' : form} 
        return render(request, 'ticket/create_ticket.html', context)   

def customer_active_tickets(request):
    tickets = Ticket.objects.filter(customer=request.user, is_resolved=False).order_by('-created_on')
    context = {'tickets': tickets}
    return render(request, 'ticket/customer_active_tickets.html', context)


def customer_resolved_tickets(request):
    tickets = Ticket.objects.filter(customer=request.user, is_resolved=True).order_by('-created_on')
    context = {'tickets': tickets}
    return render(request, 'ticket/customer_resolved_tickets.html', context)


def engineer_active_tickets(request):
    tickets = Ticket.objects.filter(engineer=request.user, is_resolved=False).order_by('-created_on')
    context = {'tickets': tickets}
    return render(request, 'ticket/engineer_active_tickets.html', context)


def engineer_resolved_tickets(request):
    tickets = Ticket.objects.filter(engineer=request.user, is_resolved=True).order_by('-created_on')
    context = {'tickets': tickets}
    return render(request, 'ticket/engineer_resolved_tickets.html', context)

def assign_ticket(request, ticket_id):
    ticket = Ticket.objects.get(ticket_id = ticket_id)
    if request.method == 'POST':
        form = AssignTicketForm(request.POST, instance = ticket)
        if form.is_valid():
            var = form.save(commit = False)
            var.is_assigned_to_engineer = True
            var.status= 'Active'
            var.save()
            messages.success(request, f'Ticket has been assigned to {var.engineer}')
            return redirect('ticket-queue')
        else:
            messages.warning(request, 'Something went wrong. Please check form for errors')
            return redirect('assign-ticket')
    else:
        form = AssignTicketForm(instance=ticket)
        form.fields['engineer'].queryset = User.objects.filter(is_engineer=True)
        context = {'form': form, 'ticket': ticket}
        return render(request, 'ticket/assign_ticket.html', context)    
    
    
def ticket_details(request, ticket_id):
    ticket = Ticket.objects.get(ticket_id=ticket_id)
    context = {'ticket':ticket}
    return render(request, 'ticket/ticket_details.html', context)

def ticket_queue(request):
    tickets = Ticket.objects.filter(is_assigned_to_engineer = False)
    context = {'tickets' : tickets}
    return render(request, 'ticket/ticket_queue.html', context)