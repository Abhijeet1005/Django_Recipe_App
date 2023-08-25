from django.shortcuts import render , redirect
from .models import Recipes

# Create your views here.

def recipes(request):  # sourcery skip: extract-method

    if request.method == "POST":

        data = request.POST
        recipe_image = request.FILES.get('recipe_image')
        recipe_name = data.get('recipe_name')
        recipe_desc = data.get('recipe_desc')

        print(recipe_name,"   ",recipe_desc, recipe_image)
        Recipes.objects.create(recipe_name = recipe_name,recipe_desc = recipe_desc,recipe_image = recipe_image)
        
        return redirect('/recipes/')
    
    queryset = Recipes.objects.values()
    all_recipes = {'recipes': queryset}


        
        
    return render(request, 'recipes.html',all_recipes)
