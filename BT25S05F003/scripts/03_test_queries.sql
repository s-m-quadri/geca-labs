-- Test Queries for Sports League Database
-- Comprehensive analytics and reporting queries

USE sports_league;

-- ============================================================================
-- BASIC QUERIES
-- ============================================================================

-- Query 1: All teams in the Premier Championship
SELECT t.team_id, t.team_name, t.founded_year, v.venue_name, c.first_name, c.last_name
FROM Teams t
LEFT JOIN Venues v ON t.home_venue_id = v.venue_id
LEFT JOIN Coaches c ON t.manager_coach_id = c.coach_id
WHERE t.league_id = (SELECT league_id FROM Leagues WHERE league_name = 'Premier Championship')
ORDER BY t.team_name;

-- Query 2: All players for Manchester United
SELECT p.player_id, CONCAT(p.first_name, ' ', p.last_name) AS player_name, 
       pos.position_abbreviation, pth.jersey_number, p.height_cm, p.weight_kg
FROM Players p
JOIN PlayerTeamHistory pth ON p.player_id = pth.player_id
JOIN Positions pos ON p.primary_position_id = pos.position_id
WHERE pth.team_id = (SELECT team_id FROM Teams WHERE team_name = 'Manchester United')
  AND pth.end_date IS NULL
ORDER BY pos.position_name, p.last_name;

-- ============================================================================
-- STANDING & PERFORMANCE QUERIES
-- ============================================================================

-- Query 3: Team Standings for 2023-24 Season (using VIEW)
SELECT * FROM TeamStandings
WHERE season_year = '2023-24'
ORDER BY wins DESC, draws DESC;

-- Query 4: Calculate points (3 for win, 1 for draw) for standings
SELECT 
    s.season_year,
    t.team_name,
    ts.matches_played,
    ts.wins,
    ts.draws,
    ts.losses,
    (ts.wins * 3 + ts.draws * 1) AS points,
    ts.goals_for,
    ts.goals_against,
    (ts.goals_for - ts.goals_against) AS goal_difference
FROM TeamStandings ts
JOIN Seasons s ON ts.season_id = s.season_id
JOIN Teams t ON ts.team_id = t.team_id
WHERE s.season_year = '2023-24'
ORDER BY (ts.wins * 3 + ts.draws * 1) DESC, (ts.goals_for - ts.goals_against) DESC;

-- ============================================================================
-- GOAL SCORER QUERIES
-- ============================================================================

-- Query 5: Top Scorers in 2023-24 Season (using VIEW)
SELECT * FROM TopScorers
WHERE season_year = '2023-24'
ORDER BY total_goals DESC, player_name;

-- Query 6: Top Scorers by Team
SELECT 
    s.season_year,
    t.team_name,
    CONCAT(p.first_name, ' ', p.last_name) AS player_name,
    SUM(pgs.goals_scored) AS total_goals,
    COUNT(DISTINCT pgs.game_id) AS games_scored_in,
    ROUND(SUM(pgs.goals_scored) / COUNT(DISTINCT pgs.game_id), 2) AS goals_per_game
FROM Seasons s
JOIN Games g ON s.season_id = g.season_id
JOIN PlayerGameStats pgs ON g.game_id = pgs.game_id
JOIN Players p ON pgs.player_id = p.player_id
JOIN Teams t ON pgs.team_id = t.team_id
WHERE g.status = 'Completed' AND s.season_year = '2023-24'
GROUP BY s.season_year, t.team_id, t.team_name, p.player_id
HAVING total_goals > 0
ORDER BY t.team_name, total_goals DESC;

-- ============================================================================
-- HEAD-TO-HEAD QUERIES
-- ============================================================================

-- Query 7: Head-to-Head: Manchester United vs Liverpool
SELECT 
    g.game_id,
    g.game_date,
    ht.team_name AS home_team,
    g.home_goals,
    g.away_goals,
    at.team_name AS away_team,
    CASE 
        WHEN g.home_goals > g.away_goals THEN ht.team_name
        WHEN g.away_goals > g.home_goals THEN at.team_name
        ELSE 'Draw'
    END AS winner
FROM Games g
JOIN Teams ht ON g.home_team_id = ht.team_id
JOIN Teams at ON g.away_team_id = at.team_id
WHERE (ht.team_name = 'Manchester United' AND at.team_name = 'Liverpool FC')
   OR (ht.team_name = 'Liverpool FC' AND at.team_name = 'Manchester United')
