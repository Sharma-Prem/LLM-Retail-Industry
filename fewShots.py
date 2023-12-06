fewShots = [
    {
        "Question": "What are the unique brands in the store?",
        "SQLQuery": "select distinct brand from t_shirts",
        "SQLResult": "Result of the SQL query",
        "Answer": "Adidas, Levi, Nike, Van Huesen"
    },
    {
        "Question": "What is the total stock quantity for each brand?",
        "SQLQuery": "select brand, sum(stock_quantity) as total_stock_quantity from t_shirts group by brand",
        "SQLResult": "Result of the SQL query",
        "Answer": "('Adidas', 1246), ('Levi', 1307), ('Nike', 1114), ('Van Huesen', 949)"
    },
    {
        "Question": "Which brand has the highest stock quantity?",
        "SQLQuery": "select TOP 1 brand, sum(stock_quantity) as total_stock_quantity from t_shirts group by brand order by total_stock_quantity desc",
        "SQLResult": "Result of the SQL query",
        "Answer": "Levi"
    },
    {
        "Question": "Which brand has the lowest stock quantity?",
        "SQLQuery": "select TOP 1 brand, sum(stock_quantity) as total_stock_quantity from t_shirts group by brand order by total_stock_quantity asc",
        "SQLResult": "Result of the SQL query",
        "Answer": "Van Huesen"
    },
    {
        "Question": "What are the unique colors available in the stock?",
        "SQLQuery": "select distinct color from t_shirts",
        "SQLResult": "Result of the SQL query",
        "Answer": "Black, Blue, Red, White"
    },
    {
        "Question": "How many items are available for each color?",
        "SQLQuery": "select color, sum(stock_quantity) as total_stock_quantity from t_shirts group by color",
        "SQLResult": "Result of the SQL query",
        "Answer": "('Black', 1253), ('Blue', 1238), ('Red', 1013), ('White', 1112)"
    },
    {
        "Question": "What are the unique sizes available in the stock?",
        "SQLQuery": "select distinct size from t_shirts",
        "SQLResult": "Result of the SQL query",
        "Answer": "L, M, S, XL, XS"
    },
    {
        "Question": "How many items are available for each size?",
        "SQLQuery": "select size, sum(stock_quantity) as total_stock_quantity from t_shirts group by size",
        "SQLResult": "Result of the SQL query",
        "Answer": "('L', 831), ('M', 1179), ('S', 823), ('XL', 900), ('XS', 883)"
    },
    {
        "Question": "What is the average price of the items?",
        "SQLQuery": "select avg(price) as avg_price from t_shirts",
        "SQLResult": "Result of the SQL query",
        "Answer": "26"
    },
    {
        "Question": "Which item has the highest price?",
        "SQLQuery": "select brand, color, size, price from t_shirts where price = (select max(price) from t_shirts)",
        "SQLResult": "Result of the SQL query",
        "Answer": "Levi, White, M, 50"
    },
    {
        "Question": "Which item has the lowest price?",
        "SQLQuery": "select brand, color, size, price from t_shirts where price = (select min(price) from t_shirts)",
        "SQLResult": "Result of the SQL query",
        "Answer": "('Van Huesen', 'Red', 'L', 10), ('Levi', 'Blue', 'M', 10), ('Nike', 'Blue', 'M', 10)"
    },
    {
        "Question": "What is the overall stock quantity in the store?",
        "SQLQuery": "select sum(stock_quantity) as total_stock_quantity from t_shirts",
        "SQLResult": "Result of the SQL query",
        "Answer": "4616"
    },
    {
        "Question": "What is the average stock quantity for each brand?",
        "SQLQuery": "select brand, avg(stock_quantity) as avg_stock_quantity from t_shirts group by brand",
        "SQLResult": "Result of the SQL query",
        "Answer": "('Adidas', 62), ('Levi', 65), ('Nike', 55), ('Van Huesen', 47)"
    },
    {
        "Question": "Which item has the highest price-to-stock quantity ratio?",
        "SQLQuery": "select TOP 1 t_shirt_id, brand, color, size, price, stock_quantity,price * 1.0 / stock_quantity AS price_to_stock_ratio FROM t_shirts ORDER BY price_to_stock_ratio desc",
        "SQLResult": "Result of the SQL query",
        "Answer": "23, Nike, White, XL, 42, 10, 4.2"
    },
    {
        'Question': "How many t-shirts do we have left for Nike in XS and white color?",
        'SQLQuery': "select sum(stock_quantity) from t_shirts where brand = 'Nike' and color = 'White and size = 'XS'",
        'SQLResult': "Result of the SQL query",
        'Answer': "42"
    },
    {
        'Question': "How much is the price of the inventory for only small size t-shirts?",
        'SQLQuery': "select sum(price*stock_quantity) as total_price from t_shirts where size = 'S'",
        'SQLResult': "Result of the SQL query",
        'Answer': "26016"
    },
    {
        'Question': "If we have to sell all the Levi T-shirt today with discounts applied. How much revenue our store will generate (post discounts)?",
        'SQLQuery': "select sum(a.total_amount*((100-COALESCE(discounts.pct_discount,0))/100)) as total_revenue from (select sum(price*stock_quantity) as total_amount, t_shirt_id from t_shirts where brand = 'Levi' group by t_shirt_id) a left join discounts on a.t_shirt_id = discounts.t_shirt_id",
        'SQLResult': "Result of the SQL query",
        'Answer': "36393.8"
    },
    {
        'Question': "If we have to sell all the Levi T-shirt today. How much revenue our store will generate?",
        'SQLQuery': "Select sum(price*stock_quantity) from t_shirts where brand = 'Levi'",
        'SQLResult': "Result of the SQL query",
        'Answer': "42803"
    },
    {
        'Question': "How many white color Levi T-shirt we have available?",
        'SQLQuery': "select sum(stock_quantity) from t_shirts where brand = 'Levi' and color = 'White'",
        'SQLResult': "Result of the SQL query",
        'Answer': "333"
    },
    {
        'Question': "How many t-shirts have associated discounts?",
        'SQLQuery': "SELECT sum(t.stock_quantity) AS NumberOfTShirtsWithDiscount FROM t_shirts t JOIN discounts d ON t.t_shirt_id = d.t_shirt_id",
        'SQLResult': "Result of the SQL query",
        'Answer': "1152"
    },
    {
        'Question': "What is the average discount percentage?",
        'SQLQuery': "select avg(pct_discount) as avg_discount from discounts",
        'SQLResult': "Result of the SQL query",
        'Answer': "41.5"
    },
    {
        'Question': "Which t-shirt has the highest discount?",
        'SQLQuery': "SELECT t.brand, t.color, t.size, d.pct_discount FROM t_shirts t JOIN discounts d ON t.t_shirt_id = d.t_shirt_id where d.pct_discount = (select max(pct_discount) from discounts)",
        'SQLResult': "Result of the SQL query",
        'Answer': "Nike, White, M, 85.00"
    },
    {
        "Question": "What is the brand-color-size combination that has the highest average discount percentage?",
        "SQLQuery": """WITH BrandColorSizeDiscount AS (
                        SELECT
                            t.brand,
                            t.color,
                            t.size,
                            AVG(d.pct_discount) AS AvgDiscountPercentage
                        FROM
                            t_shirts t
                        JOIN
                            discounts d ON t.t_shirt_id = d.t_shirt_id
                        GROUP BY
                            t.brand, t.color, t.size
                    )

                    SELECT TOP 1
                        brand,
                        color,
                        size,
                        AvgDiscountPercentage
                    FROM
                        BrandColorSizeDiscount
                    ORDER BY
                        AvgDiscountPercentage DESC""",
        "SQLResult": "Result of the SQL query",
        "Answer": "Nike, White, M"
    },
    {
        'Question': "What is the total value of the current stock, considering both original prices and applied discounts?",
        'SQLQuery': "SELECT SUM(t.price * t.stock_quantity * (1 - ISNULL(d.pct_discount, 0) / 100)) AS TotalStockValue FROM t_shirts t LEFT JOIN discounts d ON t.t_shirt_id = d.t_shirt_id",
        'SQLResult': "Result of the SQL query",
        'Answer': "485"
    },
    {
        'Question': "Is there a correlation between the size of a t-shirt and the average discount percentage applied?",
        'SQLQuery': """"WITH SizeDiscountAnalysis AS (
                            SELECT
                                t.size,
                                AVG(ISNULL(d.pct_discount, 0)) AS AvgDiscountPercentage
                            FROM
                                t_shirts t
                            LEFT JOIN
                                discounts d ON t.t_shirt_id = d.t_shirt_id
                            GROUP BY
                                t.size
                        )

                        SELECT
                            size,
                            AvgDiscountPercentage
                        FROM
                            SizeDiscountAnalysis
                        ORDER BY
                            size""",
        'SQLResult': "Result of the SQL query",
        'Answer': "('L', Decimal('0.625000')), ('M', Decimal('12.187500')), ('S', Decimal('10.125000')), ('XL', Decimal('11.562500')), ('XS', Decimal('17.375000'))"
    }
]
