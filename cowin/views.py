from django.apps import AppConfig
from django.http import HttpResponse
import requests
from datetime import date
from datetime import timedelta

def index(request):
	today = date.today()
	avail = 0;
	html = "<html><body>"
	html += "<br> ***** slot for age group between 18-45 **** <br>"
	for i in range(0,7):
			today = today + timedelta(days=i)
			d1 = today.strftime("%d-%m-%Y")

			URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=777&date=" + d1
			#URL2 = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode=390011&date=" + d1

			r = requests.get(url = URL)
			data = r.json()
			try:
				if(data['centers']):
						for center in data['centers']:
								min_age_limit = center['sessions'][0]['min_age_limit']
								avialable_slot = center['sessions'][0]['available_capacity']
								if(min_age_limit != 45 and avialable_slot > 0):
										center_name = center['name']
										pincode = center['pincode']
										on_date = center['sessions'][0]['date']
										html += "<br>*********************<br>"
										avail = 1
										html += ("center_name:%s<br>pincode:%s<br>avialable_slot:%s<br>min_age_limit:%s<br>on_date:%s"
										 %(center_name, pincode,avialable_slot,min_age_limit,on_date))
										html += "<br>*********************<br>"
			except:
				pass
									
	if(avail == 0):
		html += "<br> ***** still no luck to get slot for age group between 18-45 **** <br>"
		
		
		
		
	html += "<br> ***** slot for age group above 45 **** <br>"
	today = date.today()
	avail = 0;
	for i in range(0,7):
			today = today + timedelta(days=i)
			d1 = today.strftime("%d-%m-%Y")

			URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=777&date=" + d1
			#URL2 = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode=390011&date=" + d1

			r = requests.get(url = URL)
			data = r.json()
			try:
				if(data['centers']):
						for center in data['centers']:
								min_age_limit = center['sessions'][0]['min_age_limit']
								avialable_slot = center['sessions'][0]['available_capacity']
								if(min_age_limit >= 45 and avialable_slot > 0):
										center_name = center['name']
										pincode = center['pincode']
										on_date = center['sessions'][0]['date']
										html += "<br>*********************<br>"
										avail = 1
										html += ("center_name:%s<br>pincode:%s<br>avialable_slot:%s<br>min_age_limit:%s<br>on_date:%s"
										 %(center_name, pincode,avialable_slot,min_age_limit,on_date))
										html += "<br>*********************<br>"
			except:
				pass
	
	html += "</body></html>"
	return HttpResponse(html)
            
