import pandas as pd

df = pd.read_csv("conv.example", sep=" - ", dtype={"hard":str, "easy":str}, engine="python")

df["hard_regex"] = "/\\b" + df["hard"] + "\\b/gi"
df["escaped_easy"] = "\"" + df["easy"] + "\""
df["easy_regex"] = "/\\b" + df["easy"] + "\\b/gi"
df["escaped_hard"] = "\"" + df["hard"] + "\""

with open("regex_rules.js", mode="w+") as f:
    print("function get_formatting_rules(direction){", file=f)
    print ("if (direction == \"to\")", file=f)
    print("{return[", file=f)
    for i in range(len(df)):
        print(f"[{df.hard_regex[i]}, {df.escaped_easy[i]}],", file=f)
    print("]}else { return [", file=f)
    for i in range(len(df)):
        print(f"[{df.easy_regex[i]}, {df.escaped_hard[i]}],",file=f)
    print("]}}", file=f)

