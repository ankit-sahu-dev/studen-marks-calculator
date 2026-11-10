name = input("Student name: ")

subject_1 = int(input("Enter score for first subject: "))
subject_2 = int(input("Enter score for second subject: "))
subject_3 = int(input("Enter score for third subject: "))



if subject_1 < 0 or subject_1 > 100:
    print("Invalid marks")
elif subject_2 < 0 or subject_2 > 100:
    print("Invalid marks")
elif subject_3 < 0 or subject_3 > 100:
    print("Invalid marks")
else:
    total = subject_1 + subject_2 + subject_3
    percentage = total/300*100
    
    print("\=====STUDENT RESULT=====/")
    print("Student name:", name)
    print("Total marks:", total,"/300")
    print(f"Percentage: {percentage:.2f}%" )
    
    #PASSorFAIL
    if subject_1 < 33 or subject_2 < 33 or subject_3 < 33:
        print("Result: FAIL" )
    else:
        print("Result: PASS")
