-- Create databse t_shirts_store
CREATE DATABASE t_shirts_store
USE t_shirts_store

-- Create the t_shirts table
CREATE TABLE t_shirts (
    t_shirt_id INT PRIMARY KEY,
    brand VARCHAR(50) CHECK (brand IN ('Van Huesen', 'Levi', 'Nike', 'Adidas')) NOT NULL,
    color VARCHAR(50) CHECK (color IN ('Red', 'Blue', 'Black', 'White')) NOT NULL,
    size VARCHAR(2) CHECK (size IN ('XS', 'S', 'M', 'L', 'XL')) NOT NULL,
    price INT CHECK (price BETWEEN 10 AND 50),
    stock_quantity INT NOT NULL,
    CONSTRAINT brand_color_size UNIQUE (brand, color, size)
);

-- Create the discounts table
CREATE TABLE discounts (
    discount_id INT IDENTITY(1,1) PRIMARY KEY,
    t_shirt_id INT FOREIGN KEY REFERENCES t_shirts(t_shirt_id),
    pct_discount DECIMAL(5,2) CHECK (pct_discount BETWEEN 0 AND 100)
);

-- Create a stored procedure to populate the t_shirts table
CREATE PROCEDURE PopulateTShirts
AS
BEGIN
    DECLARE @counter INT = 0;
	DECLARE @t_shirt_id INT = 1;
    DECLARE @max_records INT = 80;
    DECLARE @brand VARCHAR(50);
    DECLARE @color VARCHAR(50);
    DECLARE @size VARCHAR(2);
    DECLARE @price INT;
    DECLARE @stock INT;

    -- Seed the random number generator
    SET @counter = 0;
	SET @t_shirt_id = 1;
    SET @max_records = 80;
    SET @brand = '';
    SET @color = '';
    SET @size = '';
    SET @price = 0;
    SET @stock = 0;

    WHILE @counter < @max_records
    BEGIN
        -- Generate random values
        SET @brand = CASE FLOOR(1 + RAND() * 4)
                        WHEN 1 THEN 'Van Huesen'
                        WHEN 2 THEN 'Levi'
                        WHEN 3 THEN 'Nike'
                        WHEN 4 THEN 'Adidas'
                     END;

        SET @color = CASE FLOOR(1 + RAND() * 4)
                        WHEN 1 THEN 'Red'
                        WHEN 2 THEN 'Blue'
                        WHEN 3 THEN 'Black'
                        WHEN 4 THEN 'White'
                     END;

        SET @size = CASE FLOOR(1 + RAND() * 5)
                        WHEN 1 THEN 'XS'
                        WHEN 2 THEN 'S'
                        WHEN 3 THEN 'M'
                        WHEN 4 THEN 'L'
                        WHEN 5 THEN 'XL'
                     END;

        SET @price = CAST(10 + RAND() * 41 AS INT);
        SET @stock = CAST(10 + RAND() * 91 AS INT);

        -- Attempt to insert a new record
        -- Duplicate brand, color, size combinations will be ignored due to the unique constraint
        BEGIN TRY
            INSERT INTO t_shirts (t_shirt_id, brand, color, size, price, stock_quantity)
            VALUES (@t_shirt_id, @brand, @color, @size, @price, @stock);
            SET @counter = @counter + 1;
			SET @t_shirt_id = @t_shirt_id + 1;

        END TRY
        BEGIN CATCH
            -- Handle duplicate key error
        END CATCH;
    END;
END;

-- Call the stored procedure to populate the t_shirts table
EXEC PopulateTShirts;

-- Insert at least 10 records into the discounts table
INSERT INTO discounts (t_shirt_id, pct_discount)
VALUES
(1, 10.00),
(2, 15.00),
(3, 20.00),
(4, 5.00),
(5, 25.00),
(6, 10.00),
(7, 30.00),
(8, 35.00),
(9, 40.00),
(10, 45.00),
(11, 50.00),
(12, 55.00),
(13, 60.00),
(14, 65.00),
(15, 70.00),
(16, 75.00),
(17, 80.00),
(18, 85.00),
(19, 17.00),
(20, 38.00);
