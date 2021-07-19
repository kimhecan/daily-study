countList = [0, 0, 0]

buttonList = [300, 60, 10]

time = int(input())
for idx, button in enumerate(buttonList):
    if button <= time:
        countList[idx] = time // button
        time = time % button

if time == 0:
    for i in countList:
        print(i, end=" ")
else:
    print(-1)
