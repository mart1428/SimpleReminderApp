class Task:
    #Constructors
    def __init__(self, task_id = None, title = None, description = None, dueDate = None):
        self.__task_id = task_id
        self.__title = title
        self.__description = description
        self.__dueDate = dueDate

    def __str__(self):
        y = str(self.__dueDate.year)
        m = str(self.__dueDate.month)
        d = str(self.__dueDate.day)
        s = "--Task--\nTitle: " + self.__title + "\nDescription: " + self.__description + "\nDue Date: " + \
            d + "/" + m + '/' + y
        # str(self.__dueDate.day) + "/" + str(self.__dueDate.month) + "/" + str(self.__dueDate.year)
        return s

    #Setters
    def setTitle(self, title):
        self.__title = title

    def setDescription(self, description):
        self.__description = description

    def setDueDate(self, dueDate):
        self.__dueDate = dueDate

    #Getters
    def getTaskID(self):
        return self.__task_id
    def getTitle(self):
        return self.__title

    def getDescription(self):
        return self.__description

    def getDueDate(self):
        return self.__dueDate