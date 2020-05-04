from django.shortcuts import render, redirect
from .models import Dogs, UserStats
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def intro(request):
    if request.method == 'GET':
        return render(request, 'intro.html', {})
    else:
        confidence = int(request.POST.get('confidence', 0))
        shyness = int(request.POST.get('shyness', 0))
        independence = int(request.POST.get('independence', 0))
        positive = int(request.POST.get('positive', 0))
        adaptability = int(request.POST.get('adaptability', 0))

        user = {
            'confidence': confidence,
            'shyness': shyness,
            'independence': independence,
            'positive': positive,
            'adaptability': adaptability
        }

        dogs = Dogs.objects.all()
        penalty_dict = {}
        for dog in dogs:
            confidence = abs(user['confidence'] - dog.confidence)
            shyness = abs(user['shyness'] - dog.shyness)
            independence = abs(user['independence'] - dog.independence)
            positive = abs(user['positive'] - dog.positive)
            adaptability = abs(user['positive'] - dog.adaptability)
            penalty = confidence + shyness + independence + positive + adaptability
            penalty_dict[dog.types] = penalty

        penalty_list = sorted(penalty_dict.items(), key = lambda kv: (kv[1], kv[0]))

        penalty_list = penalty_list[:3]

        pivot_penalty = penalty_list[0][1]

        for idx, (types, penalty) in enumerate(penalty_list):
            if penalty != pivot_penalty:
                del penalty_list[idx]
        print(penalty_list)







        # UserStats.objects.create(
        #     confidence=confidence,
        #     shyness=shyness,
        #     independence=independence,
        #     positive=positive,
        #     adaptability=adaptability,
        #     doggy=types,
        # )

        # doggy = types
        return redirect('/doggy/{}'.format(doggy))

@csrf_exempt
def result(request, doggy):
    description = '당신은 어쩌구저쩌구 입니다.'
    return render(request, 'result.html', {
        'doggy': doggy,
        'description': description
    })
