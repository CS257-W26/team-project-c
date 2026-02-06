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
  metricTonnesco2Emissions BIGINT,
);