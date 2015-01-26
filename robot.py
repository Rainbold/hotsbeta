import requests


def fct(id):
	print '-------------------'
	print id
	cookies = dict(JSESSIONID='', __utma='', __utmz='', __atuvc='', PHPSESSID='')
	payload = {'participantSweepstake.channel':'facebook', 'participant.firstName':'charlie','participant.lastName':'charliie',
	'participant.address1': '', 'participant.city': '', 'participant.postCode':'', 'participant.facebookId':'',
	'participant.email':'charlie'+str(id)+'@yopmail.com', 'participant.mobilePhone':'', 'participantAnswers[0].questionAnswer.id':'263363','ivs':''}

	r = requests.get("http://production.digibonus.com/digibonus/registration/28716", params=payload, cookies=cookies)
	print r.text

	payload = {'parentSweepstakeUrl':'','facebookIds':'',
	'friends[0].name':'charlie','friends[0].email':'charlie1'+str(id)+'@yopmail.com',
	'friends[1].name':'charlie', 'friends[1].email':'charlie2'+str(id)+'@yopmail.com',
	'friends[2].name':'charlie', 'friends[2].email':'charlie3'+str(id)+'@yopmail.com',
	'friends[3].name':'charlie', 'friends[3].email':'charlie4'+str(id)+'@yopmail.com',
	'friends_count':''}


	r = requests.get("http://production.digibonus.com/digibonus/friends/28716", params=payload, cookies=cookies)

	if r.text.find('winner') != -1:
		return id
	else:
		print r.text
		return -1

for i in range(100,3000):
	n = fct(i)
	if n != -1:
		print "/!\ FINI "+str(n)
		break
