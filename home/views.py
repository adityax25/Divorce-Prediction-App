from django.shortcuts import render,redirect
from .models import Data
from django.views.decorators.csrf import csrf_exempt
import pickle

#model import
model = pickle.load(open('./divorce_prediction/model/adaboost.pkl', 'rb'))
#questions import
questions = [x.strip() for x in open('./divorce_prediction/model/questions.txt')]


def index(request):
    return render(request,"index.html")

def form(request):
    return render(request,"form.html",{"questions":questions})

@csrf_exempt
def result(request):
    if request.method=="POST":
        data = [int(x) for x in list(dict(request.POST.items()).values())]
        outcome = model.predict([data])
        new_data = Data(prediction=outcome)
        new_data.set_data(data)
        new_data.save()
        if 1 in outcome:
            return render(request,"result.html")
        else:
            return render(request,"result2.html")
    else:
        return redirect("form")