from django.shortcuts import render,redirect

# Create your views here.



def set_budget(request):
    if request.method == "POST":
        # update the data base
        pass


    return render(request,'budget_form.html')

def previous_budget(request):
    # viewing the previous budgets

    if request.method == "GET":
        # get the data from the data base and pass it has context
        context = dict()

        return render(request,'previous_budgets.html',context)
    

def submit_budget(request):

    return redirect('/')
    