CREATE TABLE IF NOT EXISTS messages_table (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
	sender TEXT COMMENT 'user/bot/assitant',
    message_text TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    is_user_message BOOLEAN
);
