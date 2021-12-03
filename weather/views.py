from django.shortcuts import render

# Create your views here.

def home(request):
    import json
    import requests
    #El action del form y la llamada a la variable zipcode en el home.html / la variable zipcode sustituye el zipcode fijo de la api
    if request.method == "POST":
        zipcode = request.POST['zipcode']
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode + "&distance=25&API_KEY=8BB9E834-671F-4194-8D91-87B8639F3D20")
        
        try:
            api = json.loads(api_request.content)    
        except Exception as e:
            api = "Error..."

        if api[0]['Category']['Name'] == "Good":
            category_description = "(0 - 50) La Calidad del Aire es considerado satisfactorio y de poco riesgo."
            category_color = "good" #llama a la clase declarada en el base.html 
        elif api[0]['Category']['Name'] == "Moderate": 
            category_description = "(51 -100) La calidad del Aire es aceptable Existe algo de polucion"
            category_color = "moderate" #llama a la clase declarada en el base.html 
        elif api[0]['Category']['Name'] == "USG": 
            category_description = "(101 -150) El Publico general no se vera afectado, pero la polucion presente puede representar riesgos para niños y adultos mayores"
            category_color = "usg" #llama a la clase declarada en el base.html 
        elif api[0]['Category']['Name'] == "Unhealthy": 
            category_description = "(151 - 200) Todo el mundo comienza a experimentar problemas de salud"
            category_color = "unhealthy"#llama a la clase declarada en el base.html 
        elif api[0]['Category']['Name'] == "Very Unhealthy": 
            category_description = "(2001 - 300) Alerta de peligros a la salud"
            category_color = "veryunhealthy"#llama a la clase declarada en el base.html           
        elif api[0]['Category']['Name'] == "Hazardous": 
            category_description = "(3001 - 500) Advertencia de Salud en condiciones de emergencia"
            category_color = "hazardous" #llama a la clase declarada en el base.html        
            
        return render(request, 'home.html', {
        'api': api,
        'category_description':category_description,
        'category_color':category_color
        })

    else:      
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=25&API_KEY=8BB9E834-671F-4194-8D91-87B8639F3D20")
        
        try:
            api = json.loads(api_request.content)    
        except Exception as e:
            api = "Error..."

        if api[0]['Category']['Name'] == "Good":
            category_description = "(0 - 50) La Calidad del Aire es considerado satisfactorio y de poco riesgo."
            category_color = "good" #llama a la clase declarada en el base.html 
        elif api[0]['Category']['Name'] == "Moderate": 
            category_description = "(51 -100) La calidad del Aire es aceptable Existe algo de polucion"
            category_color = "moderate" #llama a la clase declarada en el base.html 
        elif api[0]['Category']['Name'] == "USG": 
            category_description = "(101 -150) El Publico general no se vera afectado, pero la polucion presente puede representar riesgos para niños y adultos mayores"
            category_color = "usg" #llama a la clase declarada en el base.html 
        elif api[0]['Category']['Name'] == "Unhealthy": 
            category_description = "(151 - 200) Todo el mundo comienza a experimentar problemas de salud"
            category_color = "unhealthy"#llama a la clase declarada en el base.html 
        elif api[0]['Category']['Name'] == "Very Unhealthy": 
            category_description = "(2001 - 300) Alerta de peligros a la salud"
            category_color = "veryunhealthy"#llama a la clase declarada en el base.html           
        elif api[0]['Category']['Name'] == "Hazardous": 
            category_description = "(3001 - 500) Advertencia de Salud en condiciones de emergencia"
            category_color = "hazardous" #llama a la clase declarada en el base.html        
            
        return render(request, 'home.html', {
        'api': api,
        'category_description':category_description,
        'category_color':category_color
        })

def about(request):
    return render(request, 'about.html', {})