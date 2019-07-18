--db_name = pet_hotel

--DROP TABLE "owner";

SELECT * FROM "owner";
SELECT * FROM "pet";

CREATE TABLE "owner" (
"id" SERIAL PRIMARY KEY,
"name" VARCHAR(80),
"address" VARCHAR(120),
"phone" VARCHAR(20)
);

CREATE TABLE "pet" (
"id" SERIAL PRIMARY KEY,
"name" VARCHAR(80),
"breed" VARCHAR(80),
"color" VARCHAR(80),
"owner_id" INT REFERENCES "owner",
"check_in" BOOL,
"age" INT,
"image" VARCHAR(500)
);

CREATE TABLE "visit" (
"id" SERIAL PRIMARY KEY,
"pet_id" INT REFERENCES "pet",
"checkin_date" DATE DEFAULT CURRENT_DATE,
"checkout_date" DATE
);

INSERT INTO "owner" (name, address, phone) VALUES 
('Sue', '123 Something rd', '5551234567'),
('Jenny Jenny', '12 Springfield Ln', '5558675309'),
('Jack', '201 Melloncamp St', '1234567890'),
('Diane', '402 Melloncamp St', '1098765432');

INSERT INTO "pet" (name, breed, color, owner_id, check_in, age) VALUES
('Charlie', 'shih-tzu', 'black', 1, false, 3),
('Thorin', 'rabbit', 'white', 2, false, 2),
('Gatsby', 'cat', 'white', 3, false, 7),
('Angus', 'scottie dog', 'black', 4, false, 6),
('Bear', 'dog', 'black', 4, false, 10);