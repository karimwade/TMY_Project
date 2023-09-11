import traceback
from django.shortcuts import render, redirect
from .models import TMYParameter
from django.contrib import messages
import yaml
import os
from django.conf import settings
from django.http import FileResponse, HttpResponse 

def index(request):
    #load data on the template
    #data=Student.objects.all()
    #context={"data":data}
    return render(request,"index.html")


def create_tmy_parameter(request):
    if request.method == 'POST':
        project_name = request.POST["project_name"]
        latitude = request.POST["latitude"]
        longitude = request.POST["longitude"]
        altitude = request.POST['altitude']
        technology = request.POST["technology"]
        pv_description = request.POST["pv_description"]
        pv_tilt = request.POST["pv_tilt"]
        pv_azimuth = request.POST["pv_azimuth"]
        tracker_description = request.POST["tracker_description"]
        tracker_gcr = request.POST["tracker_gcr"]
        tracker_axis_azimuth = request.POST["tracker_axis_azimuth"]
        tracker_max_angle = request.POST["tracker_max_angle"]
        request_id = request.POST["request_id"]
        p50 = request.POST["p50"]
        p75 = request.POST["p75"]
        p90 = request.POST["p90"]
        p10 = request.POST["p10"]
        p99 = request.POST["p99"]
        ambient_temperature = request.POST["ambient_temperature"]
        pm_2_5 = request.POST["pm_2_5"]
        pm_10 = request.POST["pm_10"]
        relative_humidity = request.POST["relative_humidity"]
        precipitable_water = request.POST["precipitable_water"]
        wind_direction = request.POST["wind_direction"]
        granularity = request.POST["granularity"]
        granularity_time = request.POST["granularity_time"]

        query = TMYParameter(project_name=project_name,
                             latitude=latitude,
                             longitude=longitude,
                             altitude=altitude,
                             technology=technology,
                             pv_description=pv_description,
                             pv_tilt = pv_tilt,
                             pv_azimuth=pv_azimuth,
                             tracker_description=tracker_description,
                             tracker_gcr=tracker_gcr,
                             tracker_axis_azimuth=tracker_axis_azimuth,
                             tracker_max_angle=tracker_max_angle,
                             request_id=request_id,
                             p50=p50,
                             p75=p75,
                             p90=p90,
                             p10=p10,
                             p99=p99,
                             ambient_temperature=ambient_temperature,
                             pm_2_5=pm_2_5,
                             pm_10=pm_10,
                             relative_humidity=relative_humidity,
                             precipitable_water=precipitable_water,
                             wind_direction=wind_direction,
                             granularity=granularity)
    # Sauvegardez les données du formulaire dans la base de données
        query.save()
        messages.info(request,"Data save sucessfully") 
        
    # Générez le contenu YAML
        tmy_data = {
            'project_name': project_name,
            'location': {
                'latitude': latitude,
                'longitude': longitude,
                'altitude': altitude,
            },
            'pv_system': {
                'technology': technology,
                'pv': {
                    'description': pv_description,
                    'tilt': pv_tilt,
                    'azimuth': pv_azimuth,
                },
                'tracker': {
                    'description': tracker_description,
                    'gcr': tracker_gcr,
                    'axis_azimuth': tracker_axis_azimuth,
                    'max_angle': tracker_max_angle,
                },
            },
            'analysis': {
                'request_id': request_id,
                'probability': {
                    'p50': p50,
                    'p75': p75,
                    'p90': p90,
                    'p10': p10,
                    'p99': p99,
                },
            },
            'meteo_data': {
                'ambient_temperature': ambient_temperature,
                'pm_2_5': pm_2_5,
                'pm_10': pm_10,
                'relative_humidity': relative_humidity,
                'precipitable_water': precipitable_water,
                'wind_direction': wind_direction,
            },
            'granularity': granularity+" "+granularity_time,
        }

        # Convertissez les données YAML en chaîne
        yaml_content = yaml.dump(tmy_data, default_flow_style=False)

        # Créez un fichier YAML
        with open('tmy_data.yaml', 'w') as yaml_file:
            yaml_file.write(yaml_content)
        #return redirect("success")

    return render(request,'index.html')

    

def success(request):
    # Chemin absolu vers le fichier YAML à la racine du projet
    file_path = os.path.join(os.path.dirname(__file__), '..', 'tmy_data.yaml')

    # Vérifiez si le fichier existe
    if os.path.exists(file_path):
        # Ouvrez le fichier en mode binaire
        with open(file_path, 'rb') as yaml_file:
            response = FileResponse(yaml_file)
            response['Content-Disposition'] = 'attachment; filename="tmy_data.yaml"'
            #return redirect(request,"success.html")
            return HttpResponse(response)
        
    else:
        # Gérez le cas où le fichier n'existe pas
        return HttpResponse("Le fichier n'existe pas", status=404)

    return redirect(request,"success.html")