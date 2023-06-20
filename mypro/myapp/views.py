from django.shortcuts import render

# Create your views here.


def Areaofrectangle(request):
    context = {}
    context['length'] = "0"
    context['breadth'] = "0"

    context['Area'] = "0"
    if request.method == 'POST':
        print("POST method is used . . .")
        length = request.POST.get("length", 0)
        breadth = request.POST.get("breadth", 0)

        l_num = int(length)
        b_num = int(breadth)

        Area = l_num*b_num
        context['length'] = length
        context['breadth'] = breadth

        context['Area'] = Area
    return render(request, "myapp/area.html", context)
