class Student:

    def __init__(self, surname, name, group, birth_date, rating):

        self.surname = surname
        self.name = name
        self.group = group
        self.birth_date = birth_date
        self.rating = rating

    def __str__(self):

        return f"(Student: surname - {self.surname}," \
               f" name - {self.name}," \
               f" group - {self.group}," \
               f" birth_date - {self.birth_date}," \
               f" rating - {self.rating})"