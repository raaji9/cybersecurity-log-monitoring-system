-- Snowflake Schema
CREATE TABLE dim_departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(50)
);

CREATE TABLE dim_users (
    user_id INT PRIMARY KEY,
    username VARCHAR(50),
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES dim_departments(department_id)
);

CREATE TABLE dim_event_categories (
    category_id INT PRIMARY KEY,
    category_name VARCHAR(50)
);

CREATE TABLE dim_event_types (
    event_type VARCHAR(50) PRIMARY KEY,
    description VARCHAR(255),
    category_id INT,
    FOREIGN KEY (category_id) REFERENCES dim_event_categories(category_id)
);

CREATE TABLE fact_logs (
    log_id INT PRIMARY KEY,
    user_id INT,
    event_time TIMESTAMP,
    event_type VARCHAR(50),
    severity VARCHAR(20),
    source_ip VARCHAR(50),
    destination_ip VARCHAR(50),
    FOREIGN KEY (user_id) REFERENCES dim_users(user_id),
    FOREIGN KEY (event_type) REFERENCES dim_event_types(event_type)
);
