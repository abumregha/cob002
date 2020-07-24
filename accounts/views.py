from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import NewAccountDataForm, SignupForm,LoginForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user,allowd_users
from django.contrib.auth.models import Group
from django.core.exceptions import ObjectDoesNotExist
from .mrz_passport import read_passport_mrz, test_call
from .utils import render_to_pdf
from django.template.loader import get_template



@login_required(login_url='login')
@allowd_users(allowed_roles=['admin'])
def home(request):
    applications = NewAccountData.objects.filter(status='Submitted')
    return render(request, 'accounts/dashboard.html', {'list': applications})

@login_required(login_url='login')
@allowd_users(allowed_roles=['admin'])
def save_to_pdf(request,pk):
    customer_application = get_object_or_404(NewAccountData, id=pk)
    context = {
        'customer_application': customer_application
    }
    template = get_template('accounts/save_to_pdf.html')
    html = template.render(context)
    pdf = render_to_pdf('accounts/save_to_pdf.html', context)
    return HttpResponse(pdf, content_type='application/pdf')



@login_required(login_url='login')
@allowd_users(allowed_roles=['admin'])
def view_application(request,pk):
    customer_application = get_object_or_404(NewAccountData, id=pk)
    context = {
        'customer_application': customer_application
    }
    print('html is rendered')
    return render(request, 'accounts/view_application.html', context)


@unauthenticated_user
def loginPage(request):
        if request.method == 'POST':
            form = LoginForm(request.POST)
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.is_active:
                    #print('hello', user.id)
                    login(request, user)
                    return redirect('user-page')

                else:
                    return HttpResponse('Disabled account')
            else:
                messages.info(request, 'incorrect username or password !!')
        else:
            form = LoginForm()
        return render(request, 'accounts/login.html', {'form': form})
