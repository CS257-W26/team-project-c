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
  tonsco2Emissions BIGINT,
  metricTonnesco2Emissions BIGINT
);

DROP TABLE IF EXISTS sales_revenue;
CREATE TABLE sales_revenue ( --Create the table--
  year INTEGER,
  month INTEGER,
  state TEXT,
  residentialRevenue BIGINT,
  residentialSales BIGINT,
  residentialCustomers BIGINT,
  residentialPrice BIGINT,
  commercialRevenue BIGINT,
  commercialSales BIGINT,
  commercialCustomers BIGINT,
  commercialPrice BIGINT,
  industrialRevenue BIGINT,
  industrialSales BIGINT,
  industrialCustomers BIGINT,
  industrialPrice BIGINT,
  transportationRevenue BIGINT,
  transportationSales BIGINT,
  transportationCustomers BIGINT,
  transportationPrice BIGINT,
  totalRevenue BIGINT,
  totalales BIGINT,
  totalCustomers BIGINT,
  totalPrice BIGINT
);