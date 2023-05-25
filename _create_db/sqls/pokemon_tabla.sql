USE POKEAPI
GO

IF EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID('dbo.[pokemon]') AND type in ('U'))
	DROP TABLE dbo.[pokemon]
GO

CREATE TABLE [pokemon]
    (
    [id]                  Integer     not null,
    [identifier]          VarChar(40) not null,
    [species_id]          Integer     not null,
    [height]              Integer     not null,
    [weight]              Integer     not null,
    [base_experience]     Integer     not null,
    [order]               Integer     not null,
    [is_default]          Integer     not null,
    )
GO
