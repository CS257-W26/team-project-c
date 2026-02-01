"""A bunch of large constants used for tests"""

valid_table = """State                           | MN   | WY   | US         
Year                            | 1990 | 2005 | 2026       
--------------------------------|------|------|------------
Total Fuel Consumption for      |
Electric Generation      (MMBtu)| 100  | NULL | NULL       
CO2 Emmissions            (Tons)| NULL | NULL | 50,000,000 
total Revenue              ($1K)| NULL | 1.20 | NULL"""

valid_ca_table = """State                           | CA             
Year                            | 2024           
--------------------------------|----------------
Generation                 (kWh)| 97,548,285,658 
Useful Thermal Output    (MMBtu)| 58,032,798     
Total Fuel Consumption   (MMBtu)| 767,934,359    
Total Fuel Consumption for      |
Electric Generation      (MMBtu)| 681,143,617    
CO2 Emmissions            (Tons)| 43,645,341     
CO2 Emmissions     (Metric Tons)| 39,594,436     
Residential Revenue        ($1K)| 27,443,697     
Residential Sales          (MWh)| 85,850,540     
Residential Customers           | 14,217,179.08  
Residential Price    (cents/kWh)| 32.07          
Commercial Revenue         ($1K)| 29,399,925     
Commercial Sales           (MWh)| 115,125,594    
Commercial Customers            | 1,777,301.08   
Commercial Price     (cents/kWh)| 25.32          
Industrial Revenue         ($1K)| 9,477,809      
Industrial Sales           (MWh)| 44,025,910     
Industrial Customers            | 146,325.75     
Industrial Price     (cents/kWh)| 21.19          
Transportation Revenue     ($1K)| 120,097        
Transportation Sales       (MWh)| 715,099        
Transportation Customers        | 12.58          
Transportation Price (cents/kWh)| 16.79          
total Revenue              ($1K)| 66,441,529     
total Sales                (MWh)| 245,717,144    
total Customers                 | 16,140,818.50  
total Price          (cents/kWh)| 26.82"""

valid_ga_e_table = """State                           | GA             
Year                            | 2024           
--------------------------------|----------------
Generation                 (kWh)| 75,096,813,674 
Useful Thermal Output    (MMBtu)| 26,949,036     
Total Fuel Consumption   (MMBtu)| 649,945,364    
Total Fuel Consumption for      |
Electric Generation      (MMBtu)| 612,469,605    
CO2 Emmissions            (Tons)| 47,088,360     
CO2 Emmissions     (Metric Tons)| 42,717,893"""

valid_wa_nm_table = """State                           | WA             | NM             
Year                            | 2024           | 2024           
--------------------------------|----------------|----------------
Generation                 (kWh)| 21,119,893,670 | 20,106,485,132 
Useful Thermal Output    (MMBtu)| 10,095,169     | 526,233        
Total Fuel Consumption   (MMBtu)| 190,433,710    | 189,048,426    
Total Fuel Consumption for      |
Electric Generation      (MMBtu)| 174,834,966    | 188,281,551    
CO2 Emmissions            (Tons)| 12,798,157     | 14,773,195     
CO2 Emmissions     (Metric Tons)| 11,610,306     | 13,402,031     
Residential Revenue        ($1K)| 4,595,905      | 1,043,284      
Residential Sales          (MWh)| 38,626,766     | 7,347,618      
Residential Customers           | 3,368,974.67   | 936,097.08     
Residential Price    (cents/kWh)| 11.98          | 14.14          
Commercial Revenue         ($1K)| 3,307,357      | 1,011,139      
Commercial Sales           (MWh)| 33,101,748     | 9,592,788      
Commercial Customers            | 405,310.42     | 148,101.75     
Commercial Price     (cents/kWh)| 10.02          | 10.49          
Industrial Revenue         ($1K)| 1,200,157      | 725,316        
Industrial Sales           (MWh)| 18,159,320     | 13,355,947     
Industrial Customers            | 26,383.75      | 9,256.08       
Industrial Price     (cents/kWh)| 6.61           | 5.43           
Transportation Revenue     ($1K)| 10,922         | 0              
Transportation Sales       (MWh)| 93,797         | 0              
Transportation Customers        | 5              | 0              
Transportation Price (cents/kWh)| 11.65          | 0              
total Revenue              ($1K)| 9,114,338      | 2,779,737      
total Sales                (MWh)| 89,981,630     | 30,296,355     
total Customers                 | 3,800,673.83   | 1,093,454.92   
total Price          (cents/kWh)| 10.12          | 9.14"""

