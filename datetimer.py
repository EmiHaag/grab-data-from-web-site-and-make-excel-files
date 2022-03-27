from datetime import datetime, timedelta

#receive a date like "12/03/22"
#return true if date is passed over 7 days
def passedSevenDays(v):
    sevenDays =datetime.now() - timedelta(days=7)
    ceTime = datetime.strptime(v, "%d/%m/%y")
    print("is " , ceTime , " minor than ", sevenDays , " ? ", ceTime < sevenDays)
    return ceTime < sevenDays

