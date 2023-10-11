
import tkinter.messagebox as messagebox
def login_function(user_id,input_password):

    password=int(input_password)
    default_password=123
    default_user_id="user"
    if(user_id==default_user_id):
        if(password==default_password):
            
            messagebox.showinfo(title="Log in status",message="    Log in succefully   ")
    else:
        messagebox.showwarning(title="Log in status",message="   Log in unsuccefully  ")

        