@unauthenticated_user
def registerPage(request):
        form = SignupForm()
        if request.method == 'POST':
            form = SignupForm(request.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username')
                group = Group.objects.get(name='customer')
                user.groups.add(group)
                # NewAccountData.objects.create(
                #     user=user,
                #     status='no Started',
                # )
                messages.success(request,'account created for  '+ username)
                return redirect('login')
        context = {'form':form}
        return render(request, 'accounts/register.html', context)
def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
@allowd_users(allowed_roles=['admin'])
@login_required(login_url='login')
@allowd_users(allowed_roles=['customer'])
def apply_for_account(request):
    form = NewAccountDataForm()
    if request.method == 'POST':
        if '_submit' in request.POST:
            print('data to be submitted')
            form = NewAccountDataForm(request.POST, request.FILES)
            form.fields['First_Name_Arabic'].required=True
            form.fields['Middle_Name_Arabic'].required = True
            form.fields['Last_Name_Arabic'].required = True
            form.fields['First_Name_English'].required = True
            form.fields['Middle_Name_English'].required = True
            form.fields['Last_Name_English'].required = True
            form.fields['Birth_dt'].required = True
            form.fields['PlaceOFBirth'].required = True
            form.fields['Gender'].required = True
            form.fields['MartialStatus'].required = True
            form.fields['Home_Address'].required = True
            form.fields['City'].required = True
            form.fields['Country'].required = True
            form.fields['Nationality'].required = True
            form.fields['CountryOfBirth'].required = True
            form.fields['Email'].required = True
            form.fields['EmployerName'].required = True
            form.fields['Position'].required = True
            form.fields['EmployerSector'].required = True
            form.fields['Salary'].required = True
            form.fields['Nationality'].required = True
            form.fields['PhoneNumber1'].required = True
            form.fields['PassportNo'].required = True
            form.fields['PassportIssueDate'].required = True
            form.fields['PassportExpiryDate'].required = True
            form.fields['PassportIssueAuthority'].required = True
            form.fields['Nid'].required = True
            form.fields['Birth_certificate'].required = True
            form.fields['Passport_copy'].required = True
            form.fields['Employer_statement'].required = True
            form.fields['Personal_pic'].required = True
            if form.is_valid():
                newaccountdata = form.save(commit=False)
                newaccountdata.status = 'Submitted'
                newaccountdata.user = request.user
                newaccountdata.save()
                return redirect('user-page')
        elif '_save' in request.POST:
            print('data is saved for later')
            form = NewAccountDataForm(request.POST, request.FILES)
            if form.is_valid():
                newaccountdata = form.save(commit=False)
                newaccountdata.status = 'Unfinished'
                newaccountdata.user = request.user
                newaccountdata.save()
            messages.warning(request, "data successfully saved, you can still revise your application")
            return render(
                    request,
                    'accounts/user.html',
                    {'form': form}
                )
    context = {'form': form}
    return render(request, 'accounts/apply_for_account.html', context)
@login_required(login_url='login')
@allowd_users(allowed_roles=['customer'])
def userPage(request):
    # print(request.user.customer.newaccountdata.status)
    try:
        application_status = request.user.newaccountdata.status
        print(application_status)
    except ObjectDoesNotExist:
        application_status = 'not Started'
        print(application_status)
    return render(request, 'accounts/user.html', {'application_status': application_status})
@login_required(login_url='login')
@allowd_users(allowed_roles=['customer'])
def customerApplication(request):
        ApplicationData = request.user.newaccountdata
        form = NewAccountDataForm(instance=ApplicationData)
        if request.method == 'POST':
            if '_submit' in request.POST:
                print('data to be submitted')
                form = NewAccountDataForm(request.POST, request.FILES,instance=ApplicationData)
                form.fields['First_Name_Arabic'].required = True
                form.fields['Middle_Name_Arabic'].required = True
                form.fields['Last_Name_Arabic'].required = True
                form.fields['First_Name_English'].required = True
                form.fields['Middle_Name_English'].required = True
                form.fields['Last_Name_English'].required = True
                form.fields['Birth_dt'].required = True
                form.fields['PlaceOFBirth'].required = True
                form.fields['Gender'].required = True
                form.fields['MartialStatus'].required = True
                form.fields['Home_Address'].required = True
                form.fields['City'].required = True
                form.fields['Country'].required = True
                form.fields['Nationality'].required = True
                form.fields['CountryOfBirth'].required = True
                form.fields['Email'].required = True
                form.fields['EmployerName'].required = True
                form.fields['Position'].required = True
                form.fields['EmployerSector'].required = True
                form.fields['Salary'].required = True
                form.fields['Nationality'].required = True
                form.fields['PhoneNumber1'].required = True
                form.fields['PassportNo'].required = True
                form.fields['PassportIssueDate'].required = True
                form.fields['PassportExpiryDate'].required = True
                form.fields['PassportIssueAuthority'].required = True
                form.fields['Nid'].required = True
                form.fields['Birth_certificate'].required = True
                form.fields['Passport_copy'].required = True
                form.fields['Employer_statement'].required = True
                form.fields['Personal_pic'].required = True
                if form.is_valid():
                    newaccountdata = form.save(commit=False)
                    newaccountdata.status = 'Submitted'
                    newaccountdata.user = request.user
                    newaccountdata.save()
                    return redirect('user-page')
            elif '_save' in request.POST:
                print('data is saved for later')
                form = NewAccountDataForm(request.POST, request.FILES,instance=ApplicationData)
                if form.is_valid():
                    newaccountdata = form.save(commit=False)
                    newaccountdata.status = 'Unfinished'
                    newaccountdata.user = request.user
                    newaccountdata.save()
                    read_passport_mrz(newaccountdata.Passport_copy.path)
                messages.warning(request, "data successfully saved, you can still revise your application")
                return render(
                    request,
                    'accounts/customer_application.html',
                    {'form': form}
                )
        context = {'form':form}
        return render(request, 'accounts/customer_application.html', context)