-- Criar Tabela de Usuários
CREATE TABLE users (
    id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    birth_date DATE,
    phone TEXT
);

-- Criar Tabela de Grupos
CREATE TABLE groups (
    id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    name TEXT NOT NULL,
    description TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    creator_id BIGINT REFERENCES users(id) ON DELETE SET NULL,
    deleted_at TIMESTAMP WITH TIME ZONE
);

-- Criar Tabela de Usuários de Grupos
CREATE TABLE group_users (
    group_id BIGINT REFERENCES groups(id) ON DELETE CASCADE,
    user_id BIGINT REFERENCES users(id) ON DELETE CASCADE,
    PRIMARY KEY (group_id, user_id),
    deleted_at TIMESTAMP WITH TIME ZONE
);

-- Criar Tabela de Áreas
CREATE TABLE areas (
    id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    name TEXT NOT NULL,
    description TEXT,
    user_id BIGINT REFERENCES users(id) ON DELETE SET NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    group_id BIGINT REFERENCES groups(id) ON DELETE SET NULL,
    deleted_at TIMESTAMP WITH TIME ZONE
);

-- Criar Tabela de Modelos
CREATE TABLE templates (
    id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    name TEXT NOT NULL,
    content TEXT,
    area_id BIGINT REFERENCES areas(id) ON DELETE SET NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    group_id BIGINT REFERENCES groups(id) ON DELETE SET NULL,
    deleted_at TIMESTAMP WITH TIME ZONE
);

-- Criar Tabela de Notas
CREATE TABLE notes (
    id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    title TEXT NOT NULL,
    content TEXT,
    user_id BIGINT REFERENCES users(id) ON DELETE SET NULL,
    area_id BIGINT REFERENCES areas(id) ON DELETE SET NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    group_id BIGINT REFERENCES groups(id) ON DELETE SET NULL,
    favorite BOOLEAN DEFAULT FALSE,
    last_modified TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    deleted_at TIMESTAMP WITH TIME ZONE
);

-- Criar Tabela de Tarefas
CREATE TABLE tasks (
    id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    title TEXT NOT NULL,
    description TEXT,
    due_date DATE,
    status TEXT CHECK (status IN ('pending', 'completed', 'overdue')) DEFAULT 'pending',
    user_id BIGINT REFERENCES users(id) ON DELETE SET NULL,
    area_id BIGINT REFERENCES areas(id) ON DELETE SET NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    group_id BIGINT REFERENCES groups(id) ON DELETE SET NULL,
    deadline TIMESTAMP WITH TIME ZONE,
    priority TEXT CHECK (priority IN ('low', 'medium', 'high')) DEFAULT 'medium',
    deleted_at TIMESTAMP WITH TIME ZONE,
    related_task_id BIGINT REFERENCES tasks(id) ON DELETE SET NULL
);

-- Criar Tabela de Eventos
CREATE TABLE events (
    id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    title TEXT NOT NULL,
    description TEXT,
    event_date TIMESTAMP WITH TIME ZONE,
    user_id BIGINT REFERENCES users(id) ON DELETE SET NULL,
    area_id BIGINT REFERENCES areas(id) ON DELETE SET NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    group_id BIGINT REFERENCES groups(id) ON DELETE SET NULL,
    deleted_at TIMESTAMP WITH TIME ZONE
);

-- Criar Tabela de Projetos
CREATE TABLE projects (
    id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    name TEXT NOT NULL,
    description TEXT,
    start_date DATE,
    end_date DATE,
    user_id BIGINT REFERENCES users(id) ON DELETE SET NULL,
    area_id BIGINT REFERENCES areas(id) ON DELETE SET NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    group_id BIGINT REFERENCES groups(id) ON DELETE SET NULL,
    deleted_at TIMESTAMP WITH TIME ZONE
);

-- Criar Tabela de Conexões de Entidades
CREATE TABLE entity_edges (
    id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    note_id BIGINT,
    task_id BIGINT,
    event_id BIGINT,
    project_id BIGINT,
    relationship_type TEXT NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    deleted_at TIMESTAMP WITH TIME ZONE,
    CHECK (
      (note_id IS NOT NULL)::int +
      (task_id IS NOT NULL)::int +
      (event_id IS NOT NULL)::int +
      (project_id IS NOT NULL)::int >= 2
    )
);

-- Criar Tabela de Arquivos
CREATE TABLE files (
    id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    file_path TEXT NOT NULL,
    table_id BIGINT NOT NULL,
    uploaded_by BIGINT REFERENCES users(id) ON DELETE SET NULL,
    upload_date TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    deleted_date TIMESTAMP WITH TIME ZONE,
    note_id BIGINT REFERENCES notes(id) ON DELETE SET NULL,
    task_id BIGINT REFERENCES tasks(id) ON DELETE SET NULL,
    event_id BIGINT REFERENCES events(id) ON DELETE SET NULL,
    project_id BIGINT REFERENCES projects(id) ON DELETE SET NULL
);