def transform(foots,type):
    int_foot=int(foots)
    if type == "inch":
        inch=int_foot*12
        return f"Result:{int_foot} foots = {inch} inches"
    elif type == "yard":
        yard=int_foot/3
        return f"Result:{int_foot} foots = {yard} yards"
    elif type == "mile":
        mile=int_foot/5280
        return f"Result:{int_foot} foots = {mile} miles"
    else:
        return "type error"

foots=input("How many foots:\n")
type=input("Choose type:\ninch\nyard\nmile\n")
tranformation=transform(foots=foots,type=type)
print(tranformation)