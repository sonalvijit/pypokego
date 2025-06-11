def load_assets(addr:str):
     with open(addr, 'r') as file:
          print(file)

a = load_assets('./assets')
print(a)