import PySimpleGUI as sg



def add_task(values):
    task = values['taskname']
    todolist.append(task)
    window.FindElement('taskname').Update(value="")
    window.FindElement('todolist').Update(values=todolist)
    window.FindElement('add_save').Update('Add')
  
def add_priority(v):    
    priority = values['priority']
    p.append(priority)
    window.FindElement('priority').Update(value="")
    window.FindElement('p').Update(values=p)
    window.FindElement('add_save').Update('Add')
    
def add_date(val):
    due_date = str(values['date'])
    date.append(due_date)
    window.FindElement('date').Update(value="")
    window.FindElement('d').Update(values=date)
    window.FindElement('add_save').Update('Add')
    

def prioritise():
    p=[]
    todolist=[]
    temp=0
    temp1=0
    dict1={"High":3,"Medium":2,"Low":1}
    with open("tasks.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                if line!='\n':
                    t=line.strip("\n")
                    todolist.append(t)
    with open("priority.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                if line!='\n':
                    t=line.strip("\n")
                    p.append(t)
                          
                

    for i in range(0,len(p)):
        for j in range(0,len(p)):
            
            if dict1[p[i]]>dict1[p[j]]:
                
                temp=p[i]
                p[i]=p[j]
                p[j]=temp
                temp1=todolist[i]
                todolist[i]=todolist[j]
                todolist[j]=temp1
    window.FindElement('todolist').Update(values=todolist)
    window.FindElement('p').Update(values=p)
            

    
   
    
def edit_tasks(values):
    edit_val = values['todolist'][0]
    drop_value=p[todolist.index(edit_val)]
    date_value=date[todolist.index(edit_val)]
    window.FindElement('taskname').Update(value=edit_val)
    window.FindElement('priority').Update(value=drop_value)
    window.FindElement('date').Update(value=date_value)
    todolist.remove(edit_val)
    date.remove(date_value)
    p.remove(drop_value)
    window.FindElement('add_save').Update('Save')
 
def delete_tasks(values):
    delete_value = values['todolist'][0]
    drop_value=p[todolist.index(delete_value)]
    date_value=date[todolist.index(delete_value)]
    todolist.remove(delete_value)
    p.remove(drop_value)
    date.remove(date_value)
    window.FindElement('todolist').Update(values=todolist)
    window.FindElement('p').Update(values=p)
    window.FindElement('d').Update(values=date)
    save()
    

def save():    
    with open("tasks.txt", "w") as f:
        for line in todolist :
            f.write(line+'\n')
    with open("priority.txt", "w") as f:
        for line in p :
            f.write(line+'\n')        
    with open("due.txt", "w") as f:
        for line in date :
            f.write(line+'\n')        
layout = [
    [sg.Text("Enter the task", font=("Arial", 14)),
     sg.InputText("", font=("Arial", 14), size=(15,1),key="taskname"),
     sg.Text("priority", font=("Arial", 14)),
     sg.Combo(["High","Medium","Low"],key="priority"),
     sg.Text("due date", font=("Arial", 14)),
     sg.InputText("", font=("Arial", 14), size=(15,1),key="date"),
     sg.Button("open", font=("Arial", 14), key="add_save")],
    [sg.Listbox(values=[], size=(15, 10), font=("Arial", 14), key='todolist'),
     sg.Listbox(values=[], size=(10,10), font=("Arial", 14), key='p'),
     sg.Listbox(values=[], size=(15,10), font=("Arial", 14), key='d'),
     sg.Button("Edit", font=("Arial", 14)),
     sg.Button("Delete", font=("Arial", 14)),
     sg.Button("prioritise",font=("Arial", 14))],
    [sg.Button("Exit",font=("Arial", 14))]
]
todolist = []
p=[]
v=[]
date=[]
val=[]
window = sg.Window("Week1", layout)

a=0            
while True:
    event, values= window.Read()
    if a==0 and event == 'add_save':
        with open("tasks.txt", "r") as f:
            lines = f.readlines()
        for line in lines:
            if line!='\n':
                t=line.strip("\n")
                todolist.append(t)
                window.FindElement('todolist').Update(values=todolist)
         

            
        
        with open("priority.txt", "r") as f:
            lines = f.readlines()
        for line in lines:
            if line!='\n':
                t=line.strip("\n")
                p.append(t)
                window.FindElement('p').Update(values=p)

        with open("due.txt", "r") as f:
            lines = f.readlines()
        for line in lines:
            if line!='\n':
                t=line.strip("\n")
                date.append(t)
                window.FindElement('d').Update(values=date)        
         

            
        a=1
        window.FindElement('add_save').Update('Add')
    elif event == 'add_save':
         add_task(values)
         add_priority(values)
         add_date(values)
         save()
        
    elif event =='Edit':
         edit_tasks(values)
         save()
         
    elif event == 'Delete':
         delete_tasks(values)
         save()
        
    elif event == 'prioritise':
         prioritise()
      
    else:
        save()
        break
window.Close()
