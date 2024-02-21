
import os
import subprocess

def trigger_data_collection():
    try:
        # Ensure logs directory exists
        logs_dir = '/home/cell32/my_flask_airbnb/logs'
        os.makedirs(logs_dir, exist_ok=True)

        # Specify the Python interpreter's absolute path
        python_interpreter = '/home/cell32/my_flask_airbnb/venv/bin/python3'

        subprocess.run([python_interpreter, '/home/cell32/my_flask_airbnb/scripts/data_collector.py'])
        print("Data collection triggered successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    trigger_data_collection()    
