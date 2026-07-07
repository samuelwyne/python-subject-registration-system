subjects={"Mathematics","English","Physics","Chemistry","Biology"}
print(f"{"="*5}AVAILABLE SUBJECTS{"="*5}")
for subject in subjects:
    print(subject)
registered_subjects=set()
registered_subjects.add(input("Enter a subject you want to register for:"))
while True:
    status=input("Do you want to add on another subject:(Y/N)").upper()
    if status=="Y":
        registered_subjects.add(input("Enter a subject you want to register for:"))
    else:
        break
print()    
print(f"{"="*5}REGISTERED SUBJECTS{"="*5}")
for subject in registered_subjects:
    print(subject)