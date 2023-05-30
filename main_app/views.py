from django.shortcuts import render

finches = [
  {'name': 'Steve', 'species': 'Evening Grosbeak', 'description': 'Yellow', 'age': 2},
  {'name': 'Carl', 'species': 'Purple Finch', 'description': 'Well, purple', 'age': 3},
  {'name': 'Queen', 'species': 'Black Rosy-Finch', 'description': 'Kinda grey', 'age': 4},
]

# Define the home view
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def index(request):
  return render(request, 'finches/index.html', {
    'finches': finches
  })
