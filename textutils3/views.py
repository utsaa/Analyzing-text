from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    params= {'name':'Harry', 'place': 'Mars'}
    return render(request ,'index.html', params)
    # return  HttpResponse('<h1>Home</h1>')



def analyze(request):
    djtext=request.POST.get('text', 'default')
    removepunc=request.POST.get('removepunc', 'off')
    fullcaps=request.POST.get('fullcaps', 'off')
    newlineremover=request.POST.get('newlineremover', 'off')
    exspace=request.POST.get('exspace','off')
    charcnter=request.POST.get('charcnter','off')
    ans='';analyzed=''
    if removepunc=='on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""

        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        # params={'purpose': 'remove punctuations', 'analyzed_text':\
        #         analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', params)
    if fullcaps=='on':
        analyzed=''
        for char in djtext:
            analyzed+=char.upper()
        # params = {'purpose': 'remove punctuations', 'analyzed_text': \
            # analyzed}
        # return render(request,'analyze.html',params)
        djtext=analyzed
    if newlineremover=='on':
        analyzed = ''
        for char in djtext:
            if char!='\n' or char!='\r':
                analyzed += char.upper()
        # params = {'purpose': 'remove punctuations', 'analyzed_text': \
        #     analyzed}
        # return render(request, 'analyze.html', params)
        djtext=analyzed
    if exspace=='on':

        analyzed = ''
        for i,char in enumerate(djtext):
            if char==' ' and i+1<len(analyzed) and  djtext[i+1]==' ': continue
            analyzed += char.upper()
        # params = {'purpose': 'remove punctuations', 'analyzed_text': \
        #     analyzed}
        # return render(request, 'analyze.html', params)
        # djtext=analyzed
    if charcnter=='on':
        djtext=djtext.replace(' ','')
        ans='The number of characters are '+str(len(djtext))
        # params = {'purpose': 'remove punctuations', 'analyzed_text': \
        #     ans}
        # return render(request, 'analyze.html', params)
    if not analyzed and not ans: return HttpResponse('Error')
    if ans and analyzed:
        params = {'purpose': 'remove punctuations', 'analyzed_text': \
            analyzed+'\n'+ans}
        return render(request,'analyze.html',params)
    if ans:
        params = {'purpose': 'remove punctuations', 'analyzed_text': \
            ans}
        return render(request, 'analyze.html', params)
    else:
        params = {'purpose': 'remove punctuations', 'analyzed_text': \
            analyzed}
        return render(request, 'analyze.html', params)





