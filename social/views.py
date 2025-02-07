from django.shortcuts import render, redirect
from django.contrib.auth.models import User 
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from social.form import UserRegistrationForm, UserLoginForm, NoteForm
from django.http import JsonResponse
from social.models import Note
 
#Function for Home 
def home(request):
    if request.user.is_authenticated:                                    #first goto the login page, login and move to the home page
      form = NoteForm() 
      notes = Note.objects.filter(user=request.user).order_by('-id')     #order by is used to get the data from the table top     
      data= {
          'form':form,
          'notes':notes
      }
      if request.method=="POST":
        id = request.POST.get('id')
        title = request.POST.get('Title1')
        description = request.POST.get('Description1')
        if id:
            get_note = Note.objects.get(id=id)
            get_note.title = title
            get_note.description = description
            get_note.save()
            notes = Note.objects.values().filter(user=request.user).order_by('-id')
            user_notes=list(notes)
            return JsonResponse({"status":"Your Note Updated Successfully!","notes":user_notes})

        note = Note()
        note.title= title
        note.description= description
        note.user = request.user
        note.save()
        notes = Note.objects.values().filter(user=request.user).order_by('-id')
        user_notes=list(notes)
        return JsonResponse({"status":"Your Note Added Successfully!","notes":user_notes})

      return render(request, 'home.html',context = data)
    else:
        return redirect('Login')
    
#Function for user logout 
def userlogout(request):
    logout(request)
    return redirect('Login')

#Function for Edit Note
def edit_note(request):
    edit_id = request.POST.get('edit_id')
    title = request.POST.get('Title1')
    Description = request.POST.get('Description1')
    Note.objects.filter(id=edit_id).update(Title1 = title, Description1= Description )
    notes = Note.objects.values().filter(user=request.user).order_by('-id')
    user_notes=list(notes)
    return JsonResponse({"status":"Your Note Added Successfully!","notes":user_notes})

#Function for Delete Note
def delete_note(request):
    delete_id = request.GET.get('delete_id')
    print(delete_id)
    Note.objects.filter(id=delete_id).first().delete()
    notes = Note.objects.values().filter(user=request.user).order_by('-id')
    user_notes=list(notes)
    return JsonResponse({"status":"Your Note Deleted Successfully!","notes":user_notes})

#Function for User Login 
def userlogin(request):
    if request.method == 'POST':
        username = request.POST.get('UserName1')
        password = request.POST.get('Password1')

        # Authenticate the user
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({"status": "User Logged in Successfully"})
        else:
            return JsonResponse({"status": "Invalid Credentials!"})
    else:
        form = UserLoginForm()
        data = {
            'form': form,
        }
        return render(request, 'login.html')

#Function for Signup
def signup(request):
    if request.method == 'POST':
        Name1 = request.POST.get('Name1')
        Username1 = request.POST.get('Username1')
        Email1 = request.POST.get('Email1')
        Password1 = request.POST.get('Password1')
        Confirmpassword1 = request.POST.get('Confirmpassword1')
        # Check if passwords match
        if Password1 != Confirmpassword1:
            messages.error(request, "Passwords do not match")
            return render(request, 'signup.html', {'form': UserRegistrationForm()})
        # Create user if passwords match
        try:
            user = User.objects.create_user(
                username=Username1,
                email=Email1,
                password=Password1,
                first_name=Name1
            )
            user.save()
            messages.success(request, "User created successfully!")
            return redirect('home')    
        except Exception as e:
            messages.error(request, "An error occurred while creating the user.")
            return render(request, 'signup.html', {'form': UserRegistrationForm()})
    else:
        forms = UserRegistrationForm()
    return render(request, 'signup.html', {'form': forms})
