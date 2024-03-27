def applicantsAcceptance(degree, experience):
    if degree == "Master's" or degree == "PhD" and experience > 2:
        return("We will take you for the job. Congrats!")
    else:
        return("Thank you for applying. Unfortunately, you do not fulfill the requirements necessary for this job.")


print(applicantsAcceptance("Master's", 3))