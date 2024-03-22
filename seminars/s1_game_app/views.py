import logging

from django.http import HttpResponse
from django.shortcuts import render

from random import choice, randint

logger = logging.getLogger(__name__)


def heads_and_tails(request):
    answer = f'{choice(['Орел', 'Решка', ])}'
    logger.info(f'Орел или Решка: {answer}')
    return HttpResponse(answer)


def roll_the_dice(request):
    answer = f'{randint(1, 6)}'
    logger.info(f'Бросок кубика: {answer}')
    return HttpResponse(answer)


def random_number(request):
    answer = f'{randint(0, 100)}'
    logger.info(f'Случайное число от 1 до 100: {answer}')
    return HttpResponse(answer)
