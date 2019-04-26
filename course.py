class Course:
    def __init__(self, _id='0000', _subject='XXXX'):
        self.id = _id
        self.subject = _subject
        self.students = []

    def add_student(self, user):
        self.students.append(user)

    def get_name(self):
        return '{} {}'.format(self.subject, self.id)

    def get_student(self):
        return self.students

    def __str__(self):
        info_string = "Course Name: {} {}\n {} stundents in this class."\
            .format(self.subject, self.id, len(self.subject))
        return info_string
