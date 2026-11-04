from data import users
from fungsiBantu import input_wajib, input_password, jeda

def register():
    print("---Register---")
    while True:
        try:
            username = input_wajib("Username: ")
            if username in users:
                raise ValueError("Username sudah digunakan!")
            break
        except ValueError as e:
            print(e)
    while True:
        try:
            password = input_password("Password (min. 4 karakter): ")
            if len(password) < 4:
                raise ValueError("Password terlalu pendek.")
            break
        except ValueError as e:
            print(e)
    users[username] = {"password": password, "role": "user"}
    print("Registrasi berhasil, silakan login!")
    jeda()

def login():
    print("---Login---")
    username = input_wajib("Username: ")
    password = input_password("Password: ")
    if username in users and users[username]["password"] == password:
        print("Login berhasil!")
        jeda()
        return username, users[username]["role"]
    else:
        print("Username atau password salah!")
        jeda()
        return "", ""