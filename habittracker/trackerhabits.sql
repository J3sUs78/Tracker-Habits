-- Elimina la base de datos y usuario si existen (para desarrollo, quitar en producción)
DROP DATABASE IF EXISTS trackerhabits;
DROP USER IF EXISTS trackeruser;

-- Crea la base de datos y usuario
CREATE DATABASE trackerhabits
  WITH OWNER = trackeruser
  ENCODING = 'UTF8'
  TEMPLATE = template0;

CREATE USER trackeruser WITH PASSWORD 'trackerpass';
GRANT ALL PRIVILEGES ON DATABASE trackerhabits TO trackeruser;

\c trackerhabits;

-- Tabla extendida de usuarios (relacionada con Django User por user_id)
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL UNIQUE, -- Relaciona con auth_user.id de Django
    email VARCHAR(254) NOT NULL,
    phone VARCHAR(20),
    notification_enabled BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabla de categorías de hábitos
CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    description TEXT
);

-- Tabla de hábitos
CREATE TABLE habits (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    active BOOLEAN DEFAULT TRUE,
    periodicity VARCHAR(10) NOT NULL CHECK (periodicity IN ('diario', 'semanal', 'mensual')),
    goal INTEGER DEFAULT 1 CHECK (goal > 0),
    category_id INTEGER REFERENCES categories(id),
    UNIQUE(user_id, name)
);

-- Tabla de registros de hábitos
CREATE TABLE habit_records (
    id SERIAL PRIMARY KEY,
    habit_id INTEGER NOT NULL REFERENCES habits(id) ON DELETE CASCADE,
    date DATE NOT NULL,
    completed BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(habit_id, date)
);

-- Índices para optimización
CREATE INDEX idx_habits_user_id ON habits(user_id);
CREATE INDEX idx_habit_records_habit_id ON habit_records(habit_id);

-- Permisos
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO trackeruser;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO trackeruser;