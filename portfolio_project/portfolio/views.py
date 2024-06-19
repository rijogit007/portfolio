from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.urls import reverse_lazy
from .models import Portfolio
from .forms import PortfolioForm, CustomUserCreationForm,UserLoginForm
from django.views.generic import TemplateView
from django.views import View
from django.contrib.auth import authenticate,login,logout
# Create your views here.



class HomeView(TemplateView):
    template_name='home.html'


class PortfolioListView(LoginRequiredMixin, ListView):
    model = Portfolio
    template_name = 'view_portfolio.html'
    context_object_name = 'portfolios'

    def get_queryset(self):
        return Portfolio.objects.filter(user=self.request.user)

class PortfolioCreateView(LoginRequiredMixin, CreateView):
    model = Portfolio
    template_name = 'create_portfolio.html'
    form_class = PortfolioForm
    success_url = reverse_lazy('view_portfolio')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PortfolioUpdateView(LoginRequiredMixin, UpdateView):
    model = Portfolio
    template_name = 'edit_portfolio.html'
    form_class = PortfolioForm
    success_url = reverse_lazy('view_portfolio')

class PortfolioDeleteView(DeleteView):
    model = Portfolio
    success_url = reverse_lazy('view_portfolio')
    pk_url_kwarg='id'
    template_name='delete.html'

class UserRegisterView(CreateView):
    template_name = 'register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')

class UserLoginView(View):
    def get(self,request):
        form = UserLoginForm()
        return render(request,'login.html',{'form':form})
    
    def post(self,request):
        uname = request.POST.get("username")
        psw = request.POST.get("password")
        user = authenticate(request,username=uname,password=psw)
        if user:
            login(request,user)
          
            return redirect('home2')
        else:
            
            return redirect('login')

class Logout(View):
    
    def get(self,request):
        logout(request)
        return redirect('home')
        

class Viewportfolio(DetailView):
      template_name='view.html'
      model = Portfolio
      pk_url_kwarg = 'id'
      context_object_name = 'portfolio'
      
class Home2(TemplateView):
    template_name='home2.html'
    
        
    