ORDER BY g.game_date;

-- Query 8: Head-to-Head Summary Stats
SELECT 
    CASE WHEN ht.team_name = 'Manchester United' THEN 'Manchester United' ELSE 'Liverpool FC' END AS team,
    SUM(CASE WHEN ht.team_name = 'Manchester United' THEN g.home_goals ELSE g.away_goals END) +
    SUM(CASE WHEN at.team_name = 'Manchester United' THEN g.away_goals ELSE g.home_goals END) AS goals_for,
    SUM(CASE WHEN ht.team_name = 'Manchester United' THEN g.away_goals ELSE g.home_goals END) +
    SUM(CASE WHEN at.team_name = 'Manchester United' THEN g.home_goals ELSE g.away_goals END) AS goals_against,
    SUM(CASE 
        WHEN (ht.team_id = 1 AND g.home_goals > g.away_goals) OR 
             (at.team_id = 1 AND g.away_goals > g.home_goals) THEN 1 
        ELSE 0 
    END) AS wins,
    SUM(CASE WHEN g.home_goals = g.away_goals THEN 1 ELSE 0 END) AS draws,
    SUM(CASE 
        WHEN (ht.team_id = 1 AND g.home_goals < g.away_goals) OR 
             (at.team_id = 1 AND g.away_goals < g.home_goals) THEN 1 
        ELSE 0 
    END) AS losses
FROM Games g
JOIN Teams ht ON g.home_team_id = ht.team_id
JOIN Teams at ON g.away_team_id = at.team_id
WHERE g.status = 'Completed'
  AND ((ht.team_name = 'Manchester United' AND at.team_name = 'Liverpool FC') OR
       (ht.team_name = 'Liverpool FC' AND at.team_name = 'Manchester United'));

-- ============================================================================
-- PLAYER STATISTICS QUERIES
-- ============================================================================

-- Query 9: Player Game-by-Game Performance
SELECT 
    g.game_date,
    CONCAT(CONCAT(ht.team_name, ' vs '), at.team_name) AS match_up,
    CONCAT(p.first_name, ' ', p.last_name) AS player_name,
    pgs.goals_scored,
    pgs.assists,
    pgs.shots_on_target,
    pgs.passes_completed,
    pgs.tackles,
    pgs.yellow_cards,
    pgs.red_cards
FROM Games g
JOIN Teams ht ON g.home_team_id = ht.team_id
JOIN Teams at ON g.away_team_id = at.team_id
JOIN PlayerGameStats pgs ON g.game_id = pgs.game_id
JOIN Players p ON pgs.player_id = p.player_id
WHERE g.status = 'Completed' AND pgs.goals_scored > 0
ORDER BY g.game_date DESC, pgs.goals_scored DESC;

-- Query 10: Player Season Aggregate Stats
SELECT 
    s.season_year,
    CONCAT(p.first_name, ' ', p.last_name) AS player_name,
    CONCAT(pos.position_name) AS position,
    t.team_name,
    COUNT(DISTINCT pgs.game_id) AS games_played,
    SUM(pgs.goals_scored) AS total_goals,
    SUM(pgs.assists) AS total_assists,
    SUM(pgs.shots_on_target) AS total_shots_on_target,
    ROUND(SUM(pgs.passes_completed) / COUNT(DISTINCT pgs.game_id), 0) AS avg_passes_per_game,
    SUM(pgs.tackles) AS total_tackles,
    SUM(pgs.yellow_cards) AS yellow_cards,
    SUM(pgs.red_cards) AS red_cards
FROM Seasons s
JOIN Games g ON s.season_id = g.season_id
JOIN PlayerGameStats pgs ON g.game_id = pgs.game_id
JOIN Players p ON pgs.player_id = p.player_id
JOIN Positions pos ON p.primary_position_id = pos.position_id
JOIN Teams t ON pgs.team_id = t.team_id
WHERE g.status = 'Completed' AND s.season_year = '2023-24'
GROUP BY s.season_id, p.player_id, pos.position_id, t.team_id
ORDER BY total_goals DESC, total_assists DESC;

-- ============================================================================
-- POSITION-BASED ANALYTICS
-- ============================================================================

-- Query 11: Average Goals by Position
SELECT 
    pos.position_name,
    COUNT(DISTINCT p.player_id) AS player_count,
    SUM(pgs.goals_scored) AS total_goals,
    ROUND(AVG(pgs.goals_scored), 2) AS avg_goals_per_game,
    COUNT(DISTINCT pgs.game_id) AS total_game_appearances
