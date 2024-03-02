from django.shortcuts import render

# Create your views here.

def view_expenses(request):

    # write the data base logic

    context = dict()
    return render(request,'expenses.html',context)
