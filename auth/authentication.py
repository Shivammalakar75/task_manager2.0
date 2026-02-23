from models.user import User
from storage.file_manager import save_users
from auth.password_utils import hash_password,verify_password


def sign_up(users):
    username = input("Enter username: ")
    password = input("Enter password: ")
    confirm = input("Confirm password: ")

    if password != confirm:
        print("Passwords do not match!")
        return
    
    if username in users:
        print("User already exists!")
        return


    hashed_pw = hash_password(password)
    user = User(username, hashed_pw)
    users[username] = user

    save_users(users)

    print("User registered successfully!")

def log_in(users):
    username = input("Enter username: ")
    password = input("Enter password: ")

    user = users.get(username)

    if user and verify_password(password, user.password):
        print("Login successful!")
        return user

    print("Invalid credentials!")
    return None