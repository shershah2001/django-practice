from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from  .forms import NameForm
from service.models import Service
from news.models import News
from django.core.paginator import Paginator
from contact.models import Contact

# from .forms import userform
def home(request):
      NewsData = News.objects.all();
      print(NewsData)
      ServiceData = Service.objects.all().order_by('-id')[:3] # order_by use to change the direction of query from ascending to decendign. and object.all to retrive the value from database.
      # for n in ServiceData:
      #       print(n.service_icon)
      data={
            "response":ServiceData,
            'NewsData':NewsData
      }
      
      return render(request,"index.html",data)
#     data={
#           "title":"Home Page",
#           "bdata":"Hello shershah, what are you doing",
#           "numbers":[10,20,30,40,50],
#           "datatemplate":["javascript","python","rust","solidity","oops"],
#           "dicData":[
#                 {"name":"shershah","phoneNumber":8076588017},
#                 {"name":"rohit","phoneNumber":9821468154}
#           ]
#     }

def aboutUs(request):
      # if request.method == "GET":
      #    output = request.GET.get("output")
      # return render(request,"about.html",{"output":output})
      if request.method =="GET":
            output = request.GET.get("output")
            return render(request,'about.html',{"output":output})

def contactUs(request):
      if request.method=="POST":
            username=request.POST.get('username')
            email=request.POST.get('email')
            password=request.POST.get('password')
            address=request.POST.get('address')
            address_2=request.POST.get('address_2')
            city=request.POST.get('city')
            state=request.POST.get('state')
            zip_num=request.POST.get('zip')
            comments=request.POST.get('comments')
            data = Contact(username=username,email=email,password=password,address=address,address2=address_2,city=city,state=state,zip_num=zip_num,comments=comments)
            data.save()
      return render(request,"contact.html")

def serviceUs(request):
      serviceData = Service.objects.all()
      paginator = Paginator(serviceData,2)
      page_number = request.GET.get('page')
      serviceDatafinal = paginator.get_page(page_number)
      totalPage = serviceDatafinal.paginator.num_pages
     
      
      if request.method=='GET':
            search_query  = request.GET.get('search')
            if search_query != None:
                  serviceData = Service.objects.filter(service_title__icontains=search_query)
                  #how to use #filter method to for making searching functionality and if you use this method 
                  #__icontainss then you can find any thing in the search functionality by typing #single word;
                  paginator = Paginator(serviceData,2)
                  serviceDatafinal = paginator.get_page(page_number)
      data={
            # 'serviceData':serviceData, 
            # firstly in this codes i am using serviceData to get the #search data but now i am #modifying this codes because i want to use search functionality with pagination #that why in this last i am passing serviceData  to  paginator and i am not writing #page_number again in the if condition because search query one time is enough for #this codes.
            'serviceDatafinal':serviceDatafinal,
            'lastPage':totalPage,
            'page_number':page_number,
            'totalpageNumber':[n+1 for n in range(totalPage)]# i am doing this to get number of #pages for numberical pagination this method is not wrote into the django offical #document
      }           
                  
      return render(request,"service.html",data)

def userForm(request):
      # finalValue = 0
      # data={}
      # try:
      #       if(request.method =="POST"):
      #              n1 = eval(request.POST.get('num1'));
      #              n2 = eval(request.POST.get('num2'));
      #              finalValue = n1 + n2
      #              data={
      #                    "n1":n1,
      #                    "n2":n2,
      #                    "output":finalValue
      #              }
      #              url="/about-us/?output={}".format(finalValue)
                  #  you can also use this redirect method to redirect from one page to another
                  #  return redirect(url)
                  #  return HttpResponseRedirect(url)
                  #  how to redirect using HttpResponseRedirect;
            # return HttpResponseRedirect('/about-us/')
            
      # except:
      #       pass 
      # return render(request,"userForm.html",data)
      
      finalValue = 0
      fn=NameForm()
      data={'form':fn}
      try:
            if(request.method=="POST"):
                  n1 = eval(request.POST.get('num1'))
                  n2 = eval(request.POST.get('num2'))
                  finalValue= n1 +n2
                  data={
                         "n1":n1,
                         "n2":n2,
                         "output":finalValue,
                         'form':fn
                         }
                  url = '/about-us/?output={}'.format(finalValue)
                  # return HttpResponseRedirect(url)
                  return redirect(url)
      except:
            pass
      return render(request,'userForm.html',data)
      
    
# def submitForm(request):
#       try:
#             if(request.method=='POST'):
#                   n1 = eval(request.POST.get('num1'))
#                   n2 = eval(request.POST.get('num2'))
#                   finalValue = n1+n2
#                   return HttpResponse(finalValue)
#       except:
#             pass
                  
def submitForm(request):
      try:
            if request.method =="POST":
                  n1 = eval(request.POST.get('num1'))
                  n2 = eval(request.POST.get("num2"))
                  finalValue = n1 +n2
                  return HttpResponse(finalValue)
      except:
            pass
                  
                  
def login(request):
       return  render (request,"login.html")
 
def  backhand_index(request):
      return render(request,"backhandIndex.html")

def conection(request):
    return render(request,'members/admin.py')

def calculator(request):
      n=""
      even_odd=''
      try:
          if  request.method=='POST':
                  n1 = eval(request.POST.get('num1'))
                  n2 = eval(request.POST.get('num2'))
                  opr  = request.POST.get('opr')
                  even_odd = request.POST.get('even_odd')
                  if opr == '+':
                        n=n1+n2
                  elif opr =='-':
                        n=n1-n2
                  elif opr =='*':
                        n=n1*n2 
                  elif opr =='/':
                        n=n1/n2
                  if n%2 == 0:
                        even_odd="even value"
                  else:
                        even_odd="odd value"
                        
      except Exception as e:
            print(e)
            n='invalid opr'       
      return render(request,'calculator.html',{'n':n,'even_odd':even_odd})    
     
def NewsData(request,slug):
      NewsData = News.objects.get(news_slug=slug);
      return render(request,'NewsData.html',{'NewsData':NewsData})
                  
                  
# how to pass dynamic links example below start
# def contactUs(request,courseid):
#       return HttpResponse(courseid)  
# how to pass dynamic links example below end

