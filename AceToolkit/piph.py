import subprocess
import sys




def install(module):
    # load in a module
    package_to_install = module
    try:
        result = subprocess.run(
            # Talk to the system to install a package through pip
            [sys.executable, "-m", "pip", "install", package_to_install],
            capture_output=True,
            text=True,
            check=True
        )
        print(f"Successfully installed {package_to_install}.")
        print("STDOUT:", result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error installing {package_to_install}:")
        print("STDERR:", e.stderr)
    except FileNotFoundError:
        print(f"Error: Python executable not found at {sys.executable}")
