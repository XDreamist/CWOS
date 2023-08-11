import os
import subprocess

def main():
    folder = os.path.join(os.getcwd(), 'venv')
    activate_script = os.path.join(folder, 'Scripts', 'activate')
    activate_cmd = f'call "{activate_script}"'

    if os.path.exists(folder):
        print('Folder exists')
        subprocess.run([activate_cmd], shell=True)
        subprocess.run(['python', 'manage.py', 'runserver'], shell=True)
    else:
        print('Folder does not exist')
        subprocess.run(['python', '-m', 'venv', folder], shell=True)
        subprocess.run([activate_cmd], shell=True)
        subprocess.run(['pip', 'install', 'django'], shell=True)
        subprocess.run(['pip', 'install', 'Pillow'], shell=True)
        subprocess.run(['python', 'manage.py', 'runserver'], shell=True)

if __name__ == "__main__":
    main()
