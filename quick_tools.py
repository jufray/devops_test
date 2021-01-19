import sqlite3

def get_rooms(db_path):
  connect = sqlite3.connect(db_path)
  cursor = connect.cursor()

  sql = 'SELECT room_name FROM Rooms;'

  rooms = cursor.execute(sql ).fetchall()

  rooms = [room[0] for room in rooms]

  return rooms


def verify_room_type(room_type):
  if ((room_type =='public') or (room_type == 'private')):
    return True
  return False

def verify_user_password(user_password):
  cpt_spe_char = 0
  cpt_digit = 0
  list_spe_char = [ '@', '{', '}', '!', '"', '#', '(', ')', '/', '*', ':', ';', '=', '|', '~']
  list_digit = ['0', '1', '2', '3', '4', '5', '6', '7', '9']
  if (len(user_password) <= 8):
    return False

  for e in user_password :
    if (e in list_digit):
      cpt_digit = cpt_digit + 1
    if (e in list_spe_char):
      cpt_spe_char = cpt_spe_char + 1
    if (e == ' '):
      return False

  if (cpt_digit<2):
    return False

  if (cpt_spe_char == 0):
    return False

  return True


def add_room(db_path, room_name, room_type):
  connect = sqlite3.connect(db_path)
  cursor = connect.cursor()

  sql = 'INSERT INTO Rooms (room_name,room_type) VALUES (?,?)'

  cursor.execute(sql,(room_name, room_type))
  connect.commit()


def delete_room(db_path, room_name):
  connect = sqlite3.connect(db_path)
  cursor = connect.cursor()

  sql = 'DELETE FROM Rooms WHERE room_name=?'

  cursor.execute(sql,(room_name,))
  connect.commit()


def get_users(db_path):
  connect = sqlite3.connect(db_path)
  cursor = connect.cursor()

  sql = 'SELECT user_name FROM Users;'

  users = cursor.execute(sql ).fetchall()

  users = [user[0] for user in users]

  return users


def add_user(db_path, user_name, user_role, user_rights, user_password):
  connect = sqlite3.connect(db_path)
  cursor = connect.cursor()

  sql = 'INSERT INTO Users (user_name, user_role, user_rights, user_password) VALUES (?,?,?,?)'

  cursor.execute(sql,(user_name, user_role, user_rights, user_password))
  connect.commit()


def delete_user(db_path, user_name):
  connect = sqlite3.connect(db_path)
  cursor = connect.cursor()

  sql = 'DELETE FROM Users WHERE user_name=?'

  cursor.execute(sql,(user_name,))
  connect.commit()

def create_db(db_path):
  connect = sqlite3.connect(db_path)

  cursor = connect.cursor()

  cursor.execute('CREATE TABLE Rooms ([id_room] INTEGER PRIMARY KEY,[room_name] text UNIQUE, [room_type] text)')
  cursor.execute('CREATE TABLE Users ([id_user] INTEGER PRIMARY KEY,[user_name] text UNIQUE, [user_role] integer, [user_rights] integer, [user_password] text)')

  connect.commit()

# Db creation :
#db_path = 'quick_chat.db'

#create_db(db_path)

# add_user('quick_chat.db','yann.c',0,0,'password')
# add_room('quick_chat.db','room0','public')

# print(get_users(db_path))
# print(get_rooms(db_path))
# delete_user(db_path,'yann.c')