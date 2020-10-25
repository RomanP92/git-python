class LoggableList(list, Loggable):
    def append(self, val):
        super(LoggableList, self).append(val)
        self.log(val)