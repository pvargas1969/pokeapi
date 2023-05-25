USE POKEAPI
GO

CREATE TABLE pokemon_moves
    (
    [pokemon_id]                Integer not null,
    [version_group_id]          Integer not null,
    [move_id]                   Integer not null,
    [pokemon_move_method_id]    Integer not null,
    [level]                     Integer not null,
    [order]                     Integer not null,
    )
GO
