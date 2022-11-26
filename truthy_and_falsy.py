class HealthRecord:
    def __init__(self, height, weight) -> None:
        self.height = height
        self.weight = weight

    def __bool__(self):
        # Calculate the IMC for a person, and return true if it is between
        # the healthy range. If not, it returns false
        return (self.weight / (self.height * self.height)) >= 18.5 and (
            self.weight / (self.height * self.height)
        ) <= 24.9


if __name__ == "__main__":
    person_1 = HealthRecord(1.76, 81)
    print("healthy" if person_1 else "be careful!")
