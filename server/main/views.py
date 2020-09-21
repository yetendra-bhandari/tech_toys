from django.http import FileResponse, Http404


def showImage(request, directory, filename):
    try:
        return FileResponse(open(f'storage/{directory}/{filename}', 'rb'))
    except(IOError):
        raise Http404("Requested image does not exist!")
