"""A bunch of large constants used for tests"""

VALID_TABLE= "State                           | MN   | WY   | US         \n"\
"Year                            | 1990 | 2005 | 2026       \n"\
"--------------------------------|------|------|------------\n"\
"Total Fuel Consumption for      |\n"\
"Electric Generation      (MMBtu)| 100  | NULL | NULL       \n"\
"CO2 Emmissions            (Tons)| NULL | NULL | 50,000,000 \n"\
"total Revenue              ($1K)| NULL | 1.20 | NULL"

VALID_CA_TABLE= """State                           | CA             
Year                            | 2024           
--------------------------------|----------------
Generation                 (kWh)| 97,548,285,658 
Useful Thermal Output    (MMBtu)| 58,032,798     
Total Fuel Consumption   (MMBtu)| 767,934,359    
Total Fuel Consumption for      |
Electric Generation      (MMBtu)| 681,143,617    
Fuel Consumption for Useful     |
Thermal Output           (MMBtu)| 86,790,735     
Quanitty of Fuel Units Consumed | 692,539,700    
CO2 Emmissions            (Tons)| 43,645,341     
CO2 Emmissions     (Metric Tons)| 39,594,436     
Residential Revenue        ($1K)| 27,443,697.50  
Residential Sales          (MWh)| 85,850,537.90  
Residential Customers           | 14,217,179.08  
Residential Price    (cents/kWh)| 32.07          
Commercial Revenue         ($1K)| 29,399,924.60  
Commercial Sales           (MWh)| 115,125,594.70 
Commercial Customers            | 1,777,301.08   
Commercial Price     (cents/kWh)| 25.32          
Industrial Revenue         ($1K)| 9,477,808.28   
Industrial Sales           (MWh)| 44,025,912.10  
Industrial Customers            | 146,325.75     
Industrial Price     (cents/kWh)| 21.19          
Transportation Revenue     ($1K)| 120,098.20     
Transportation Sales       (MWh)| 715,100.01     
Transportation Customers        | 12.58          
Transportation Price (cents/kWh)| 16.79          
total Revenue              ($1K)| 66,441,528.70  
total Sales                (MWh)| 245,717,144    
total Customers                 | 16,140,818.50  
total Price          (cents/kWh)| 26.82"""

VALID_WA_NM_TABLE= """State                           | WA             | NM             
Year                            | 2024           | 2024           
--------------------------------|----------------|----------------
Generation                 (kWh)| 21,119,893,670 | 20,106,485,132 
Useful Thermal Output    (MMBtu)| 10,095,169     | 526,233        
Total Fuel Consumption   (MMBtu)| 190,433,710    | 189,048,426    
Total Fuel Consumption for      |
Electric Generation      (MMBtu)| 174,834,966    | 188,281,551    
Fuel Consumption for Useful     |
Thermal Output           (MMBtu)| 15,598,744     | 766,876        
Quanitty of Fuel Units Consumed | 142,088,690    | 106,540,216    
CO2 Emmissions            (Tons)| 12,798,157     | 14,773,195     
CO2 Emmissions     (Metric Tons)| 11,610,306     | 13,402,031     
Residential Revenue        ($1K)| 4,595,906.32   | 1,043,282.68   
Residential Sales          (MWh)| 38,626,766.00  | 7,347,619.99   
Residential Customers           | 3,368,974.67   | 936,097.08     
Residential Price    (cents/kWh)| 11.98          | 14.14          
Commercial Revenue         ($1K)| 3,307,355.43   | 1,011,136.97   
Commercial Sales           (MWh)| 33,101,746.10  | 9,592,788.98   
Commercial Customers            | 405,310.42     | 148,101.75     
Commercial Price     (cents/kWh)| 10.02          | 10.49          
Industrial Revenue         ($1K)| 1,200,154.55   | 725,316.23     
Industrial Sales           (MWh)| 18,159,320     | 13,355,945.01  
Industrial Customers            | 26,383.75      | 9,256.08       
Industrial Price     (cents/kWh)| 6.61           | 5.43           
Transportation Revenue     ($1K)| 10,922.40      | 0              
Transportation Sales       (MWh)| 93,797.01      | 0              
Transportation Customers        | 5              | 0              
Transportation Price (cents/kWh)| 11.65          | 0              
total Revenue              ($1K)| 9,114,338.70   | 2,779,735.90   
total Sales                (MWh)| 89,981,629.10  | 30,296,354.10  
total Customers                 | 3,800,673.83   | 1,093,454.92   
total Price          (cents/kWh)| 10.12          | 9.14"""

