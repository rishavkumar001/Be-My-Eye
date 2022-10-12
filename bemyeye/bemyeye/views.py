# from django.http import HttpResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from information.models import Information
from django.core.paginator import Paginator
from information.models import Information

def homePage(request):

    # for product in informationData:
    #     print(product.product_name)
    informationData = Information.objects.all()
    if request.method == "GET":
        st = request.GET.get('titlesearch')
        if st != None:
            informationData = Information.objects.filter(product_name__icontains = st)

    paginator = Paginator(informationData, 5) # adding LIMIT to the add
    page_number = request.GET.get('page') # to get from URL that which page number we are at (*By default it is set to 1*)
    informationDataFinal = paginator.get_page(page_number) # which page number data you want to show
    totalPages = informationDataFinal.paginator.num_pages # returns the total number of pages

    obj = "Text From Views"

    data = {
        'informationData':informationDataFinal,
        'lastPage':totalPages,
        'obj':obj,
        'totalPageList':[i + 1 for i in range(totalPages)]
    }
    return render(request, "index.html", data)

def submitform(request):
    try:
        Ftitle = ""
        FcompanyName = ""
        Fdescription = ""
        Fcost = 0
        FmanuDate = ""
        FexpDate = ""
        data = {}
        if request.method == "POST":
        # title = int(request.GET.get('title'))
            title = request.POST['title']
            company = request.POST['company']
            description = request.POST['description']
            cost = request.POST['cost']
            manudate = request.POST['manudate']
            expdate = request.POST['expdate']
            Ftitle = title
            FcompanyName = company
            Fdescription = description
            Fcost = cost
            FmanuDate = manudate
            FexpDate = expdate
            data = {'Ftitle': Ftitle, 'FcompanyName':FcompanyName, 'Fdescription':Fdescription, 'Fcost':Fcost, 'FmanuDate':FmanuDate, 'FexpDate':FexpDate}
            # return HttpResponse(Ftitle + " " + FcompanyName + " " + Fdescription + " " + Fcost + " " + FmanuDate + " " + FexpDate)
            return render(request, "index.html", data)
    except:
        pass

def saveInformation(request):
    if request.method == "POST":
        title = request.POST.get('title')
        company = request.POST.get('company')
        description = request.POST.get('description')
        cost = request.POST.get('cost')
        manudate = request.POST.get('manudate')
        expdate = request.POST.get('expdate')

        info = Information(product_name = title, company_name = company, product_description = description, product_cost = cost, manu_date = manudate, exp_date = expdate)
        info.save() # This line will save the data in the Database

        return HttpResponseRedirect('/')

def aboutUs(request):
    return render(request, "about.html")