FROM Players p
JOIN Positions pos ON p.primary_position_id = pos.position_id
JOIN PlayerGameStats pgs ON p.player_id = pgs.player_id
GROUP BY pos.position_id, pos.position_name
ORDER BY avg_goals_per_game DESC;

-- ============================================================================
-- TRANSFER & TEAM CHANGE QUERIES
-- ============================================================================

-- Query 12: Player Transfer History
SELECT 
    CONCAT(p.first_name, ' ', p.last_name) AS player_name,
    pos.position_name,
    pth.start_date,
    pth.end_date,
    t.team_name,
    pth.jersey_number,
    s.season_year
FROM PlayerTeamHistory pth
JOIN Players p ON pth.player_id = p.player_id
JOIN Positions pos ON p.primary_position_id = pos.position_id
JOIN Teams t ON pth.team_id = t.team_id
JOIN Seasons s ON pth.season_id = s.season_id
ORDER BY p.last_name, pth.start_date DESC;

-- Query 13: Current Squad Composition by Team
SELECT 
    t.team_name,
    pos.position_name,
    COUNT(pth.player_id) AS player_count
FROM Teams t
JOIN PlayerTeamHistory pth ON t.team_id = pth.team_id
JOIN Players p ON pth.player_id = p.player_id
JOIN Positions pos ON p.primary_position_id = pos.position_id
WHERE pth.end_date IS NULL
GROUP BY t.team_id, t.team_name, pos.position_id, pos.position_name
ORDER BY t.team_name, FIELD(pos.position_name, 'Goalkeeper', 'Defender', 'Midfielder', 'Forward');

-- ============================================================================
-- GAME ATTENDANCE & STATISTICS
-- ============================================================================

-- Query 14: Game Attendance by Stadium
SELECT 
    v.venue_name,
    COUNT(g.game_id) AS total_games,
    SUM(COALESCE(g.attendance, 0)) AS total_attendance,
    ROUND(AVG(COALESCE(g.attendance, 0)), 0) AS avg_attendance,
    MAX(COALESCE(g.attendance, 0)) AS max_attendance
FROM Venues v
LEFT JOIN Games g ON v.venue_id = g.venue_id AND g.status = 'Completed'
GROUP BY v.venue_id, v.venue_name
ORDER BY avg_attendance DESC;

-- Query 15: Highest Scoring Games
SELECT 
    g.game_date,
    ht.team_name AS home_team,
    g.home_goals,
    g.away_goals,
    at.team_name AS away_team,
    (g.home_goals + g.away_goals) AS total_goals,
    v.venue_name,
    COALESCE(g.attendance, 0) AS attendance
FROM Games g
JOIN Teams ht ON g.home_team_id = ht.team_id
JOIN Teams at ON g.away_team_id = at.team_id
JOIN Venues v ON g.venue_id = v.venue_id
WHERE g.status = 'Completed'
ORDER BY total_goals DESC, g.game_date DESC;

-- ============================================================================
-- DATA INTEGRITY CHECKS
-- ============================================================================

-- Query 16: Find Missing Player Stats in Lineups
SELECT 
    gl.game_lineup_id,
    CONCAT(p.first_name, ' ', p.last_name) AS player_name,
    gl.game_id,
    gl.is_starter
FROM GameLineups gl
JOIN Players p ON gl.player_id = p.player_id
LEFT JOIN PlayerGameStats pgs ON gl.game_id = pgs.game_id AND gl.player_id = pgs.player_id
WHERE pgs.game_stat_id IS NULL
ORDER BY gl.game_id;

-- Query 17: Games with Incomplete Data
SELECT 
    g.game_id,
    ht.team_name,
    at.team_name,
    g.game_date,
    COUNT(gl.game_lineup_id) AS lineup_entries,
    COUNT(pgs.game_stat_id) AS stat_entries,
    g.status
FROM Games g
JOIN Teams ht ON g.home_team_id = ht.team_id
JOIN Teams at ON g.away_team_id = at.team_id
LEFT JOIN GameLineups gl ON g.game_id = gl.game_id
LEFT JOIN PlayerGameStats pgs ON g.game_id = pgs.game_id
WHERE g.status = 'Completed'
GROUP BY g.game_id
HAVING lineup_entries = 0 OR stat_entries = 0;
