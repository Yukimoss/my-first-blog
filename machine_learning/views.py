from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm
from django.http import HttpResponse
import pandas as pd
import pickle
import sys
import io

loaded_model = pickle.load(open('finalized_model.sav', 'rb'))

# ------------------------------------------------------------------
def file_upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():

            sys.stderr.write("*** machine_leraning *** aaa ***\n")
            handle_uploaded_file(request.FILES['file'])
            file_obj = request.FILES['file']
            sys.stderr.write(file_obj.name + "\n")
            # df = pd.read_csv(io.BytesIO(file_obj))
            df = pd.read_csv(file_obj.name)
            result = loaded_model.predict(df)
            print(result)
            str_out = result
            return HttpResponse(str_out)
    else:
        form = UploadFileForm()
    return render(request, 'machine_learning/upload.html', {'form': form})
#
#
# ------------------------------------------------------------------
def handle_uploaded_file(file_obj):
    sys.stderr.write("*** handle_uploaded_file *** aaa ***\n")
    sys.stderr.write(file_obj.name + "\n")
    # file_path = 'imada.pythonanywhere.com/media/documents/' + file_obj.name 
    file_path = file_obj.name 
    sys.stderr.write(file_path + "\n")
    with open(file_path, 'wb+') as destination:
        for chunk in file_obj.chunks():
            sys.stderr.write("*** handle_uploaded_file *** ccc ***\n")
            destination.write(chunk)
            sys.stderr.write("*** handle_uploaded_file *** eee ***\n")
#
# ------------------------------------------------------------------
# def success(result):
#     str_out = "予測結果は<p />"
#     str_out += result + "です<p />"
#     return HttpResponse(str_out)
# ------------------------------------------------------------------

# Create your views here.
