#local ui 
import time
import cashier_logic

def test() -> None:
    '''
    line = cashier_logic.CustomerState(4, cashier_logic.MEDIUM)
    for customer in line.line(): 
        print(customer.due(), customer.given(), customer.satisfaction())
    '''

    running = True
    score = 0
    timer = 0
    while running:
        line = cashier_logic.CustomerState(5, cashier_logic.HARD)

        for customer in line.line():
            print(f'Amount Given: {customer.given()}')
            print(f'Amount Due  : {customer.due()}')

            print(f'Correct: {customer.correct_change()}')
            start = time.time()
            answer = input('Enter Change: ')
            end = time.time()
            
            timer += (end - start)

            
            if line.timer() < timer:
                break

            if answer == ' ':
                break
            if float(answer) == customer.correct_change():
                score += 100
            else:
                score -= 100
        running = False
    
    print(f'TOTAL: {score}')


if __name__ == '__main__':
    test()

