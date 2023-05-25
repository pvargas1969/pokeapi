USE POKEAPI
GO

IF EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID('dbo.[pokemon_types]') AND type in ('U'))
	DROP TABLE dbo.[pokemon_types]
GO

CREATE TABLE [pokemon_types]
    (
    [pokemon_id]          Integer not null,
    [type_id]             Integer not null,
    [slot]                Integer not null,
    )
GO
