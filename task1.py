class Student:
    def __init__(self, surname, name, age):
        self.surname = surname
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.surname} {self.name}, {self.age} years old'


class _StudentsIterator:
    def __init__(self, collections):
        self.index = 0
        self.collections = collections

    def __iter__(self):
        return self

    def __next__(self):
        if self.index > len(self.collections):
            raise StopIteration

        current_student = self.collections[self.index]
        self.index += 1
        return current_student


class Students:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def __iter__(self):
        return _StudentsIterator(self.students)

    def __str__(self):
        return "\n".join([str(student) for student in self.students])


if __name__ == '__main__':
    students = Students()

    students.add_student(Student("Yegorovich", "Dmytro", 22))
    students.add_student(Student("Dmitrovich", "Roman", 12))

    print(students)
