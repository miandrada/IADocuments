import subprocess

def ejecutar_npm():
    try:
        subprocess.run(['npm', 'run', 'dev'], check=True)
    except subprocess.CalledProcessError as e:
        print("Error al ejecutar 'npm run dev':", e)

if __name__ == "__main__":
    ejecutar_npm()