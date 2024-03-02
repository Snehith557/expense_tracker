from django.shortcuts import render

# Create your views here.


def view_investments(request):

    # fetch the data from the data base related to the expenses and render it 
    context = dict()
    return render(request,'investments.html',context)