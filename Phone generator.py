from onlinesimru import GetFree, GetRent, GetProxy, GetUser, GetNumbers

def main():
    client = GetUser('3a29bfc6ce6d3520238d55319fdccad4')
    balance = client.balance()
    print(balance)

main()