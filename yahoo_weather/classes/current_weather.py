class Current_Weather:
    def __init__(self, current_observation, forecasts, location):
        self.current_observation = current_observation
        self.forecasts = forecasts
        self.location = location

    def as_dict(self):
        return self.__dict__
