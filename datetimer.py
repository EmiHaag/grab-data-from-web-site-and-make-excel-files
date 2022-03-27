from datetime import datetime, timedelta

#example = "12/03/22"


def passedSevenDays(v):
    sevenDays =datetime.now() - timedelta(days=7)
    ceTime = datetime.strptime(v, "%d/%m/%y")
    print("is " , ceTime , " minor than ", sevenDays , " ? ", ceTime < sevenDays)
    return ceTime < sevenDays

#print(passedSevenDays(example))