VALID_ND_SD_TABLE= "State                           | ND             | SD            \n"\
"Year                            | 2024           | 2024          \n"\
"--------------------------------|----------------|---------------\n"\
"Generation                 (kWh)| 25,668,864,763 | 3,839,359,578 \n"\
"Useful Thermal Output    (MMBtu)| 7,839,786      | 1,468,469     \n"\
"Total Fuel Consumption   (MMBtu)| 298,600,042    | 41,735,122    \n"\
"Total Fuel Consumption for      |\n"\
"Electric Generation      (MMBtu)| 281,475,282    | 37,167,960    \n"\
"CO2 Emmissions            (Tons)| 30,374,329     | 3,325,000     \n"\
"CO2 Emmissions     (Metric Tons)| 27,555,161     | 3,016,390     \n"\
"Residential Revenue        ($1K)| 565,148        | 664,939       \n"\
"Residential Sales          (MWh)| 4,910,755      | 5,170,067     \n"\
"Residential Customers           | 397,836.33     | 433,542.67    \n"\
"Residential Price    (cents/kWh)| 11.77          | 12.97         \n"\
"Commercial Revenue         ($1K)| 812,799        | 539,258       \n"\
"Commercial Sales           (MWh)| 11,309,335     | 5,111,480     \n"\
"Commercial Customers            | 77,193.17      | 78,290.17     \n"\
"Commercial Price     (cents/kWh)| 7.19           | 10.54         \n"\
"Industrial Revenue         ($1K)| 981,890        | 277,780       \n"\
"Industrial Sales           (MWh)| 13,549,610     | 3,355,657     \n"\
"Industrial Customers            | 10,863.50      | 4,313.58      \n"\
"Industrial Price     (cents/kWh)| 7.25           | 8.27          \n"\
"Transportation Revenue     ($1K)| 0              | 0             \n"\
"Transportation Sales       (MWh)| 0              | 0             \n"\
"Transportation Customers        | 0              | 0             \n"\
"Transportation Price (cents/kWh)| 0              | 0             \n"\
"total Revenue              ($1K)| 2,359,831      | 1,481,978     \n"\
"total Sales                (MWh)| 29,769,699     | 13,637,205    \n"\
"total Customers                 | 485,893        | 516,146.42    \n"\
"total Price          (cents/kWh)| 7.93           | 10.87"


VALID_MN_TABLE= "State                           | MN             \n"\
"Year                            | 2024           \n"\
"--------------------------------|----------------\n"\
"Generation                 (kWh)| 27,814,120,731 \n"\
"Useful Thermal Output    (MMBtu)| 17,095,959     \n"\
"Total Fuel Consumption   (MMBtu)| 277,129,619    \n"\
"Total Fuel Consumption for      |\n"\
"Electric Generation      (MMBtu)| 251,190,061    \n"\
"CO2 Emmissions            (Tons)| 22,476,702     \n"\
"CO2 Emmissions     (Metric Tons)| 20,390,541     \n"\
"Residential Revenue        ($1K)| 3,408,954      \n"\
"Residential Sales          (MWh)| 22,062,758     \n"\
"Residential Customers           | 2,581,181.67   \n"\
"Residential Price    (cents/kWh)| 15.49          \n"\
"Commercial Revenue         ($1K)| 2,729,308      \n"\
"Commercial Sales           (MWh)| 22,468,439     \n"\
"Commercial Customers            | 308,457.33     \n"\
"Commercial Price     (cents/kWh)| 12.13          \n"\
"Industrial Revenue         ($1K)| 1,831,204      \n"\
"Industrial Sales           (MWh)| 20,015,580     \n"\
"Industrial Customers            | 9,404.58       \n"\
"Industrial Price     (cents/kWh)| 9.14           \n"\
"Transportation Revenue     ($1K)| 1,949          \n"\
"Transportation Sales       (MWh)| 15,331         \n"\
"Transportation Customers        | 1              \n"\
"Transportation Price (cents/kWh)| 12.88          \n"\
"total Revenue              ($1K)| 7,971,414      \n"\
"total Sales                (MWh)| 64,562,108     \n"\
"total Customers                 | 2,899,044.58   \n"\
"total Price          (cents/kWh)| 12.33"

VALID_US_PRICE_TABLE= "State                           | US               \n"\
"Year                            | 2024             \n"\
"--------------------------------|------------------\n"\
"Residential Revenue        ($1K)| 244,367,406      \n"\
"Residential Sales          (MWh)| 1,482,873,606    \n"\
"Residential Customers           | 7,300,347,727.25 \n"\
"Residential Price    (cents/kWh)| 17.13            \n"\
"Commercial Revenue         ($1K)| 185,043,252      \n"\
"Commercial Sales           (MWh)| 1,450,941,245    \n"\
"Commercial Customers            | 993,518,998.00   \n"\
"Commercial Price     (cents/kWh)| 13.31            \n"\
"Industrial Revenue         ($1K)| 84,094,819       \n"\
"Industrial Sales           (MWh)| 1,034,584,212    \n"\
"Industrial Customers            | 56,913,811.25    \n"\
"Industrial Price     (cents/kWh)| 9.76             \n"\
"Transportation Revenue     ($1K)| 890,326          \n"\
"Transportation Sales       (MWh)| 6,982,850        \n"\
"Transportation Customers        | 4,109.75         \n"\
"Transportation Price (cents/kWh)| 6.67             \n"\
"total Revenue              ($1K)| 514,395,778      \n"\
"total Sales                (MWh)| 3,975,381,862    \n"\
"total Customers                 | 8,350,784,646.25 \n"\
"total Price          (cents/kWh)| 13.73"
