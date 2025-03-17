amount=int(input())
five_hundred_notes=amount//500
rem=amount%500
print("Five Hundred notes(500):" + str(five_hundred_notes))
hundred_notes=rem//100
rem=rem%100
print("Hundred notes(100):" + str(hundred_notes))
fifty_notes=rem//50
rem=rem%50
print("Fifty Notes(50):" + str(fifty_notes))
ten_notes=rem//10
rem=rem%10
print("Ten Notes(10):" + str(ten_notes))
