from models import create_student
from services import *
from utils import display_student

database = []

def menu():
    print("\n===== MENU =====")
    print("1. Ajouter étudiant")
    print("2. Afficher étudiants")
    print("3. Moyenne étudiant")
    print("4. Quitter")


while True:
    menu()
    choice = input("Choix : ")

    if choice == "1":
        nom = input("Nom : ")
        notes = input("Notes (séparées par virgules) : ")

        notes_list = [float(n) for n in notes.split(",")]

        student = create_student(nom, notes_list)
        add_student(database, student)

        print("Étudiant ajouté ✔")

    elif choice == "2":
        for student in get_all_students(database):
            display_student(student)

    elif choice == "3":
        nom = input("Nom étudiant : ")
        student = find_student(database, nom)

        if student:
            avg = calculate_average(student)
            print(f"Moyenne: {avg:.2f}")
        else:
            print("Étudiant introuvable")

    elif choice == "4":
        print("Bye 👋")
        break

    else:
        print("Option invalide")
        continue
