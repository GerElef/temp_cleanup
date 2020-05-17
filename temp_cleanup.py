from tempfile import gettempdir
from os       import listdir, remove


def deleteFiles(directory):
    files = listdir(directory)
    for filename in files:
        try:
            remove(f"{directory}\{filename}")
            print(f"Cleaned up temporary file {filename}")
        except PermissionError:
            print(f"Cannot delete file {filename}")

if __name__ == "__main__":
    deleteFiles(gettempdir())
