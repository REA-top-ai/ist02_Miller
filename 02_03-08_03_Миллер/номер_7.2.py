answers = ["A", "C", "A", "A", "D",
    "B", "C", "A", "C", "B",
    "A", "D", "C", "A", "D",
    "C", "B", "B", "D", "A"]

with open('student_answers.txt', 'r') as file:
    ans = [line.strip().upper() for line in file]

right = 0
wrong = 0

for i in range(20):
    if ans[i] == answers[i]:
        right += 1
    else:
        wrong += 1

if right >= 15:
    print('экзамен сдан')
else:
    print('экзамен не сдан')

print(f'колво ошибок {wrong}')
print(f'колво правильных ответов {right}')