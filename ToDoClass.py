

class Task:
    def __init__ (self, taskId: int, title: str): 
        self.task_id = taskId
        self.title = title
        self.completed = False


#class to store active tasks and completed tasks
#definitions will allow us to manipulate taskLists
class TaskList:
    def __init__ (self):
        self.tasks = {}
        self._next_id = 1


    
    def view_tasks(self):
        if self.tasks:
            print("Tasks:\n")
            for key, value in self.tasks.items(): 
                print(f"{key}. {value}\n")
        else:
            print("No active tasks.\n")

    def delete_task(self, task_id):
        pass

    def add_task(self, title):
        """Add a new task to the task list.
        anywhere we see 'self' that is because
        in main.py we specify 'activeTaskList' 
        so use self to refer to...itself """

        #create new task object
        #pass placeholders for anything we intend to change 
        #in this function, i.e. name and id
        new_task = Task(0, title)
               
        
        #set the task_id for our new_task object
        new_task.task_id = max(self.tasks, default=0) + 1
        #add the task_id and name to our activeTaskList declared below
        self.tasks[new_task.task_id] = title
        #print back to user for confirmation
        print(f"Task '{title}' added as Task {new_task.task_id}.\n")
        
    
    
    def mark_task_complete(self, task_id):
        pass 

