completed_tasks = '12'
number_of_hors_spent = '1.5'
name_of_course = 'Python'
time_per_task = float(number_of_hors_spent) * 60 / int(completed_tasks)
#print('Курс: ' + name_of_course + ', ' + 'всего задач: ' + completed_tasks + ', ' + 'затрачено часов: '
#      + number_of_hors_spent + ', ' + 'среднее время выполнения задания ' + str(time_per_task) + ' мин.')
print(f"Курс: {name_of_course}; всего задач: {completed_tasks}; затрачено часов: {number_of_hors_spent};"
      f" среднее время выполнения задания: {time_per_task} мин")
