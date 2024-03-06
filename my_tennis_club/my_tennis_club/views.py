from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from  .forms import NameForm
from service.models import Service
from news.models import News
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
      
      return render(request,"contact.html")
def serviceUs(request):
      serviceData = Service.objects.all()
      if request.method=='GET':
            str = request.GET.get('search')
            if str != None:
                  serviceData = Service.objects.filter(service_title__icontains=str)
                  
      return render(request,"service.html",{'serviceData':serviceData})

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
     
def NewsData(request,newsid):
      NewsData = News.objects.get(id=newsid);
      return render(request,'NewsData.html',{'NewsData':NewsData})
                  
                  
# how to pass dynamic links example below start
# def contactUs(request,courseid):
#       return HttpResponse(courseid)  
# how to pass dynamic links example below end

