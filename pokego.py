from load import load_asset, random_asset_from_list

regular = load_asset("assets/colorscripts/regular/")
shiny = load_asset("assets/colorscripts/shiny/")

a = random_asset_from_list(regular)["content"]
b = random_asset_from_list(shiny)["content"]
c = random_asset_from_list(regular)
# print(a)
# print(b)
print(c["content"])
print(c["filename"])