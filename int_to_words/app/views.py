from django.http import JsonResponse

from app.en import int_to_words


def index(request):
    """
    Converts an integer represented in digits to words in English.
    :parameter number (query parameter) - the integer in digits
    :return If success: Status 200 and a JSON body with key `status` with
    value "ok" and key `num_in_english` whose value holds the words in
    English.
    If the number is invalid, returns status 401 and a JSON body with key
    `status` with value "error" and key `message` with value explaining the
    error.
    """
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
