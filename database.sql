--db_name = pet_hotel

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