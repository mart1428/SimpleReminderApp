import MySQLdb as sql
import getpass, datetime
from Task import Task

class Reminder:
    def __init__(self):
        self.taskList =[]
        self.db = None

    def __str__(self):
        s = "--Reminder--"
        return s

    def create_task(self):
        print("Task: ")
        title = str(input("Title: "))
        description = str(input("Description: "))
        y = int(input("Enter year[yyyy]: "))
        m = int(input("Enter month[mm]: "))
        d = int(input("Enter day[dd]: "))
        dueDate = datetime.date(y, m ,d)

        task = Task(title = title, description = description, dueDate = dueDate)
        return task

    def show_last_added(self):
        print(self.taskList[-1])

    def connectDB(self):
        '''
            connect Python with MySQL, host is set to localhost and user is set to root.
            executes MySQL queries.
        '''
        s = '''
----------
host = localhost
user = root
----------
        '''
 

        host = "localhost"
        user = "root"
        print(s)

        # if dbName == "0":
        #     connect = False

        while True:
            try:
                dbName = str(input("Database Name: ")) #"reminder"

                if dbName == "0":
                    break
                passwd = getpass.getpass(prompt = "Password: ", stream = None)
                db = sql.connect(host = host, user = user, passwd = passwd, db = dbName)


            except:
                print("Invalid Database name and/or password!")
            else:
                break

        self.db = db



    def startSQL(self):
        cur = self.db.cursor()

        while True:
            print("0 to exit SQL")
            cmd = str(input("SQL>> "))
            if(cmd == "0"):
                print("Exiting SQL...")
                break
            else:
                cur.execute(cmd)

            for row in cur.fetchall():
                print(row)


    def loadFromDB(self):
        if(self.db == None):
            self.connectDB()

        try:
            cur = self.db.cursor()
            cur.execute("SELECT task.task_id, title, description, date FROM task LEFT JOIN task_desc ON task.task_id = task_desc.task_id;")

            for row in cur.fetchall():
                loaded_task = Task(row[0], row[1], row[2], row[3])
                self.taskList.append(loaded_task)

        
        except:
            print("Database not found!")

    def saveNewTask(self):
        if(self.db == None):
            self.connectDB()
        
        try:
            cur = self.db.cursor()

            new_task = self.create_task()

            cmd = "INSERT INTO task(title, date) VALUES("

            cmd += '"' + str(new_task.getTitle()) + '"' + ', "' + str(new_task.getDueDate().year) + \
                "-" + str(new_task.getDueDate().month) + "-" + str(new_task.getDueDate().day) + '");' 

            cur.execute(cmd)

            cmd = 'SELECT task_id FROM task WHERE title = "' + str(new_task.getTitle()) + '"'

            cur.execute(cmd)

            task_id = 0
            for row in cur.fetchall():
                print(row)
                task_id = row[0]

            cmd = "INSERT INTO task_desc(task_id, description) VALUES(" + '"' + str(task_id)  + '", "' + str(new_task.getDescription()) + '");'

            cur.execute(cmd)


            self.db.commit()
            self.loadFromDB()

        except Exception as error:
            print("Database not found!", error)

    def printAllTask(self):
        self.loadFromDB()
        
        for task in self.taskList:
            print(task, end="\n\n")

        
            
def displayMenu():
    s = ''' ---Menu---
    C - Connect to Database
    L - Load from Database
    S - Save New Task
    A - Show Last Added
    P - Print All Tasks
    M - Start MySQL Command Line
    D - Display Menu
    Q - Quit Program
    '''
    print(s)

##--Main--
if __name__ == "__main__":
    displayMenu()
    reminder = Reminder()

    choice = str(input("Enter choice: ")).upper()
    while(choice != "Q"):
        if(choice == "C"):
            reminder.connectDB()
        elif(choice == "L"):
            reminder.loadFromDB()
        elif(choice == "S"):
            reminder.saveNewTask()
        elif(choice == "A"):
            reminder.show_last_added()
        elif(choice == "P"):
            reminder.printAllTask()
        elif(choice == "M"):
            reminder.startSQL()
        elif(choice == "D"):
            displayMenu()
        else:
            print("Invalid menu choice!")
        
        choice = str(input("\nEnter choice: ")).upper()