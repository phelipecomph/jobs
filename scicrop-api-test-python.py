import requests
from datetime import datetime

def send():

	# Getting date times
	now_date = int(datetime.timestamp(datetime.now()))
	degree_time = [int(datetime.timestamp(datetime(2020, 2, 1))), int(datetime.timestamp(datetime(2023, 11, 30)))]

	# URL to post
	url = 'https://engine.scicrop.com/scicrop-engine-web/api/v1/jobs/post_resume'

	# Curriculum Infos
	content = {
		"full_name": "Phelipe Augusto Naves Muller",
		"email": "phelipecomph42@gmail.com",
		"mobile_phone": "+55 (11) 99360-0430",
		"age": 22,
		"home_address": "Santana de Parnaiba, Av Marcos Penteado de Ulhoa Rodrigues 3800",
		"start_date": now_date,
		"opportunity_tag": "dev_intern_200",
		"past_jobs_experience": "I worked as a freelancer to develop a system to automate the customization and sending of emails.",
		"degrees": [{
			"institution_name": "Fatec Carapicuiba",
			"degree_name": "Design de Mídias Digitais",
			"begin_date": degree_time[0],
			"end_date": degree_time[1]
		}],
		"programming_skills": ["python", "javascript"],
		"database_skills": ["postgresql", "sqlite"],
		"hobbies": ["gaming", "spending time with friends", "series", "movies"],
		"why": "I am looking for an environment to develop myself and that I can contribute with my personal characteristics",
		"git_url_repositories": "https://github.com/phelipecomph"
	}

	# Posting
	response = requests.post(url=url, json=content)
	print(response.status_code)

if __name__ == '__main__':
	send()
