class Face:
    def __init__(self, mouth, mood, eye):
        self.mouth = mouth
        self.mood = mood
        self.eye = eye

    def changeMouth(self):
        if self.mouth == "smile":
            self.mouth = "frown"
        elif self.mouth == "frown":
            self.mouth = "smile"

    def changeMood(self):
        if self.mood == "yellow":
            self.mood = "red"
        elif self.mood == "red":
            self.mood = "yellow"

    def changeEye(self):
        if self.eye == "black":
            self.eye = "blue"
        elif self.eye == "blue":
            self.eye = "black"