
function show_help {  
 echo "Usage: $0 [add|list|remove|help] [task]"  
 echo "Commands:"  
 echo " add Adds a new task"  
 echo " list Lists all tasks"  
 echo " remove Removes a task"  
 echo " help Shows this help message"  
}  

function add_task {  
 if [ -z "$1" ]; then echo "Please provide a task to add."  
 return1 fi echo "$1" >> "$TODO_FILE"  
 echo "Task added: $1"  
}  

function list_tasks {  
 if [ ! -f "$TODO_FILE" ]; then echo "No tasks found."  
 return fi echo "Your To-Do List:"  
 nl -w2 -s'. ' "$TODO_FILE"  
}  

function remove_task {  
 if [ -z "$1" ]; then echo "Please provide a task number to remove."  
 return1 fi if [ ! -f "$TODO_FILE" ]; then echo "No tasks found."  
 return fi sed -i.bak "${1}d" "$TODO_FILE"  
 echo "Task removed: $1"  
}  

case "$1" in add)  
 add_task "$2"  
 ;;  
 list)  
 list_tasks ;;  
 remove)  
 remove_task "$2"  
 ;;  
 help)  
 show_help ;;  
 *)  
 show_help ;;  
esac```  
