# a sequence of SQL commands to be executed

SQL_SCRIPT = [
    'USE inventory;',
    
    'SET autocommit = 1;',
     
    # 'CREATE TABLE IF NOT EXISTS Transactions( \
    #     id INT NOT NULL, \
    #     type VARCHAR (20) NOT NULL, \
    #     unit_price DOUBLE NOT NULL, \
    #     num_of_tires INT NOT NULL, \
    #     total_price DOUBLE NOT NULL, \
    #     PRIMARY KEY( id ) \
    # );',
    
    #'INSERT INTO Transactions VALUES (2, "saida", 10.1, 5, 50.5);',
    'INSERT INTO Transactions VALUES (1, "entrada", 10.1, 10, 101.0);',
    'SHOW DATABASES',
    
    'SHOW TABLES FROM inventory;',
    
    'SELECT * FROM Transactions;'
]