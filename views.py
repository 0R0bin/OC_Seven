def ask_budget(default_budget):
    """
    Ask user input to chose budget
    """
    print('Souhaitez-vous utiliser un budget personnalisé ?')
    b_choice = input('Répondre par (y / oui / yes) pour le personnaliser ou autre pour garder 500€ : ')

    if b_choice.lower() in ['y', 'yes', 'oui']:
        budget = input('Merci d\'entrer le budget : ')
        # Vérification du budget en INT
        try:
            budget = int(budget)
        except ValueError:
            print('Merci d\'indiquer votre budget au format INT\n')
            return ask_budget(default_budget)
        print(f'\nBudget de {budget}€ choisi\n')
        return int(budget)

    print('\nBudget par défaut choisi (500€)')
    return default_budget


def ask_dset():
    """
    Demander à l'utilisateur de choisir un jeu de données
    """
    print('\nMerci de choisir un jeu de données et de rentrer son nom sans extension et sans tenir compte du dossier')
    print('Exemple d\'input possible :\n - actions \n - dataset1')
    dset_choice = input('Nom du jeu de données : ')

    filename = f'dataset_csv/{dset_choice}.csv'

    print(f'\nFichier choisi : {filename}')
    b_continue = input('Confirmez-vous ce choix ? (y ou n) ')

    if b_continue.lower() in ['y', 'yes', 'oui']:
        try:
            with open(filename, 'r'):
                print('\nChoix validé, lecture du fichier en cours\n')
                return filename
        except FileNotFoundError:
            print(f"Erreur : Le fichier '{filename}' n'existe pas")
            return ask_dset()

    return ask_dset()


def csv_ok():
    """Print CSV OK, launch knapsack"""
    return '\nRécupération des données du fichier terminé, lancement de l\'algorithme...'


def report(best_stock, actual_time, started_time):
    """
    Affichage algo terminé avec :
     - Temps passé
     - Coût
     - Gains
    """
    print('======================================================================')
    print(f'Algorithme Knapsack terminé en {actual_time - started_time} secondes')
    print('======================================================================\n')
    print(f"\nMeilleurs investissements possibles ({len(best_stock)} stock) :\n")
    print('(Col1) Nom |(Col2) Prix |(Col3) Profit')

    total_price = 0
    total_profit = 0

    for stock in best_stock:
        print(f'- {stock[0]} | {stock[1] / 100} € | +{stock[3]} €')
        total_price += stock[1]
        total_profit += stock[3]

    print(f'\nCoût total : {total_price / 100}€')
    print(f'Gains : {total_profit}€\n')