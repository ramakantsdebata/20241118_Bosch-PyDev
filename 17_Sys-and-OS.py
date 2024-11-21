import sys
import os

def demo_sys():

    for idx, arg in enumerate(sys.argv):
        print(idx, ":", arg)

    print("\n", "#"*50, "\n", sep='')
    for idx, path in enumerate(sys.path):
        print(idx, ":", path)


    print("\n", "#"*50, "\n", sep='')
    print(sys.version)


def demo_os():
    curr_dir = os.getcwd()
    print(f"Current directory --> {curr_dir}")

    new_dir = "demo_folder"
    # new_dir_path = curr_dir + "/" + new_dir    
    new_dir_path = os.path.join(curr_dir, new_dir)
    print(f"New dir Path --> {new_dir_path}")

    # List all contents of the current directory
    contents = os.listdir(curr_dir)
    for idx, entity in enumerate(contents):
        print(f"\t{idx}: {entity}")

    # Create folder using os.mkdir()
    if os.path.exists(new_dir_path):
        print(f"The path [{new_dir_path}] already exists.")
    else:
        os.mkdir(new_dir_path)
        print(f"Folder [{new_dir_path}] created.")

    # Create a path for a file in the new folder
    new_file = "demo_file.txt"
    new_file_path = os.path.join(new_dir_path, new_file)

    # Create the file
    try:
        file = open(new_file_path, "w")
        print(type(file))
        # file.close()
    except Exception as ex:
        print(f"EXCEPTION --> {ex!r}")
    finally:
        file.close()

    with open(new_file_path, mode="w") as file:
        # Write data into the file
        file.write("this is the first line\n")
        file.writelines(["Second\n", "Third\n", "Fourth\n"])
        

    with open(new_file_path, mode="r") as file:
        # Read data from the file
        s1 = file.read(10)
        print(s1)
        file.seek(0, 0)
        s2 = file.readline()
        print(type(s2), s2)
        file.seek(0, 0)
        s3 = file.readlines()
        print(type(s3), s3)

    with open(new_file_path, mode="r") as file:
        # Read file as an iterator
        for line in file:
            print(line, end='')


    # Remove the file
    if os.path.exists(new_file_path):
        os.remove(new_file_path)
        print(f"File [{new_file_path}] removed.")
    else:
        print(f"File [{new_file_path}] not present.")

    # Remove directory
    if os.path.exists(new_dir_path):
        os.rmdir(new_dir_path)
        print(f"Folder [{new_dir_path}] removed.")


if __name__ == "__main__":
    # demo_sys()
    demo_os()
