CREATE TABLE users (
  id INTEGER PRIMARY KEY,
  username VARCHAR(50) UNIQUE,
  password VARCHAR(50),
  role VARCHAR(20)
);
