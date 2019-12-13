from django.http import JsonResponse

from app import en


def index(request):
    n = request.GET.get('number')
    if n is None:
        return JsonResponse(
            {
                'status': 'error',
                'message': 'missing parameter "number"'
            },
            status=401)
    return JsonResponse({'status': 'ok', 'num_in_english': en.int_to_words(n)})
