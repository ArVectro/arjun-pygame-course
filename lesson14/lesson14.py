#Applicants must have a masters degree _and_ more than 2 yrs of experience

degree = input("What is your degree? Pick from 'PhD', 'Master's', 'Bachelor's', or 'No degree' ")
experience = int(input("How many years of experience do you have? "))


if degree == "Master's" or degree == "PhD" and experience > 2:
    print("We will take you for the job. Congrats!")
else:
    print("Thank you for applying. Unfortunately, you do not fulfill the requirements necessary for this job.")