# Practice session on Functions

-- CREATE DEFINER=`root`@`localhost` FUNCTION `product_price`(price float) RETURNS varchar(32) CHARSET utf8mb4
--     DETERMINISTIC
-- begin

-- 	if price > 50000 then
-- 		return "Expensive";
-- 	else
-- 		return "Affortable";
-- 	end if;

-- end

use product_db;

select * from Products;

select product_price(Price) from Products;

# Task - 2
-- create function product_tax(category varchar(32))
-- returns varchar(10)
-- deterministic
-- begin

-- 	if category = "Electronics" then
-- 		return "Tax 18%";
-- 	elseif category = "Furniture" then
-- 		return "Tax 12%";
-- 	elseif category = "Furniture" then
-- 		return "Tax 5%";
-- 	elseif category = "Grocery" then
-- 		return "o";
-- 	else
-- 		return "No tax";
--     end if;

-- end

select product_tax(Category) from Products;

# Task - 3 

-- CREATE DEFINER=`root`@`localhost` FUNCTION `discount_price`(price float, category varchar(32)) RETURNS float
--     DETERMINISTIC
-- begin

-- 	if category = "Electronics" then
-- 		return (price * 20)/100;
-- 	elseif category = "Furniture" then
-- 		return (price * 15)/100;
-- 	elseif category = "Fashion" then
-- 		return (price * 10)/100;
-- 	elseif category = "Grocery" then
-- 		return (price * 5)/100;
-- 	else
-- 		return 0;
-- 	end if;

-- end

select discount_price(Price,Category) from Products;

# Task - 4

-- create function cal_selling_price(price float, category varchar(32))
-- returns float
-- deterministic
-- begin

-- if category = "Electronics" then
-- 		return price-price*0.25;
-- 	elseif category = "Furniture" then
-- 		return price-price*0.2;
-- 	elseif category = "Fashion" then
-- 		return price+price*0.3;
-- 	elseif category = "Grocery" then
-- 		return price-price*0.1;
-- 	else
-- 		return price-price*0.05;
-- 	end if;

-- end

select cal_selling_price(Price, Category) from Products;