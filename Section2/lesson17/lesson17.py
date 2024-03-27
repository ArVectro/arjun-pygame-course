def homework_task(language, task): # language and task are the variables the function is assigning values to when the function is called
    print('Your homework task: ')
    print(task + ' in ' + language)

print('Start')

homework_task('Java', 'Write a function') 
homework_task(task='Code well', language='C++') # We can switch these around by defining the variables
print('End')