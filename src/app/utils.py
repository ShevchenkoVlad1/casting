import inspect

import simplejson


# декоратор добавляющий поддержку application/json без заморочек
def body_parser(function):
    def wrapper(self, request, *args, **kwargs):

        # Если декорируемая функция принимает аргумент data,
        # значит нужно передать туда то что нужно
        # Это реализованно для поддержки application/json
        # запросов на ровне с обычными POST запросами
        if "data" in inspect.getargspec(function).args:
            if request.META['CONTENT_TYPE'].startswith('application/json'):
                request_data = simplejson.loads(request.body)
            elif request.META['CONTENT_TYPE'].startswith(
                    'application/x-www-form-urlencoded'):
                # Формой можно отправить только GET и POST
                if request.method == "GET":
                    request_data = request.GET
                elif request.method == "POST":
                    request_data = request.POST
                else:
                    raise ValueError(
                        "Request method: {} "
                        "not allowed for CONTENT_TYPE: {}".format(
                            request.method, request.META['CONTENT_TYPE']))
            else:
                raise ValueError("Unknown content type: '{}'".format(
                    request.META['CONTENT_TYPE']))
            kwargs['data'] = request_data

        return function(self, request, *args, **kwargs)

    return wrapper
