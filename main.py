from atm import ATM

def main():

    actions = set(["1", "2", "3"])
    atm = ATM()

    print("Hello, welcome to Bear Robotics Bank! Please insert your bank card: ")
    while True:
        card_num = input("Enter your card number: ")
        if atm.verify_card_num(card_num):
            while True:
                card_pin = input("Enter your card PIN: ")
                if atm.verify_card_pin(card_num, card_pin):
                    break
                else:
                    print("Sorry, your PIN number is incorrect, try again.")
            break
        else: 
            print("Sorry, your card number is incorrect, try again.")

    print("Your card has been successfully inserted.")
    atm.insert_card(card_num)

    # select account
    print("You may now select an account from below:\n")
    accounts = atm.get_accounts()
    for account in accounts:
        acc_num = account.get_acc_num()
        print("    - " + str(acc_num) + "\n")

    while True:
        selected_acc_num = input("Please type in the account number of the account you wish to interact with: ")
        if atm.verify_account(selected_acc_num):
            break
        else:
            print("Sorry, this account number does not exist, try again")
    print("You have selected account " + selected_acc_num)
    atm.select_account(selected_acc_num)

    print("Please select an action from below: \n")
    print("    1. See Balance\n")
    print("    2. Deposit\n")
    print("    3. Withdraw\n")

    while True:
        action_option = input("Type the number of the action you wish to perform: ")
        if action_option not in actions:
            print("That is not a valid action. Try again.")
        else:

            if action_option == "1":
                print("Account " + selected_acc_num + " balance: $" + str(atm.get_selected_account().get_balance()) + "\n")
                key = input("Press q to quit or enter to select another action: ")

            elif action_option == "2":
                print("Account " + selected_acc_num + " balance: $" + str(atm.get_selected_account().get_balance()) + "\n")
                deposit_amt = input("Deposit amount: $")
                while True:
                    try:
                        deposit_amt_int = int(deposit_amt)
                        atm.get_selected_account().deposit(deposit_amt_int)
                        print("You have deposited $" + deposit_amt + "\n")
                        print("Account " + selected_acc_num + " new balance: $" + str(atm.get_selected_account().get_balance()) + "\n")
                        key = input("Press q to quit or enter to select another action: ")
                        break
                    except:
                        deposit_amt = input("ERROR: Please enter a number to deposit: $")
                        
            elif action_option == "3":
                print("Account " + selected_acc_num + " balance: $" + str(atm.get_selected_account().get_balance()) + "\n")
                withdraw_amt = input("Withdraw amount: $")
                while True:
                    try:
                        withdraw_amt_int = int(withdraw_amt)
                        if atm.get_selected_account().withdraw(withdraw_amt_int):
                            print("You have withdrawn $" + withdraw_amt + "\n")
                            print("Account " + selected_acc_num + " new balance: $" + str(atm.get_selected_account().get_balance()) + "\n")
                            key = input("Press q to quit or enter to select another action: ")

                        else:
                            print("ERROR: Balance too low" + "\n")
                            print("Account " + selected_acc_num + " balance: $" + str(atm.get_selected_account().get_balance()) + "\n")
                            key = input("Press q to quit or enter to select another action: ")
                        break
                    except:
                        withdraw_amt = input("ERROR: Please enter a number to withdraw: $")
            if key == "q":
                print("You have ended the session. Please remove your card.")
                atm.remove_card()
                break

main()      