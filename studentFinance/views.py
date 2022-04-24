from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def get_index(request):
    return render(request, 'index.html')

def display_bank(request):
	data = {
		'firstName': request.POST['firstName'],
		'lastName': request.POST['lastName'],
        'university': request.POST['university'],
		'dining':int(request.POST['dining']),
		'housing':int(request.POST['housing']),
		'salary':int(request.POST['salary']),
		'parking':int(request.POST['parking']),
		'annualTuition':int(request.POST['annualTuition']),
		'budget':int(request.POST['budget'])
	}
	cost = data['dining'] + data['housing'] + data['parking'] + (data['annualTuition'] // 12)
	amountSpent = cost - data['salary']
	amountLeft = data['budget'] - amountSpent

	costData = {
		'restaurants': 0.2 * amountLeft,
		'groceries': 0.3 * amountLeft,
		'medicalSupplies': 0.05 * amountLeft,
		'travel': 0.2 * amountLeft,
		'others': 0.25 * amountLeft
	}
	
	
	return render(request, 'bank.html', {'data': data, 'costData': costData})
