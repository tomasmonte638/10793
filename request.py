import requests as rex
 
nome_procurado = "Pedro Carlos Mestre dos Santos".lower()
 
for i in range(3000, 7194):
    url = f"https://trainingserver.atec.pt/TrainingServer/Mulberry/JSON/Controls/Calendar/getCalendarDataSource.ashx?command=_SelectAllSchedulesDataSetGivenByUserId&oId=%7Bi%7D&idField=DataValueField&titleField=DataTextField&startDateField=DataStartField&endDateField=DataEndField&backgroundColorField=&textColorField=textcolor&eventColorField=color&description=description&picField=pic&urlField=url&start=1771804800&end=1772409600&_=%7B1771940484594%7D%22
    response = rex.get(url)
    texto = response.text.lower()
    print(i, "verificado")
 
    if nome_procurado in texto:
        print(f"\nNome encontrado no ID {i}!")
        print("Resposta:", response.text)
        break