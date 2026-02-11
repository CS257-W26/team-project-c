DROP TABLE IF EXISTS emissions;
CREATE TABLE emissions ( --Create the table--
  plantName TEXT,
  state TEXT,
  fuelGroup TEXT,
  generation BIGINT,
  usefullThermalOutput BIGINT,
  totalFuelConsumption BIGINT,
  fuelConsumptionElectricGeneration BIGINT,
  fuelConsumptionUsefulThermalOutput BIGINT,
  quantityOfFuelConsumed BIGINT,
  fuelUnits TEXT,
  tonsco2Emissions FLOAT,
  metricTonnesco2Emissions FLOAT,
  year INTEGER
);

DROP TABLE IF EXISTS sales_revenue;
CREATE TABLE sales_revenue ( --Create the table--
  year INTEGER,
  month INTEGER,
  state TEXT,
  residentialRevenue FLOAT,
  residentialSales FLOAT,
  residentialCustomers FLOAT,
  residentialPrice FLOAT,
  commercialRevenue FLOAT,
  commercialSales FLOAT,
  commercialCustomers FLOAT,
  commercialPrice FLOAT,
  industrialRevenue FLOAT,
  industrialSales FLOAT,
  industrialCustomers FLOAT,
  industrialPrice FLOAT,
  transportationRevenue FLOAT,
  transportationSales FLOAT,
  transportationCustomers FLOAT,
  transportationPrice FLOAT,
  totalRevenue FLOAT,
  totalSales FLOAT,
  totalCustomers FLOAT,
  totalPrice FLOAT
);