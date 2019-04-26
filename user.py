class User:
    def __init__(self, _name='N/A', _id='N/A', _school='RPI'):
        self.name = _name
        self.id = _id
        self.school = _school
        self.courses = []

    def add_course(self, c):
        self.courses.append(c)

    def get_name(self):
        return self.name

    def get_id(self):
        return self.id

    def get_school(self):
        return self.school

    def course_info(self):
        temp = 'Taking {} courses:\n'.format(len(self.courses))
        for c in self.courses:
            temp += '\t{}\n'.format(c.get_name)
        return temp

    def __str__(self):
        info_string = "Name: {}\nID: {}\nSchool: {}\n Taking {} Courses:"\
            .format(self.name, self.id, self.school, len(self.courses))
        for c in self.courses:
            info_string += "{}".format(c.get_name())
        return info_string
