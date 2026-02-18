from django.shortcuts import render, redirect
from .forms import SuggestionForm

def suggestion_view(request):
    if request.method == 'POST':
        form = SuggestionForm(request.POST)
        if form.is_valid():
            # Extract cleaned data
            title = form.cleaned_data['title']
            year = form.cleaned_data['release_year']
            
            # Print confirmation to terminal
            print(f"Suggestion received for '{title}' ({year})")
            
            # Redirect to the 'thanks' page
            return redirect('thanks_page')
    else:
        # GET request: provide a blank form
        form = SuggestionForm()

    return render(request, 'catalog/suggestion_form.html', {'form': form})

def thanks_view(request):
    return render(request, 'catalog/thanks.html')