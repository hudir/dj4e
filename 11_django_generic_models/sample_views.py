# from django import View 
# from Cat_model import Cat

# class CatListView(View):
#     def get(self, request):
#         stuff = Cat.objects.all()
#         cntx = { 'cat_list': stuff}
#         return render(request, 'gview/cat_list.html', cntx)
    
# class DogListView(View):
#     model = DogListView
#     def get(self, request):
#         modelname = self.model._meta.verbose_name.title().lower()
#         stuff = self.model.objects.all()
#         cntx = { modelname: stuff}
#         return render(request, 'gview/' + modelname +'_list.html', cntx)
    

# from django.views import generic
# class HorseListView(generic.ListView):
#     model = Horse