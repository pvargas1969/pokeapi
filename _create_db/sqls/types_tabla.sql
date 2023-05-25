USE POKEAPI
GO

IF EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID('dbo.[types]') AND type in ('U'))
	DROP TABLE dbo.[types]
GO

CREATE TABLE [types]
    (
    [id]                  Integer     not null,
    [identifier]          VarChar(20) not null,
    [generation_id]       Integer     not null,
    [damage_class_id]     Integer     not null,
    )
GO
