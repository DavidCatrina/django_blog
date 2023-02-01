from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm


def register(request):
    if request.method == "POST":
        #creates a post with the form's data
        form = UserRegisterForm(request.POST) 

        # check if the data is valid
        if form.is_valid(): 

            # save the user to the database
            form.save() 
            username = form.cleaned_data.get('username') # get data in good format

            #show a success message
            messages.success(request, f'Account created for {username}!')

            #redirects to the blog page using the name value of the blog url patterns
            return redirect('blog-home')

    else:
        #creates an empty form
        form = UserRegisterForm() 

    
    context = {
        'form': form
    }
    return render(request, 'users/register.html', context)
