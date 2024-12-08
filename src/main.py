import os

if __name__ == "__main__":
    # Print all environment variables line by line
    for key, value in os.environ.items():
        print(f"{key}: {value}")
