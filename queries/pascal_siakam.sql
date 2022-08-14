SELECT ros.Player, ros.Year, ros.School, ros.Class, ros.Height, total.MP, adv.'USG%', adv.'TS%', per_40.'3P', per_40.'3P%', per_40.'FT%', adv.'STL%', adv.'BLK%', adv.'AST%', adv.WS, adv.BPM
FROM roster ros
JOIN per_40_min per_40 on per_40.Player = ros.Player AND per_40.Year = ros.Year AND per_40.School = ros.School
JOIN total total on total.Player = ros.Player AND total.Year = ros.Year AND total.School = ros.School
JOIN advanced adv on adv.Player = ros.Player AND adv.Year = ros.Year AND adv.School = ros.School
JOIN per_100_poss per_100 on per_100.Player = ros.Player AND per_100.Year = ros.Year AND per_100.School = ros.School
WHERE total.MP > 300 AND adv.'STL%' >= 1.5 AND adv.'AST%' >= 10 AND adv.'ORB%' >= 10 AND adv.'BLK%' >= 5 AND per_100.FTA >= 10
order by adv.BPM desc
