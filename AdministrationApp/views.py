from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from datetime import datetime, timedelta, time
from django.contrib.auth.models import User
from . import models
from django.views import generic
from django.views.generic import DetailView, CreateView
from LoginApp.forms import SignUpForm
from django.urls import reverse_lazy
from AdministrationApp.forms import GalleryForm, DoctorsForm, FeedbackForm, ShopForm

def ErrorSubmit(request):
    html = 'administration/error.html'
    return render(request,html,{'today_date':datetime.today().date()})


@login_required(login_url='administration_login')
def DashboardView(request):
    yT = models.QuickAppointment.objects.filter(flag=True).count()
    yF = models.QuickAppointment.objects.filter(flag=False).count()
    xT = models.Appointment.objects.filter(flag=True).count()
    xF = models.Appointment.objects.filter(flag=False).count()
    msg = models.Messages.objects.all().count()
    todo_count = models.Todo.objects.all().count()
    notes_count = models.Notes.objects.all().count()

    today_date = datetime.today().date()
    todat1 = models.PatentRegistration.objects.filter(booking_date=today_date,flag=False)
    todat2 = models.QuickAppointment.objects.filter(booking_date=today_date,flag=False)
    todat3 = models.Appointment.objects.filter(booking_date=today_date,flag=False)
    
    tomorrow_date = today_date + timedelta(1)
    tomorrow1 = models.PatentRegistration.objects.filter(booking_date=tomorrow_date,flag=False)
    tomorrow2 = models.QuickAppointment.objects.filter(booking_date=tomorrow_date,flag=False)
    tomorrow3 = models.Appointment.objects.filter(booking_date=tomorrow_date,flag=False)
    
    today_count1 = todat1.count()
    today_count2 =  todat2.count()
    today_count3 =  todat3.count()
    today_count = today_count1 + today_count2 + today_count3
    
    tomorrow_count1 = tomorrow1.count()
    tomorrow_count2 = tomorrow2.count()
    tomorrow_count3 = tomorrow3.count()
    tomorrow_count = tomorrow_count1 + tomorrow_count2 + tomorrow_count3
    
    if todat1 or todat2 or todat3:
        todayFlag = 1
    else:
        todayFlag = 0

    if tomorrow1 or tomorrow2 or tomorrow3:
        tomorrowFlag = 1
    else:
        tomorrowFlag = 0

    context = {
        'yT':yT, 'yF':yF,
        'xT':xT, 'xF':xF,
        'msg':msg,
        'todayFlag': todayFlag, 
        'tomorrowFlag' : tomorrowFlag,
        'today_count' : today_count,
        'tomorrow_count' : tomorrow_count,
        'todo_count' : todo_count,
        'notes_count' : notes_count,
        'today_date':datetime.today().date()
    }
    html = 'administration/dashboard.html'
    return render(request,html,context)


