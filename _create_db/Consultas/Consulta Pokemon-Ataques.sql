SELECT	* --MOV.version_group_id, COUNT(*)
FROM	pokemon							PKM
		INNER JOIN pokemon_moves		MOV
			ON	PKM.id	= MOV.pokemon_id
		INNER JOIN move_names			MVN
			ON	MOV.move_id	= MVN.move_id
WHERE	PKM.id	= 6
  AND	MOV.version_group_id = 16
  AND	MVN.local_language_id = 7
