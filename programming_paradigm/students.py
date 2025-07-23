class students :
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")
    def is_passing(self):
        return self.grade >= 60
# Example usage
student1 = students("Alice", 20, 85)
student2 = students("Bob", 19, 55)
student1.display_info()
student2.display_info()
print(f"{student1.name} is {'passing' if student1.is_passing() else 'not passing'}.")
print(f"{student2.name} is {'passing' if student2.is_passing() else 'not passing'}.")