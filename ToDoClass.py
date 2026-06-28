

class Task:
    def __init__ (self, taskId=int, title=str, status=bool): 
        self.task_id = taskId
        self.title = title
        self.status = status


#class to store active tasks and completed tasks
#definitions will allow us to manipulate taskLists
class TaskList:
    def __init__ (self, taskListId=int, taskListTitle=str):
        self.taskListId = taskListId
        self.taskListTitle = taskListTitle


    