def PatentRegistrationView(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        remark = request.POST.get('remark')
        place = request.POST.get('place')
        mobile = request.POST.get('mobile')
        other_contact = request.POST.get('other_contact')
        booking_date = request.POST.get('booking_date')
        submit_date = datetime.today().date()
        flag = False

        obj_1 = models.PatentRegistration()
        obj_1.name = name
        obj_1.age = age
        obj_1.remark = remark
        obj_1.place = place
        obj_1.mobile = mobile
        obj_1.other_contact = other_contact
        obj_1.booking_date = booking_date
        obj_1.submit_date = submit_date
        obj_1.flag = flag

        if mobile == '' or name == '' or booking_date == '':
            return redirect('error')
        else:
            obj_1.save()
            return redirect('patent_table')
    context = {'today_date':datetime.today().date()}
    html = 'administration/forms/patent_registration.html'
    return render(request,html,context)


def PatentTableView(request):
    data = models.PatentRegistration.objects.all().order_by('-id')
    context = {
        'data':data,
        'today_date':datetime.today().date()
    }
    html = 'administration/tables/patent_registration_table.html'
    return render(request,html,context)


def PatentEditView(request,id):
    data = models.PatentRegistration.objects.get(id=id)
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        remark = request.POST.get('remark')
        place = request.POST.get('place')
        mobile = request.POST.get('mobile')
        other_contact = request.POST.get('other_contact')
        booking_date = request.POST.get('booking_date')
        submit_date = datetime.today().date()
        flag = False

        obj_3 = models.PatentRegistration.objects.get(id=id)
        obj_3.name = name
        obj_3.age = age
        obj_3.remark = remark
        obj_3.place = place
        obj_3.mobile = mobile
        obj_3.other_contact = other_contact
        obj_3.booking_date = booking_date
        obj_3.flag = flag

        if mobile == '' or name == '' or booking_date == '':
            return redirect('error')
        else:
            obj_3.save()
            return redirect('patent_table')
    context = {
        'data':data,
        'today_date':datetime.today().date()
    }
    html = 'administration/forms/patent_edit_form.html'
    return render(request,html,context)


def PatentDeleteView(request,id):
    data = models.PatentRegistration.objects.get(id=id)
    data.delete()
    return redirect('patent_table')
    context = {}
    html = 'administration/forms/patent_edit_form.html'
    return render(request,html,context)


# =================================== Website Mobile Request ===============


def QuickAppointmentTableView(request):
    data = models.QuickAppointment.objects.all().order_by('-id')
    context = {
        'data':data,
        'today_date':datetime.today().date()
    }
    html = 'administration/tables/quick_appointment_table.html'
    return render(request,html,context)


def QuickAppointmentEditView(request,id):
    data = models.QuickAppointment.objects.get(id=id)
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        remark = request.POST.get('remark')
        place = request.POST.get('place')
        mobile = request.POST.get('mobile')
        other_contact = request.POST.get('other_contact')
        booking_date = request.POST.get('booking_date')
        submit_date = datetime.today().date()
        flag = False

        obj = models.QuickAppointment.objects.get(id=id)
        obj.name = name
        obj.age = age
        obj.remark = remark
        obj.place = place
        obj.mobile = mobile
        obj.other_contact = other_contact
        obj.booking_date = booking_date
        obj.flag = flag

        if mobile == '' or name == '' or booking_date == '':
            return redirect('error')
        else:
            obj.save()
            return redirect('quick_appointment_table')
    context = {
        'data':data,
        'today_date':datetime.today().date()
    }
    html = 'administration/forms/quick_appointment_edit_form.html'
    return render(request,html,context)


def QuickAppointmentDeleteView(request,id):
    data = models.QuickAppointment.objects.get(id=id)
    data.delete()
    return redirect('quick_appointment_table')
    context = {}
    html = 'administration/forms/quick_appointment_edit_form.html'
    return render(request,html,context)
    

# ===================== Website Form Request (Appointment) ====================


def AppointmentTableView(request):
    data = models.Appointment.objects.all().order_by('-id')
    context = {
        'data':data,
        'today_date':datetime.today().date()
    }
    html = 'administration/tables/appointment_table.html'
    return render(request,html,context)


def AppointmentEditView(request,id):
    data = models.Appointment.objects.get(id=id)
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        remark = request.POST.get('remark')
        place = request.POST.get('place')
        mobile = request.POST.get('mobile')
        other_contact = request.POST.get('other_contact')
        booking_date = request.POST.get('booking_date')
        submit_date = datetime.today().date()
        flag = False

        obj = models.Appointment.objects.get(id=id)
        obj.name = name
        obj.age = age
        obj.remark = remark
        obj.place = place
        obj.mobile = mobile
        obj.other_contact = other_contact
        obj.booking_date = booking_date
        obj.flag = flag

        if mobile == '' or name == '' or booking_date == '':
            return redirect('error')
        else:
            obj.save()
            return redirect('appointment_table')
    context = {
        'data':data,
        'today_date':datetime.today().date()
    }
    html = 'administration/forms/appointment_edit_form.html'
    return render(request,html,context)


def AppointmentDeleteView(request,id):
    data = models.Appointment.objects.get(id=id)
    data.delete()
    return redirect('appointment_table')
    context = {}
    html = 'administration/forms/appointment_edit_form.html'
    return render(request,html,context)


def ShopRequestTableView(request):
    data = models.ShopRequest.objects.all().order_by('-id')
    context = { 'data' : data, 'today_date':datetime.today().date() }
    html = 'administration/tables/shop_request_table.html'
    return render(request,html,context)


def DeleteShopRequestView(request,id):
    data = models.ShopRequest.objects.get(id=id)
    data.delete()
    return redirect('shop_request')
    context = {}
    html = 'administration/tables/shop_request_table.html'
    return render(request,html,context)


def MessageTableView(request):
    data = models.Messages.objects.all().order_by('-id')
    context = { 'data' : data, 'today_date':datetime.today().date() }
    html = 'administration/tables/message_table.html'
    return render(request,html,context)


def DeleteMessageView(request,id):
    data = models.Messages.objects.get(id=id)
    data.delete()
    return redirect('message_table')
    context = {}
    html = 'administration/tables/message_table.html'
    return render(request,html,context)


def SubscribersTableView(request):
    data = models.Subscribe.objects.all().order_by('-id')
    context = { 'data' : data, 'today_date':datetime.today().date() }
    html = 'administration/tables/subscribers_table.html'
    return render(request,html,context)


def DeleteSubscribersView(request,id):
    data = models.Subscribe.objects.get(id=id)
    data.delete()
    return redirect('subscribers_table')
    context = {}
    html = 'administration/tables/subscribers_table.html'
    return render(request,html,context)

# ========================================================


def TodayTableView(request):
    today_date = datetime.today().date()
    data1 = models.PatentRegistration.objects.filter(booking_date=today_date,flag=False)
    data2 = models.QuickAppointment.objects.filter(booking_date=today_date,flag=False)
    data3 = models.Appointment.objects.filter(booking_date=today_date,flag=False)
    context = {
        'data1':data1, 
        'data2':data2,
        'data3':data3,
        'today_date':datetime.today().date() 
    }
    html = 'administration/tables/today.html'
    return render(request,html,context)


def TomorrowTableView(request):
    today_date = datetime.today().date()
    tomorrow_date = today_date + timedelta(1)
    data1 = models.PatentRegistration.objects.filter(booking_date=tomorrow_date,flag=False)
    data2 = models.QuickAppointment.objects.filter(booking_date=tomorrow_date,flag=False)
    data3 = models.Appointment.objects.filter(booking_date=tomorrow_date,flag=False)
    context = {
        'data1':data1, 
        'data2':data2,
        'data3':data3,
        'today_date':datetime.today().date() 
    }
    html = 'administration/tables/tomorrow.html'
    return render(request,html,context)

# ====================== LOGIN / LOGOUT ===================

def AdministrationLoginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        aut = authenticate(username = username, password = password)
        if aut is None:       
            return redirect('administration_login')
        else:
            login(request,aut)
            if aut.is_staff:
                return redirect('administration_home')
            else:
                return redirect('administration_login')
    
    context = {'today_date':datetime.today().date()}
    html = 'administration/forms/administration_login_form.html'
    return render(request,html,context)

# ====================== Nurse Registration ===============


class NurseRegisterView(generic.CreateView):
   form_class = SignUpForm
   template_name = 'administration/forms/nurse_register_form.html'
   success_url = reverse_lazy('nurse_register')
   
   def get_context_data(self, *args, **kwargs):
       data = User.objects.all()
       context = super(NurseRegisterView, self).get_context_data(*args, **kwargs)
       context["data"] = data
       context["today_date"] = datetime.today().date()
       return context


def DeleteNurseView(request,id):
    data = User.objects.get(id=id)
    data.delete()
    return redirect('nurse_register')
    context = {}
    html = 'administration/forms/nurse_register_form.html'
    return render(request,html,context)
       

# =============================


class AddGalleryImage(CreateView):
    model = models.Gallery
    form_class = GalleryForm
    template_name = 'administration/forms/add_gallery_image.html'
    success_url = reverse_lazy('add_gallery_image')

    def get_context_data(self, *args, **kwargs):
        data = models.Gallery.objects.all().order_by('-id')
        context = super(AddGalleryImage, self).get_context_data(*args, **kwargs)
        context["data"] = data
        context["today_date"] = datetime.today().date()
        return context

      
def DeleteGalleryImage(request,id):
    data = models.Gallery.objects.get(id=id)
    data.delete()
    return redirect('add_gallery_image')
    context = {}
    html = 'administration/forms/add_gallery_image.html'
    return render(request,html,context)


class AddFeedbackView(CreateView):
    model = models.Feedback
    form_class = FeedbackForm
    template_name = 'administration/forms/add_feedback.html'
    success_url = reverse_lazy('add_feedback')

    def get_context_data(self, *args, **kwargs):
        data = models.Feedback.objects.all().order_by('-id')
        context = super(AddFeedbackView, self).get_context_data(*args, **kwargs)
        context["data"] = data
        context["today_date"] = datetime.today().date()
        return context


def DeleteFeedbackView(request,id):
    data = models.Feedback.objects.get(id=id)
    data.delete()
    return redirect('add_feedback')
    context = {}
    html = 'administration/forms/add_feedback.html'
    return render(request,html,context)



class AddDoctorsProfileView(CreateView):
    model = models.DoctorsProfile
    form_class = DoctorsForm
    template_name = 'administration/forms/add_doctors_profile.html'
    success_url = reverse_lazy('add_doctors_profile')

    def get_context_data(self, *args, **kwargs):
        data = models.DoctorsProfile.objects.all().order_by('-id')
        context = super(AddDoctorsProfileView, self).get_context_data(*args, **kwargs)
        context["data"] = data
        context["today_date"] = datetime.today().date()
        return context


def DeleteDoctorsProfileView(request,id):
    obj = models.DoctorsProfile.objects.get(id=id)
    obj.delete()
    return redirect('add_doctors_profile')
    context = {}
    html = 'administration/forms/add_doctors_profile.html'
    return render(request,html,context)


class AddShopItemView(CreateView):
    model = models.Shop
    form_class = ShopForm
    template_name = 'administration/forms/add_shop_item.html'
    success_url = reverse_lazy('add_shop_item')

    def get_context_data(self, *args, **kwargs):
        data = models.Shop.objects.all().order_by('-id')
        context = super(AddShopItemView, self).get_context_data(*args, **kwargs)
        context["data"] = data
        context["today_date"] = datetime.today().date()
        return context
  
    
def DeleteShopItemView(request,id):
    obj = models.Shop.objects.get(id=id)
    obj.delete()
    return redirect('add_shop_item')
    context = {}
    html = 'administration/forms/add_shop_item.html'
    return render(request,html,context)

# ===================================

def SearchPatientTableView(request):
    data = models.PatentRegistration.objects.all()
    if request.method == 'POST':
      searched_patient = request.POST['searched_patient']
      search_name = models.PatentRegistration.objects.filter(name__icontains=searched_patient)
      search_mobile = models.PatentRegistration.objects.filter(mobile__icontains=searched_patient)
      search_mobile2 = models.PatentRegistration.objects.filter(other_contact__icontains=searched_patient)
      
      return render(request, 'administration/tables/search_patient_table.html', {
         'searched_patient':searched_patient, 
         'search_name':search_name, 
         'search_mobile':search_mobile,
         'search_mobile2':search_mobile2,
         'data':data,
         'today_date':datetime.today().date()
         })
    else:    
      return render(request, 'administration/tables/search_patient_table.html', {}) 


def SearchAppointmentTableView(request):
    data = models.Appointment.objects.all()
    if request.method == 'POST':
      searched_appointment = request.POST['searched_appointment']
      search_name = models.Appointment.objects.filter(name__icontains=searched_appointment)
      search_mobile = models.Appointment.objects.filter(mobile__icontains=searched_appointment)
      search_mobile2 = models.Appointment.objects.filter(other_contact__icontains=searched_appointment)
      
      return render(request, 'administration/tables/search_appointment_table.html', {
         'searched_patient':searched_appointment, 
         'search_name':search_name, 
         'search_mobile':search_mobile,
         'search_mobile2':search_mobile2,
         'data':data,
         'today_date':datetime.today().date()
         })
    else:    
      return render(request, 'administration/tables/search_appointment_table.html', {}) 



def SearchQuickAppointmentTableView(request):
    data = models.QuickAppointment.objects.all()
    if request.method == 'POST':
      searched_quick_appointment = request.POST['searched_quick_appointment']
      search_name = models.QuickAppointment.objects.filter(name__icontains=searched_quick_appointment)
      search_mobile = models.QuickAppointment.objects.filter(mobile__icontains=searched_quick_appointment)
      search_mobile2 = models.QuickAppointment.objects.filter(other_contact__icontains=searched_quick_appointment)
      
      return render(request, 'administration/tables/search_quick_appointment_table.html', {
         'searched_patient':searched_quick_appointment, 
         'search_name':search_name, 
         'search_mobile':search_mobile,
         'search_mobile2':search_mobile2,
         'data':data,
         'today_date':datetime.today().date()
         })
    else:    
      return render(request, 'administration/tables/search_quick_appointment_table.html', {}) 



# ======================================


def AddCountView(request):
    data = models.CounterValues.objects.all()
    if request.method == 'POST':
        docter_count = request.POST.get('docter_count')
        department_count = request.POST.get('department_count')
        reserchlab_count = request.POST.get('reserchlab_count')
        awards_count = request.POST.get('awards_count')
        submit_date = datetime.today().date()

        obj = models.CounterValues()
        obj.docter_count = docter_count
        obj.department_count = department_count
        obj.reserchlab_count = reserchlab_count
        obj.awards_count = awards_count
        obj.submit_date = submit_date

        if docter_count == '' or department_count == '' or reserchlab_count == '' or awards_count == '' :
            return redirect('error')
        else:
            obj.save()
            return redirect('add_count')
    context = { 'data' : data, 'today_date':datetime.today().date() }
    print(data)
    html = 'administration/forms/add_count.html'
    return render(request,html,context)


def DeleteCountView(request,id):
    obj = models.CounterValues.objects.get(id=id)
    obj.delete()
    return redirect('add_count')
    context = {}
    html = 'administration/forms/add_count.html'
    return render(request,html,context)



def AddGoogleMeetView(request):
    data = models.GoogleMeet.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        link = request.POST.get('link')
        submit_date = datetime.today().date()

        obj = models.GoogleMeet()
        obj.name = name
        obj.link = link
        obj.submit_date = submit_date

        if name == '' or link == '':
            return redirect('error')
        else:
            obj.save()
            return redirect('add_google_meet')
    context = { 'data' : data, 'today_date':datetime.today().date() }
    print(data)
    html = 'administration/forms/add_google_meet.html'
    return render(request,html,context)


def DeleteGoogleMeetView(request,id):
    obj = models.GoogleMeet.objects.get(id=id)
    obj.delete()
    return redirect('add_google_meet')
    context = {}
    html = 'administration/forms/add_google_meet.html'
    return render(request,html,context)




def AddTodoView(request):
    data = models.Todo.objects.all().order_by('-id')
    if request.method == 'POST':
        todo_name = request.POST.get('todo_name')
        todo_dead_time = request.POST.get('todo_dead_time')
        todo_subject = request.POST.get('todo_subject')
        todo_body = request.POST.get('todo_body')
        todo_status = request.POST.get('todo_status')
        submit_date = datetime.today().date()

        obj = models.Todo()
        obj.todo_name = todo_name
        obj.todo_dead_time = todo_dead_time
        obj.todo_subject = todo_subject
        obj.todo_body = todo_body
        obj.todo_status = todo_status
        obj.submit_date = submit_date

        if todo_name == '' or todo_subject == '':
            return redirect('error')
        else:
            obj.save()
            return redirect('add_todo')
    context = { 'data' : data, 'today_date':datetime.today().date() }
    html = 'administration/forms/add_todo_form.html'
    return render(request,html,context)


def EditTodoView(request,id):
    data = models.Todo.objects.get(id=id)
    if request.method == 'POST':
        todo_name = request.POST.get('todo_name')
        todo_dead_time = request.POST.get('todo_dead_time')
        todo_subject = request.POST.get('todo_subject')
        todo_body = request.POST.get('todo_body')
        todo_status = request.POST.get('todo_status')
        submit_date = datetime.today().date()

        obj = models.Todo(id=id)
        obj.todo_name = todo_name
        obj.todo_dead_time = todo_dead_time
        obj.todo_subject = todo_subject
        obj.todo_body = todo_body
        obj.todo_status = todo_status
        obj.submit_date = submit_date

        if todo_name == '' or todo_subject == '':
            return redirect('error')
        else:
            obj.save()
            return redirect('add_todo')
    context = { 'data' : data, 'today_date':datetime.today().date() }
    html = 'administration/forms/edit_todo_form.html'
    return render(request,html,context)



def EditTodoStatusView(request,id):
    data = models.Todo.objects.get(id=id)
    if request.method == 'POST':
        todo_status = request.POST.get('todo_status')

        obj = models.Todo(id=id)
        obj.todo_name = data.todo_name
        obj.todo_dead_time = data.todo_dead_time
        obj.todo_subject = data.todo_subject
        obj.todo_body = data.todo_body
        obj.todo_status = todo_status
        obj.submit_date = data.submit_date

        if todo_status == '' :
            return redirect('error')
        else:
            obj.save()
            return redirect('add_todo')
    context = { 'data' : data, 'today_date':datetime.today().date() }
    html = 'administration/forms/edit_todo_status.html'
    return render(request,html,context)


def DeleteTodoView(request,id):
    obj = models.Todo.objects.get(id=id)
    obj.delete()
    return redirect('add_todo')
    context = {}
    html = 'administration/forms/add_todo_form.html'
    return render(request,html,context)



def AddNotesView(request):
    data = models.Notes.objects.all().order_by('-id')
    if request.method == 'POST':
        note_body = request.POST.get('note_body')
        submit_date = datetime.today().date()

        obj = models.Notes()
        obj.note_body = note_body
        obj.submit_date = submit_date

        if note_body == '':
            return redirect('add_notes')
        else:
            obj.save()
            return redirect('add_notes')
    context = { 'data' : data, 'today_date':datetime.today().date() }
    html = 'administration/forms/add_notes.html'
    return render(request,html,context)


def DeleteNotesView(request,id):
    obj = models.Notes.objects.get(id=id)
    obj.delete()
    return redirect('add_notes')
    context = {}
    html = 'administration/forms/add_notes.html'
    return render(request,html,context)
