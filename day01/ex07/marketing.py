from pydoc import cli
import sys


def call_center(clients, recipients):
    return [x for x in set(clients) - set(recipients)]


def potential_clients(clients, participants):
    return [x for x in set(participants) - set(clients)]


def loyalty_program(clients, participants):
    return [x for x in set(clients) - set(participants)]


def marketing():
    clients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com', 'john@snow.is', 
                'bill_gates@live.com', 'mark@facebook.com', 'elon@paypal.com', 'jessica@gmail.com']
    participants = ['walter@heisenberg.com', 'vasily@mail.ru', 'pinkman@yo.org', 'jessica@gmail.com', 
                'elon@paypal.com', 'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com']
    recipients = ['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is']
    if len(sys.argv) != 2:
        raise Exception('The number of arguments is not equal to 2')
    tasks = ['call_center', 'potential_clients', 'loyalty_program']
    if sys.argv[1] == tasks[0]:
        print(call_center(clients, recipients))
    elif sys.argv[1] == tasks[1]:
        print(potential_clients(clients, participants))
    elif sys.argv[1] == tasks[2]:
        print(loyalty_program(clients, participants))
    else:
        raise Exception('Wrong task')



if __name__ == '__main__':
    marketing()
