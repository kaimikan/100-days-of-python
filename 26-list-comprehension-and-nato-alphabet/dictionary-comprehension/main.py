import random
import pandas

# visualization: new_dict = {new_key:new_value for item in list}
students = ["Bob", "Steve", "Phil", "Bill", "Joe"]

# visualization: student_scores = {new_key:new_value for item in names}
student_scores = {student: random.randint(1, 100) for student in students}
print(student_scores)

passed_students = {student: student_scores[student] for student in student_scores if student_scores[student] > 50}
print(passed_students)
# lecturer solution
print(student_scores.items())
# makes it into tuples, and we can separate student and score (key and value) into separate variables
passed_students = {student: score for (student, score) in student_scores.items() if score > 50}
print(passed_students)

# exercise 1
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
words = sentence.split(" ")
sentence_words = {word: len(word) for word in words}
print(sentence_words)

# exercise 2
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# method 1
weather_fahrenheit = {day: temperature * 9 / 5 + 32 for (day, temperature) in weather_c.items()}
print(weather_fahrenheit)
# method 2
weather_fahrenheit = {day: weather_c[day] * 9 / 5 + 32 for day in weather_c}
print(weather_fahrenheit)

# iterating over a pandas DataFrame
student_dict = {
    "student": ["Bob", "Steve", "Phil", "Bill", "Joe"],
    "score": [56, 76, 98, 42, 72]
}

# Loop through dictionary
# for (key, value) in student_dict.items():
#     print(value)

student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

# # Loop through data frame
# for (key, value) in student_data_frame.items():
#     print(key, value)

# # Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # each of these rows is a pandas Series object
    print(row)
    print(row.student, row.score)
