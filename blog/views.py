from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from django.utils import timezone
from django.shortcuts import render, get_object_or_404

class IndexView(generic.ListView):
	template_name='blog/index.html'
	context_object_name='all_products'

	def get_queryset(self):
		return Product.objects.all()

class DetailView(generic.DetailView):
	model=Product
	template_name='blog/detail.html'

class ProductCreate(CreateView):
	model=Product
	fields=['pname','product_id','price','quantity','product_type','brand_name','mrp','expiry','vat','effective_price']

class ProductUpdate(UpdateView):
	model=Product
	fields=['pname','product_id','price','quantity','product_type','brand_name','mrp','expiry','vat','effective_price']

class ProductDelete(DeleteView):
	model=Product
	success_url=reverse_lazy('index') #what's this for??

def login(request):
	return render(request, 'blog/login.html')

class Signup(CreateView):
	model=User
	fields=['name'.'adm_no','phone_no','password','cbid']

def signup(request):
	return render(request,'blog/signup.html')

def logout(request):
	request.session['logid']='' #wats this for
	request.session['vericode']=''
	return HttpResponseRedirect('/app') #where'z app??

def loginprocess(request):
	adm_no=request.POST.get("username","") #WATS IT FOOORRRR
	password=request.POST.get("password","")
	if(len(adm_no) == 0 and len(password) == 0):
		return render(request,'blog/login.html', {'loginmessage' : ''})
	user_data = user_data = User.objects.all().filter(adm_no)
	got = True
	for e in user_data:
		got = False
	if(got):
		return render(request,'blog/login.html',{'loginmessage' : 'Email id does not exist please signup '})
	for e in user_data:
		if(e.password != password):
			return render(request, 'blog/login.html')