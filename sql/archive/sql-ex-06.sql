SELECT
	pok_name,
	b_atk
FROM pokemon p
inner join base_stats bs on bs.pok_id = bs.pok_id
order by bs.b_atk desc;
