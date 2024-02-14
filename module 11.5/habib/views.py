from django.shortcuts import render

# Create your views here.
def index(request):
    
    meals = [
        {
            "strMeal": "BeaverTails",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/ryppsv1511815505.jpg",
            "idMeal": "52928",
            "text":"BeaverTails is a Canadian restaurant chain, specializing in pastries known as BeaverTails, that is operated by BeaverTails Canada Inc. Its namesake products are fried dough pastries, individually hand stretched to resemble beaver's tails, with various toppings added on the",

        },
        {
            "strMeal": "Breakfast Potatoes",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/1550441882.jpg",
            "idMeal": "52965",
             "text":"Easy to make deliciously seasoned Breakfast Potatoes! This tasty breakfast side is oven baked on a sheet pan, leaving you with potatoes that are perfectly crispy and golden brown outside and light and fluffy on the inside."
        },
        {
            "strMeal": "Canadian Butter Tarts",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/wpputp1511812960.jpg",
            "idMeal": "52923",
            "text":"Canadian dessert—and, oh, how I love them! These buttery mini pies, typically baked in a muffin tin, have a flaky crust filled with a gooey mixture of butter, sugar, syrup, egg, and sometimes raisins or nuts. They bear some resemblance to the American pecan pie and British treacle tart, but their uniquely rich flavor sets them apart. Though they can be enjoyed any time of year, butter tarts are"
        },
        {
            "strMeal": "Montreal Smoked Meat",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/uttupv1511815050.jpg",
            "idMeal": "52927",
            "text":"Montreal-style smoked meat, Montreal smoked meat or simply smoked meat in Quebec is a type of kosher-style deli meat product made by salting and curing beef brisket with spices. The brisket is allowed to absorb the flavours over a week. It is then hot smoked to cook through, and finally is steamed to completion. Wikipedia"
        },
        {
            "strMeal": "Nanaimo Bars",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/vwuprt1511813703.jpg",
            "idMeal": "52924",
            "text":"The Nanaimo bar is a bar dessert that requires no baking and is named after the Canadian city of Nanaimo in British Columbia. It consists of three layers: a wafer, nut, and coconut crumb base; custard icing in the middle; and a layer of chocolate ganache on top."
        },
        {
            "strMeal": "Pate Chinois",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/yyrrxr1511816289.jpg",
            "idMeal": "52930",
            "text":"Pâté chinois is a French Canadian dish similar to the English shepherd's pie or French hachis Parmentier. It is a traditional recipe in both Québécois cuisine and Acadian cuisine"
        },
        {
            "strMeal": "Pouding chomeur",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/yqqqwu1511816912.jpg",
            "idMeal": "52932",
            "text":"Though it translates to 'unemployed man's pudding,' pouding chomeur isn't cheap to make. The good news is you don't really need to eat this more than a few times a year anyway. It's the perfect dessert to pair with summer fruit or vanilla ice cream. If you use a bigger baking dish than I did, and pour over all the maple cream syrup, your cake should float over a pool of what will eventually be your sauce. If you just use a deep pie dish like I did, then just serve the extra sauce on the side."
        },
        {
            "strMeal": "Poutine",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/uuyrrx1487327597.jpg",
            "idMeal": "52804",
            "text":"Poutine is a dish of french fries and cheese curds topped with a brown gravy. It emerged in Quebec, in the late 1950s in the Centre-du-Québec region, though its exact origins are uncertain and there are several competing claims regarding its invention. For many years, it was used by some to mock Quebec society."
        },
        {
            "strMeal": "Rappie Pie",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/ruwpww1511817242.jpg",
            "idMeal": "52933",
            "text":"french fries and cheese curds topped with a brown gravy. It emerged in Quebec, in the late 1950s in the Centre-du-Québec region, though its exact origins are uncertain and there are several competing claims regarding its invention. For many years, it was used by some to mock Quebec society."
        },
        {
            "strMeal": "Split Pea Soup",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/xxtsvx1511814083.jpg",
            "idMeal": "52925",
            "text":"Pea soup or split pea soup is soup made typically from dried peas, such as the split pea. It is, with variations, a part of the cuisine of many cultures. It is most often greyish-green or yellow in color depending on the regional variety of peas used; all are cultivars of Pisum sativum."
        }
    ]
    return render(request, 'index.html', {'cards' : meals})
  