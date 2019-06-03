from django.shortcuts import render


def index(request):
    return render(request, 'utils/index.html')

def artii(request, keyword):
    import art
    result = art.text2art(keyword, 'random')
    context = {
        'result':result,
        'keyword': keyword,
    }
    return render(request, 'utils/artii.html', context)


def stock(request):
    return render(request, 'utils/stock.html') #todo: 완성하기
