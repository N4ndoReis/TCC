-- Popular Tabela de Arquivos
DO $$
BEGIN
    FOR i IN 1..100 LOOP
        INSERT INTO files (file_path, table_id, uploaded_by, note_id, task_id, event_id, project_id)
        VALUES (
            '/caminho/para/arquivo' || i || '.txt', -- Caminho do arquivo
            (RANDOM() * 1000)::int, -- ID da tabela aleatório
            (SELECT id FROM users ORDER BY RANDOM() LIMIT 1), -- Seleciona um usuário aleatório
            (SELECT id FROM notes ORDER BY RANDOM() LIMIT 1), -- Seleciona uma nota aleatória
            (SELECT id FROM tasks ORDER BY RANDOM() LIMIT 1), -- Seleciona uma tarefa aleatória
            (SELECT id FROM events ORDER BY RANDOM() LIMIT 1), -- Seleciona um evento aleatório
            (SELECT id FROM projects ORDER BY RANDOM() LIMIT 1) -- Seleciona um projeto aleatório
        );
    END LOOP;
END $$;