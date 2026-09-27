notes = []

while True:
    print("\n===== Note Manager =====")
    print("1. Add Note")
    print("2. View Notes")
    print("3. Search Note")
    print("4. Delete Note")
    print("5. Count Notes")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # Add Note
    if choice == "1":
        title = input("Enter note title: ")
        content = input("Enter note content: ")

        note = {
            "title": title,
            "content": content
        }

        notes.append(note)
        print("Note added successfully!")

    # View Notes
    elif choice == "2":
        if len(notes) == 0:
            print("No notes found.")
        else:
            print("\n--- All Notes ---")

            for note in notes:
                print("Title:", note["title"])
                print("Content:", note["content"])
                print("----------------")

    # Search Note
    elif choice == "3":
        title = input("Enter note title to search: ")

        found = False

        for note in notes:
            if note["title"].lower() == title.lower():
                print("\nNote Found!")
                print("Title:", note["title"])
                print("Content:", note["content"])
                found = True
                break

        if not found:
            print("Note not found.")

    # Delete Note
    elif choice == "4":
        title = input("Enter note title to delete: ")

        found = False

        for note in notes:
            if note["title"].lower() == title.lower():
                notes.remove(note)
                print("Note deleted successfully!")
                found = True
                break

        if not found:
            print("Note not found.")

    # Count Notes
    elif choice == "5":
        print("Total Notes:", len(notes))

    # Exit
    elif choice == "6":
        print("Thank you!")
        break

    else:
        print("Invalid choice. Please try again.")
