from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin  # New

from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views.generic import ListView, DetailView

from .forms import CommentForm, VechicleForm
from .models import models, VechicleByCustomer
from .models import Client, Comment
from django.urls import reverse_lazy
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.translation import ugettext as _


class ClientListView(LoginRequiredMixin, ListView):
    model = Client
    template_name = 'client_list.html'


class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client
    template_name = 'client_detail.html'
    login_url = 'login'


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    fields = ('name', 'notes', 'address', 'city', 'state', 'zipcode', 'email', 'cell_phone', 'acct_number')
    template_name = 'client_edit.html'


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    template_name = 'client_delete.html'
    success_url = reverse_lazy('client_list')


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'change_password.html', args)


def comment(request, pk):
    post = get_object_or_404(Client, pk=pk)

    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            comment = comment_form.save(commit=False)
            # Assign the current post to the comment

            comment.client = post
            comment.author = request.user
            comment.comment = comment.comment
            # Save the comment to the database
            comment.save()
            # print(comment.client)
            # messages.success(request, 'your  comment has been posted')
            return redirect('client_detail', pk=post.pk)
    else:
        comment_form = CommentForm()
    new_content = {'comment_form': comment_form}

    return render(request, 'comment.html', new_content)


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    template_name = 'client_new.html'
    fields = ('name', 'notes', 'address', 'city', 'state', 'zipcode', 'email', 'cell_phone', 'acct_number')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# vechicles

class VechicleListView(LoginRequiredMixin, ListView):
    model = VechicleByCustomer
    template_name = 'vechicle_list.html'


class VechicleDetailView(LoginRequiredMixin, DetailView):
    model = VechicleByCustomer
    template_name = 'vechicle_detail.html'
    login_url = 'login'


class VechicleUpdateView(LoginRequiredMixin, UpdateView):
    model = VechicleByCustomer
    fields = ('client', 'make', 'model', 'vin_number', 'Date_Of_Purchase',
              'Date_Of_LastService')
    # vechicle_form = VechicleForm
    template_name = 'vechicle_edit.html'
    success_url = reverse_lazy('vechicle_list')


class VechicleDeleteView(LoginRequiredMixin, DeleteView):
    model = VechicleByCustomer
    template_name = 'vechicle_delete.html'
    success_url = reverse_lazy('vechicle_list')


class VechicleCreateView(LoginRequiredMixin, CreateView):
    model = VechicleByCustomer
    template_name = 'vechicle_new.html'
    # vechicle_form = VechicleForm
    fields = ('client', 'make', 'model', 'vin_number', 'Date_Of_Purchase',
              'Date_Of_LastService')
    login_url = 'login'
    success_url = reverse_lazy('vechicle_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

