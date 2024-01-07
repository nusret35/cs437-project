# Database Tables

## Users Table

```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) UNIQUE,
    password VARCHAR(255),
    role VARCHAR(255) DEFAULT 'user'
);
```
## Comments Table

```sql
CREATE TABLE comments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    news_link VARCHAR(255) NOT NULL,
    FOREIGN KEY (username) REFERENCES users(username)
);


```
## Coins Table

```sql
CREATE TABLE coins (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), url VARCHAR(255));

```
## TrackAd Table

```sql
CREATE TABLE TRACKAD (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user VARCHAR(255),
    date DATETIME,
    url VARCHAR(255)
);

```
## Economists Table

```sql
CREATE TABLE economists (id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(255),image_url VARCHAR(255),short_info TEXT);
```

