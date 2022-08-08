# ncaab-data-and-dumb-scraper

This project is a quick and dirty way to grab the rosters and player statistics for men's college basketball on sports-reference.com (going back to the 2010-11 season) and saving the data into .csv files. I lost the first version of this which wrote the data right into a sqlite database but I will eventually getting around to doing that again here.

The file 'sports-reference' is a current version of the sqlite database through the 2021-22 season.

Also, I'll be adding some queries to find some interesting players. The first one called base_query returns any year a freshman had a 2%+ steal and block rate (for defensive disruption) while making 1+ three pointer per 40 minutes and shoot 75%+ from the free throw line (for some shooting capability). Then, it's ordered by BPM descending to find the most impactful (roughly since BPM is nowhere near perfect) players first. This first query returns:

Player Year School Class Height Minutes Usage TS 3P_per_40 3P% FT% STL% BLK% WS BPM  
Jabari Smith	2022	Auburn Tigers	FR	6-10	978.0	27.6	0.57	3.2	0.42	0.799	2.1	3.8	5.6	11.1  
Marcus Smart	2013	Oklahoma State Cowboys	FR	6-4	1106.0	27.2	0.532	1.4	0.29	0.777	5.3	2.2	5.4	10.8  
Jonathan Isaac	2017	Florida State Seminoles	FR	6-10	839.0	20.3	0.614	1.5	0.348	0.78	2.4	6.2	4.3	10.0  
Mikal Bridges	2016	Villanova Wildcats	FR	6-7	813.0	14.5	0.633	1.1	0.299	0.787	3.1	3.6	3.9	9.4  
Jontay Porter	2018	Missouri Tigers	FR	6-11	808.0	22.5	0.567	2.0	0.364	0.75	2.1	7.3	3.6	9.0  
Killian Tillie	2017	Gonzaga Bulldogs	FR	6-10	404.0	16.2	0.62	1.1	0.478	0.778	3.3	2.4	2.3	8.7  
Jabari Walker	2021	Colorado Buffaloes	FR	6-8	369.0	26.0	0.641	2.5	0.523	0.778	2.0	3.7	2.2	8.4  
Bradley Beal	2012	Florida Gators	FR	6-3	1267.0	23.0	0.575	2.0	0.339	0.769	2.5	2.6	5.7	8.4  
Keegan Murray	2021	Iowa Hawkeyes	FR	6-8	558.0	18.5	0.586	1.1	0.296	0.755	2.6	7.2	2.7	8.3  
Cade Cunningham	2021	Oklahoma State Cowboys	FR	6-8	956.0	29.1	0.574	2.6	0.4	0.846	2.5	2.3	4.0	8.3  
Andrew Wiggins	2014	Kansas Jayhawks	FR	6-8	1148.0	26.3	0.563	1.5	0.341	0.775	2.1	3.1	4.9	8.3  
Jayson Tatum	2017	Duke Blue Devils	FR	6-8	966.0	26.2	0.566	1.7	0.342	0.849	2.3	3.2	4.1	7.9  
Tyler Lydon	2016	Syracuse Orange	FR	6-8	1122.0	16.5	0.606	1.7	0.405	0.774	2.3	7.0	4.7	7.8  
Kamar Baldwin	2017	Butler Bulldogs	FR	6-1	916.0	20.4	0.574	1.5	0.372	0.756	3.8	2.4	3.0	7.7  
Justin Anderson	2013	Virginia Cavaliers	FR	6-6	841.0	20.3	0.523	1.0	0.303	0.764	2.3	6.0	3.6	7.4  
