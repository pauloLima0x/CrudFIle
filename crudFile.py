def main():
  try:
    choice = input("Choice a mode:\nc - create file\nr - read a file\nw - write a file\nx - remove file\n")
    if choice == "c":
       filename = input("Enter the file name you want to create: ")
       file = open(filename + ".txt", "x")
       print("Creating the file " + ".txt...")
       print("File " + filename + ".txt has been created.")
       file.close()
    elif choice == "r":
       filename = input("Enter the file name you want to read: ")
       filename = setExtension(filename)
       print("Reading the content of the file " + filename + "...")
       file = open(filename, "r")
       print(file.read())
       print("Read complete")
    elif choice == "w":
       filename = input("Enter the file name you want to write: ")
       filename = setExtension(filename)
       file = open(filename, "a")
       content = input("Enter the content you want write and press enter: ")
       print("Writing in the file " + filename + "...")
       file.write(content + "\n")
       print("Writing complete")
       file.close()
    elif choice == "x":
       filename = input("Enter the file you want remove: ")
       filename = setExtension(filename)
       print("Removing the file " + filename + "...")
       os.remove(filename)
       print("File " + filename + " removed.")
    else:
       print("Sorry. Invalid choice")

  except FileNotFoundError:
    print("File not found.")
  except KeyboardInterrupt:
    print("\nExiting....")
  except FileExistsError:
    print("File already exists.")

def setExtension(filename):
  check_txt = ".txt" in filename
  if not(check_txt):
      filename = filename + ".txt"
  return filename

if __name__ == "__main__":
    main()
