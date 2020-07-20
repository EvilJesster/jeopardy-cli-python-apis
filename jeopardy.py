import requests, random, json

#response = requests.get('http://jservice.io/api/clues?category=139').json()
#response = requests.get('http://jservice.io/api/category?id=' + str(random.randint(0, 11500))).json()

#for testing purposes
response = requests.get('http://jservice.io/api/category?id=6783').json()
print(type(response))
#print(response)
for i in response:
    print(i)
    print(response[i])

print(json.dumps(response, indent= 4))
holdquestion = response['clues'][0]
print((holdquestion['question']))
holdans = input('in the form of a question please answer the above ').capitalize()
#print(response[0]['question'])
if(holdans == holdquestion['answer']):
    print('magic')
else:
    print('the answer was ' + holdquestion['answer'])

