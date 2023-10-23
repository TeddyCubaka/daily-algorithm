# Une calculatrice simple en Python
# Bing, 2023

# Définir les fonctions pour les opérations arithmétiques
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

# Afficher le menu des options
print("Choisissez une opération:")
print("1. Addition")
print("2. Soustraction")
print("3. Multiplication")
print("4. Division")

# Demander à l'utilisateur de choisir une option
choice = input("Entrez votre choix (1/2/3/4): ")

# Demander à l'utilisateur d'entrer deux nombres
num1 = float(input("Entrez le premier nombre: "))
num2 = float(input("Entrez le deuxième nombre: "))

# Effectuer l'opération choisie et afficher le résultat
if choice == '1':
    print(num1, "+", num2, "=", add(num1, num2))
elif choice == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))
elif choice == '3':
    print(num1, "*", num2, "=", multiply(num1, num2))
elif choice == '4':
    print(num1, "/", num2, "=", divide(num1, num2))
else:
    print("Option invalide")