valid_nd_sd_table = """State                           | ND             | SD            
Year                            | 2024           | 2024          
--------------------------------|----------------|---------------
Generation                 (kWh)| 25,668,864,763 | 3,839,359,578 
Useful Thermal Output    (MMBtu)| 7,839,786      | 1,468,469     
Total Fuel Consumption   (MMBtu)| 298,600,042    | 41,735,122    
Total Fuel Consumption for      |
Electric Generation      (MMBtu)| 281,475,282    | 37,167,960    
CO2 Emmissions            (Tons)| 30,374,329     | 3,325,000     
CO2 Emmissions     (Metric Tons)| 27,555,161     | 3,016,390     
Residential Revenue        ($1K)| 565,148        | 664,939       
Residential Sales          (MWh)| 4,910,755      | 5,170,067     
Residential Customers           | 397,836.33     | 433,542.67    
Residential Price    (cents/kWh)| 11.77          | 12.97         
Commercial Revenue         ($1K)| 812,799        | 539,258       
Commercial Sales           (MWh)| 11,309,335     | 5,111,480     
Commercial Customers            | 77,193.17      | 78,290.17     
Commercial Price     (cents/kWh)| 7.19           | 10.54         
Industrial Revenue         ($1K)| 981,890        | 277,780       
Industrial Sales           (MWh)| 13,549,610     | 3,355,657     
Industrial Customers            | 10,863.50      | 4,313.58      
Industrial Price     (cents/kWh)| 7.25           | 8.27          
Transportation Revenue     ($1K)| 0              | 0             
Transportation Sales       (MWh)| 0              | 0             
Transportation Customers        | 0              | 0             
Transportation Price (cents/kWh)| 0              | 0             
total Revenue              ($1K)| 2,359,831      | 1,481,978     
total Sales                (MWh)| 29,769,699     | 13,637,205    
total Customers                 | 485,893        | 516,146.42    
total Price          (cents/kWh)| 7.93           | 10.87"""


valid_mn_table = """State                           | MN             
Year                            | 2024           
--------------------------------|----------------
Generation                 (kWh)| 27,814,120,731 
Useful Thermal Output    (MMBtu)| 17,095,959     
Total Fuel Consumption   (MMBtu)| 277,129,619    
Total Fuel Consumption for      |
Electric Generation      (MMBtu)| 251,190,061    
CO2 Emmissions            (Tons)| 22,476,702     
CO2 Emmissions     (Metric Tons)| 20,390,541     
Residential Revenue        ($1K)| 3,408,954      
Residential Sales          (MWh)| 22,062,758     
Residential Customers           | 2,581,181.67   
Residential Price    (cents/kWh)| 15.49          
Commercial Revenue         ($1K)| 2,729,308      
Commercial Sales           (MWh)| 22,468,439     
Commercial Customers            | 308,457.33     
Commercial Price     (cents/kWh)| 12.13          
Industrial Revenue         ($1K)| 1,831,204      
Industrial Sales           (MWh)| 20,015,580     
Industrial Customers            | 9,404.58       
Industrial Price     (cents/kWh)| 9.14           
Transportation Revenue     ($1K)| 1,949          
Transportation Sales       (MWh)| 15,331         
Transportation Customers        | 1              
Transportation Price (cents/kWh)| 12.88          
total Revenue              ($1K)| 7,971,414      
total Sales                (MWh)| 64,562,108     
total Customers                 | 2,899,044.58   
total Price          (cents/kWh)| 12.33"""

valid_us_price_table = """State                           | US               
Year                            | 2024             
--------------------------------|------------------
Residential Revenue        ($1K)| 244,367,406      
Residential Sales          (MWh)| 1,482,873,606    
Residential Customers           | 7,300,347,727.25 
Residential Price    (cents/kWh)| 17.13            
Commercial Revenue         ($1K)| 185,043,252      
Commercial Sales           (MWh)| 1,450,941,245    
Commercial Customers            | 993,518,998.00   
Commercial Price     (cents/kWh)| 13.31            
Industrial Revenue         ($1K)| 84,094,819       
Industrial Sales           (MWh)| 1,034,584,212    
Industrial Customers            | 56,913,811.25    
Industrial Price     (cents/kWh)| 9.76             
Transportation Revenue     ($1K)| 890,326          
Transportation Sales       (MWh)| 6,982,850        
Transportation Customers        | 4,109.75         
Transportation Price (cents/kWh)| 6.67             
total Revenue              ($1K)| 514,395,778      
total Sales                (MWh)| 3,975,381,862    
total Customers                 | 8,350,784,646.25 
total Price          (cents/kWh)| 13.73"""
