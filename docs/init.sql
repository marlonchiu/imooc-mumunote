-- 创建数据库
CREATE DATABASE IF NOT EXISTS mumushouji DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- 使用数据库
USE mumushouji;

-- 创建用户表
CREATE TABLE IF NOT EXISTS user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 插入一些测试数据
INSERT INTO user (username, password, email) VALUES
('test1', '123456', 'test1@example.com'),
('test2', '123456', 'test2@example.com');

-- 创建文章表
CREATE TABLE IF NOT EXISTS article (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    content TEXT,
    author_id INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (author_id) REFERENCES user(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 插入一些测试文章数据
INSERT INTO article (title, content, author_id) VALUES
('第一篇文章', '这是第一篇文章的内容', 1),
('第二篇文章', '这是第二篇文章的内容', 1),
('测试文章', '这是一篇测试文章', 2); 