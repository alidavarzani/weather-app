CREATE TABLE IF NOT EXISTS weather_data (
    id SERIAL PRIMARY KEY,
    city VARCHAR(100) NOT NULL,
    temperature FLOAT NOT NULL,
    feels_like FLOAT NOT NULL,  -- Real feel temperature
    wind_speed FLOAT NOT NULL,
    wind_deg FLOAT NOT NULL,    -- Wind direction in degrees
    humidity FLOAT NOT NULL,
    weather_condition VARCHAR(50) NOT NULL,  -- Weather condition (e.g., Sunny, Rain)
    weather_description VARCHAR(100) NOT NULL,  -- Detailed description
    timestamp TIMESTAMP NOT NULL
);
