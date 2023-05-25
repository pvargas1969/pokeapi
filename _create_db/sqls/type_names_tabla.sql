USE POKEAPI
GO

IF EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID('dbo.[type_names]') AND type in ('U'))
	DROP TABLE dbo.[type_names]
GO

CREATE TABLE [type_names]
    (
    [type_id]             Integer     not null,
    [local_language_id]   Integer     not null,
    [name]                VarChar(20) not null,
    )
GO
