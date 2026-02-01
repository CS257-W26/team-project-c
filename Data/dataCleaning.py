import pandas as pd

df = pd.read_csv("emissionsAllYears.csv")
cols_to_sum = ["Generation (kWh)", 
               "Useful Thermal Output (MMBtu)", 
               "Total Fuel Consumption (MMBtu)",
               "Fuel Consumption for Electric Generation (MMBtu)",
               "Quantity of Fuel Consumed",
               "Tons of CO2 Emissions",
               "Metric Tonnes of CO2 Emissions"
               ]
for col in cols_to_sum:
    df[col] = (
        df[col]
        .replace({r"[,\s\u00A0]": ""}, regex=True)
        .replace("", pd.NA)
        .apply(pd.to_numeric, errors="coerce")  
    )
state_year_summary = (
    df
    .groupby(["State", "Year"], as_index=False)[cols_to_sum]
    .sum(min_count=1)
)
state_year_summary.to_csv("state_year_power_summary.csv", index=False)