class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score

        print(name, age, tracks, score)

    def change_name(self, name):
        self.name = name
        # return str
        print(name)

    def change_age(self, age):
        self.age = age
        # return int
        print(age)

    def append(self, tracks):
        self.tracks = tracks
        print(tracks)
        # tracks.append()

    def get_score(self, score):
        self.score = score
        print(score)


# Bob.change_name("Peter")
# Bob.add_track("UI/UX")
Bob = Student("Bob", 26, ["FE", "BE"], 20.90)


Bob.change_name("Peter")
Bob.change_age(34)
Bob.append("UI/UX")
Bob.get_score(20.90)


# Expected methods
