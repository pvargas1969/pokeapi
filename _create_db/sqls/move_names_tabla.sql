USE POKEAPI
GO

CREATE TABLE move_names
    (
    [move_id]             Integer       not null,
    [local_language_id]   Integer       not null,
    [name]                VarChar(40)   not null,
    )
GO
