exams_Score=[20,45,56,66,67,46,85,45,21,89]
print(len(exams_Score))
print(exams_Score[2])
print(exams_Score[-2])
print(exams_Score[2:5])
print(exams_Score[2:10])
exams_Score[2]='orange'
print(exams_Score)
exams_Score[9]='banana'
print(exams_Score)
exams_Score[0]='apple'
print(exams_Score)
exams_Score.append('grapes')
print(exams_Score)
exams_Score.insert(4,'Davis')
print(exams_Score)

agentMoves=[True,34,'apple','Raymond']
exams_Score.extend(agentMoves)
print(exams_Score)


edible_fruits=['grapes','banana','guava','apple','pineapple']
print(len(edible_fruits))
print(edible_fruits)
print(edible_fruits[0])
print(edible_fruits[4])
edible_fruits.append('orange')
print(edible_fruits)
edible_fruits[1]='lion'
print(edible_fruits)

EuropeCountries=("albania","spain","germany")
print(EuropeCountries)