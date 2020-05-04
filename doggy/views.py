from django.shortcuts import render, redirect
from .models import Dogs, Question, Choice
from django.views.decorators.csrf import csrf_exempt
import random

@csrf_exempt
def intro(request):
    if request.method == 'GET':
        questions = Question.objects.all()
        choices = Choice.objects.all()
        return render(request, 'intro.html', {
            'questions': questions,
            'choices': choices,
            })
    else:
        questions = Question.objects.all()
        number_of_question = len(questions)
        choices = []

        user = {
            'Confidence': 0,
            'Shyness': 0,
            'Independence': 0,
            'Positiveness': 0,
            'Adaptability': 0
        }

        for i in range(number_of_question):
            i = i + 1
            pk = int(request.POST.get('radio-container{}'.format(str(i))))
            choice = Choice.objects.get(pk=pk)
            personality = choice.question.personality
            score = choice.score
            user[personality] = user[personality] + score

        dogs = Dogs.objects.all()
        penalty_dict = {}
        for dog in dogs:
            confidence = abs(user['Confidence'] - dog.confidence)
            shyness = abs(user['Shyness'] - dog.shyness)
            independence = abs(user['Independence'] - dog.independence)
            positiveness = abs(user['Positiveness'] - dog.positiveness)
            adaptability = abs(user['Adaptability'] - dog.adaptability)
            penalty = confidence + shyness + independence + positiveness + adaptability
            penalty_dict[dog.breed] = penalty

        penalty_list = sorted(penalty_dict.items(), key = lambda kv: (kv[1], kv[0]))

        penalty_list = penalty_list[:3]

        pivot_penalty = penalty_list[0][1]

        for idx, (breed, penalty) in enumerate(penalty_list):
            if penalty != pivot_penalty:
                del penalty_list[idx]

        breed, penalty = penalty_list[random.randint(0, len(penalty_list)-1)]

        return redirect('/doggy/{}'.format(breed))

@csrf_exempt
def result(request, doggy):
    dog = Dogs.objects.get(breed=doggy)
    return render(request, 'result.html', {
        'dog': dog
    })
