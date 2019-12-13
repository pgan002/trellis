from django.http import JsonResponse

from app.en import int_to_words


def index(request):
    n = request.GET.get('number')
    if n is None:
        return JsonResponse(
            {
                'status': 'error',
                'message': 'missing parameter "number"'
            },
            status=401)
    try:
        words = int_to_words(n)
    except ValueError as e:
        return JsonResponse({'status': 'error', 'message': e},
                            status=401)

    return JsonResponse({'status': 'ok', 'num_in_english': words})
