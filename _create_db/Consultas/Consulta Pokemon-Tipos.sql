SELECT	*
FROM	POKEMON								POK
		INNER JOIN POKEMON_TYPES			PTY
			ON	POK.ID	= PTY.POKEMON_ID
			AND	PTY.SLOT	= 1
		INNER JOIN TYPE_NAMES				TNM
			ON	PTY.TYPE_ID	= TNM.TYPE_ID
			AND	TNM.LOCAL_LANGUAGE_ID	= 7
		LEFT JOIN POKEMON_TYPES			PTY2
			ON	POK.ID	= PTY2.POKEMON_ID
			AND	PTY2.SLOT	= 2
		LEFT JOIN TYPE_NAMES				TNM2
			ON	PTY2.TYPE_ID	= TNM2.TYPE_ID
			AND	TNM2.LOCAL_LANGUAGE_ID	= 7
--WHERE	POK.identifier LIKE '%ARCEUS%'
