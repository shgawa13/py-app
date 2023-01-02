import sqlite3

db = sqlite3.connect('app.db')  # we connect the app to the database
cr = db.cursor()  # setting up the curser


def save_and_close():
    """save and and close the connection"""
    db.commit()
    db.close()


welcome_message = """
Please Choose one option:
 's'=> Show all skill 
 'a'=> Add new skill 
 'u'=> Update skill
 'd'=> Delete skill 
 'q'=> Quit the app
 """
uid = 1

command_list = ['s', 'a', 'u', 'd', 'q']

# create function that match each command


def show_skills():
    cr.execute(f'select * from skills where user_id ="{uid}"')
    result = cr.fetchall()
    if len(result) > 0:
        print(f'you have {len(result)} skills')
    for row in result:
        print(f'skill => {row[1]}, the progress is {row[2]}%')


def add_skill():
    """ add new skill """
    skname = str(input('Type the skill name: ').strip().capitalize())
    cr.execute(
        f'select name from skills where name = "{skname}" and user_id ="{uid}"')
    result = cr.fetchone()
    if result == None:
        print('Nice, you got a new skill :)')
        prog = int(input('Type the skill progress: ').strip())
        cr.execute(
            f'insert into skills(user_id,name,progress) values("{uid}","{skname}","{prog}")')
        print(f'the skill {skname} and progress has been added successully')
        save_and_close()
    else:
        print(f'Sorry {skname} is already exist :(')
        change = str(
            input('the do you like to update it?: "Y" or "N"').strip().lower())
        if change == "y":
            prog = int(input('Type the skill progress: ').strip())
            cr.execute(
                f'update skills set progress = "{prog}" where name = "{skname}" and  user_id = "{uid}"')
            print(
                f'the skill {skname} with the {prog}% progress has been updated successully')
            save_and_close()
        else:
            quit


def update_skill():
    skname = str(input('Type the skill name: ').strip().capitalize())
    prog = int(input('Type the skill progress: ').strip())
    cr.execute(
        f'update skills set progress = "{prog}" where name = "{skname}" and user_id = "{uid}"')
    print(f'the skill new {skname}  progress has been updated successully')
    save_and_close()


def delete_skill():
    skname = str(input('Type the skill name: ').strip().capitalize())
    cr.execute(
        f'delete from skills where name = "{skname}" and user_id = "{uid}"')
    print(f'the skill {skname} and progress has been deleted successully')
    save_and_close()


user_inpt = str(input(f'{welcome_message} Your option: ').strip().lower())

if user_inpt in command_list:
    # if user input in the list of commands we call the function
    if user_inpt == 's':
        show_skills()
    elif user_inpt == 'a':
        add_skill()
    elif user_inpt == 'u':
        update_skill()
    elif user_inpt == 'd':
        delete_skill()
    else:
        print('The app has been closed, Thank you')
else:
    print(f'sorry there is no command with {user_inpt}')
