SELECT
	pok_name,
	b_hp
FROM pokemon p
inner join base_stats bs on bs.pok_id = p.pok_id
order by bs.b_hp between 80 and 50;
