SELECT
	pok_name,
	b_speed
FROM pokemon p
inner join base_stats bs on bs.pok_id = p.pok_id
order by bs.b_speed desc
limit 5;
