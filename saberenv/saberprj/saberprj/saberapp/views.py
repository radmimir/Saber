# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse,Http404
import json


def take_message_from_json(f, maxsize=2048):
    while True:
        data = f.read(maxsize)
        if not data:
            break
        yield data


def application(request):
    print request
    if request.method == 'POST':
        json_str = ((request.body).decode('utf-8'))
        json_obj = json.loads(json_str)
        next_offset = json_obj['offset']
        answer = dict()
        answer["ok"] = True
        try:
            f = open('./saberprj/saberapp/log.txt', 'r')
            total_size = sum(1 for l in f)
            f.close()
            f = open('./saberprj/saberapp/log.txt', 'r')
            for portion in take_message_from_json(f):
                lin = portion.splitlines()
                for line in portion.splitlines():
                    data = json.loads(line)
                    if 'messages' in answer:
                        answer['messages'].append(data)
                    else:
                        answer['messages'] = [data]
                    next_offset += 1
                    answer['next_offset'] = next_offset
                    answer['total_size'] = total_size
        except ImportError:
            answer['reason'] = 'File was not found.'
            answer['ok'] = False
        except IOError:
            answer['reason'] = 'File can not be read.'
            answer['ok'] = False
        except MemoryError:
            answer['reason'] = 'Out of memory exception.'
            answer['ok'] = False
        except:
            answer['reason'] = 'Some another reason.'
            answer['ok'] = False
        return JsonResponse(answer, safe=False)
    else:
        answer = {"ok": False}
        answer['reason'] = 'Irregular request method type = ' + request.method
        return JsonResponse(answer)
