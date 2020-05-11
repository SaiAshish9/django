from django.http import HttpResponse
from .models import Item
from django.template import loader
from django.shortcuts import render,redirect
from .forms import ItemForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView



# Create your views here.

def item(request):
    return HttpResponse('This is an item view ')

def detail(request,item_id):
    item=Item.objects.get(pk=item_id)
    context={
        'item':item,
    }
    # return HttpResponse("This is item no/id: %s"%item_id)
    return render(request, 'food/detail.html ',context)

class FoodDetail(DetailView):
      model=Item
      template_name='food/detail.html'





def update_item(request,id):
    item=Item.objects.get(id=id)
    form=ItemForm(request.POST or None,instance=item)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request,'food/item-form.html',{'form':form,'item':item})

def delete_item(request,id):
    item=Item.objects.get(id=id)

    if request.method =='POST':
        item.delete()
        return redirect('food:index')
    
    return render(request,'food/item-delete.html',{'item':item})

#function based view
def index(req):
    item_list=Item.objects.all()
    template = loader.get_template('food/index.html')
    context ={
       'item_list': item_list,
    }
    # return HttpResponse(template.render(context,req))
    return render(req, 'food/index.html ',context)


class CreateItem(CreateView):
    model=Item;
    fields=['item_name','item_desc','item_price','item_image']
    template_name='food/item-form.html'    
    success_url = '/food'


    def form_valid(self,form):
        form.instance.user=self.request.user
        return super().form_valid(form)



def create_item(request):
    form=ItemForm(request.POST or None)
    if form.is_valid():
        form.instance.user_name='hi'
        form.save()
        return redirect('food:index')

    return render(request, 'food/item-form.html',{'form':form,'user':request.user})




#class based view
# .as_view()
class IndexClassView(ListView):
    model=Item;
    template_name='food/index.html'
    context_object_name='item_list'


