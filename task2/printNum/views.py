from django.shortcuts import render

# Create your views here.

def index(request):
    if(request.method == 'POST'):
        data = request.POST.dict()
        number = int(data.get("number"))
        if(number>0 and number<=500):
            num_list = []
            for i in range(number):
                num_list.append(i+1)
            return render(request, 'printNum/index.html', {"num_list": num_list})
        else:
            message = {'message': "Enter Number between 1 to 500"}
            return  render(request, 'printNum/index.html', message)
    else:
        return render(request, 'printNum/index.html')