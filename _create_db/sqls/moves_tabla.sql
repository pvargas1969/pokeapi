USE POKEAPI
GO

CREATE TABLE [moves]
    (
    [id]                        Integer         not null,
    [identifier]                VarChar(40)     not null,
    [generation_id]             Integer         not null,
    [type_id]                   Integer         not null,
    [power]                     Integer         not null,
    [pp]                        Integer         not null,
    [accuracy]                  Integer         not null,
    [priority]                  Integer         not null,
    [target_id]                 Integer         not null,
    [damage_class_id]           Integer         not null,
    [effect_id]                 Integer         not null,
    [effect_chance]             Integer         not null,
    [contest_type_id]           Integer         not null,
    [contest_effect_id]         Integer         not null,
    [super_contest_effect_id]   Integer         not null,
    )
GO
