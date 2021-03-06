from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render

# Create your views here.
from cnn_model import compute_result
from main.models import RoadExtraction


def home(request):
    return render(request, 'main/home.html')


def result(request):
    if request.method == 'POST':

        upload_directory = str(settings.MEDIA_ROOT) + "/" + str(request.user.id) + "/uploads/"
        print(upload_directory)
        result_directory = str(settings.MEDIA_ROOT) + "/" + str(request.user.id) + "/results/"
        uploaded_file_url = None
        processed_file_url = None

        if request.FILES.get('image'):
            uploaded_image = request.FILES.get('image')
            fs = FileSystemStorage(location=upload_directory)  # defaults to MEDIA_ROOT
            file_name = fs.save(uploaded_image.name, uploaded_image)
            uploaded_file_url = '/images/' + str(request.user.id) + "/uploads/" + file_name
            compute_result.process_image(upload_directory, result_directory, file_name)
            processed_file_url = '/images/' + str(request.user.id) + "/results/" + file_name

        if request.user.is_authenticated:
            RoadExtraction.objects.create(
                user=request.user,
                uploaded_image_url=uploaded_file_url,
                processed_image_url=processed_file_url,
            )

        context = {
            'uploaded_image_url': uploaded_file_url,
            'processed_image_url': processed_file_url
        }

        return render(request, 'main/result.html', context)


def history(request):
    if request.method == 'GET':
        predictions = RoadExtraction.objects.filter(user=request.user).order_by('-date_created')
        context = {
            'predictions': predictions
        }
        return render(request, 'main/history.html', context)
