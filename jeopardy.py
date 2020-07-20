import requests, random, json
from similar_text import similar_text

#response = requests.get('http://jservice.io/api/clues?category=139').json()
#response = requests.get('http://jservice.io/api/category?id=' + str(random.randint(0, 11500))).json()

#for testing purposes
# response = requests.get('http://jservice.io/api/category?id=6783').json()
# print(type(response))

# for i in response:
#     print(i)
#     print(response[i])

# print(json.dumps(response, indent= 4))
# holdquestion = response['clues'][0]
# print((holdquestion['question']))
# holdans = input('in the form of a question please answer the above ').capitalize()

# if(holdans == holdquestion['answer']):
#     print('magic')
# else:
#     print('the answer was ' + holdquestion['answer'])
score = 0 
completed = []
def jeopardy( testing = False, catselect = random.randint(0,11500)):
    catselect = str(catselect)
    #response = requests.get('http://jservice.io/api/category?id=' + catselect).json()
   # print('the category is ' + response['title'])
    global score
    global completed
    qbank = []
    for i in range(6):
        catselect = str(random.randint(0,11500))
        qbank.append(requests.get('http://jservice.io/api/category?id=' + catselect).json())
    
    while(len(completed) < 30):
        for i in range(6):
            print(qbank[i]['title'], "aka category " + str(i + 1))  
        print('your score is currently ' + str(score))
        boardmaker()
        curcat = int(input('chose a category using the number from above by entering in just the number')) - 1
        print(qbank[curcat]['title'])
        curq = int(input('chose a question using 1 for the first question and 5 for the fifth for a category and above by entering in just the number')) - 1
        #print(qbank[curcat]['clues'][curq])
        question(qbank[curcat ]['clues'][curq ], testing)
        completed.append([curcat ,curq])

def boardmaker():        
    board = []
    for i in range(5):
        line = []
        for j in range(6):
            if([j,i] not in completed):
                line.append('O')
            else:
               line.append('X')
        board.append(line)
    for i in board:
        print(i)

def question(holdquestion, testing = False):
    global score
    if(not(holdquestion['question'] == "")):
        print('your score is ' + str(score))
        print((holdquestion['question']))
        if(testing):
            print('you cheat the answer is ' + holdquestion['answer'])
        if(holdquestion['value'] is None):
            holdquestion['value'] = 1000
        print(type(holdquestion['value']))
        print('worth ' + str(holdquestion['value']))     
        correct = False
        failcounter = 0
        while(failcounter < 3):
            holdans = input('in the form of a question please answer the above ')
            print(similar_text(holdans, holdquestion['answer']))
            holdans = holdans.lower()
            holdquestion['answer'] = holdquestion['answer'].lower()
            if(holdans == holdquestion['answer']):
                print('you got it perfectly right')
                score += holdquestion['value']
                correct = True
                break
            if(similar_text(holdans, holdquestion['answer']) > 90):
                print('close enough')
                score += holdquestion['value']
                correct = True
                break
            if(similar_text(holdans, holdquestion['answer']) > 70):
                print("very close, just a minor typo")
                failcounter += 1
            else:
                failcounter += 1
        if(not(correct)):
            print('the answer was ' + holdquestion['answer'])
    return(False)

#jeopardy(6783, True)
jeopardy(True)

