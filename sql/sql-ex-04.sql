select
	pok_name
from pokemon p
inner join base_stats bs on p.pok_id = bs.pok_id
where bs.b_hp > 100;
