-- Sample Data for Sports League Database
-- Insert test data for a mini soccer league

USE sports_league;

-- ============================================================================
-- LOOKUP DATA
-- ============================================================================

INSERT INTO Leagues (league_name, country, founded_year) VALUES
('Premier Championship', 'England', 1992),
('National Division', 'England', 2000);

INSERT INTO Positions (position_name, position_abbreviation, description) VALUES
('Goalkeeper', 'GK', 'Defends the goal'),
('Defender', 'DF', 'Defends the team'),
('Midfielder', 'MF', 'Midfield playmaker'),
('Forward', 'FW', 'Attacking player');

INSERT INTO Venues (venue_name, city, country, capacity, surface_type) VALUES
('Old Trafford', 'Manchester', 'England', 74140, 'Grass'),
('Anfield', 'Liverpool', 'England', 61294, 'Grass'),
('Stamford Bridge', 'London', 'England', 60004, 'Grass'),
('Etihad Stadium', 'Manchester', 'England', 55097, 'Grass'),
('St James Park', 'Newcastle', 'England', 52354, 'Grass');

INSERT INTO Coaches (first_name, last_name, date_of_birth, nationality, license_level) VALUES
('Erik', 'ten Hag', '1970-02-05', 'Netherlands', 'Pro'),
('Jurgen', 'Klopp', '1967-06-16', 'Germany', 'Pro'),
('Enzo', 'Maresca', '1985-11-21', 'Italy', 'Pro'),
('Pep', 'Guardiola', '1971-01-21', 'Spain', 'Pro'),
('Eddie', 'Howe', '1973-11-29', 'England', 'Pro');

-- ============================================================================
-- TEAMS
-- ============================================================================

INSERT INTO Teams (team_name, league_id, founded_year, home_venue_id, manager_coach_id, city, country) VALUES
('Manchester United', 1, 1878, 1, 1, 'Manchester', 'England'),
('Liverpool FC', 1, 1892, 2, 2, 'Liverpool', 'England'),
('Chelsea FC', 1, 1905, 3, 3, 'London', 'England'),
('Manchester City', 1, 1880, 4, 4, 'Manchester', 'England'),
('Newcastle United', 1, 1880, 5, 5, 'Newcastle', 'England');

-- ============================================================================
-- SEASONS
-- ============================================================================

INSERT INTO Seasons (league_id, season_year, start_date, end_date) VALUES
(1, '2023-24', '2023-08-15', '2024-05-31'),
(1, '2024-25', '2024-08-15', '2025-05-31');

-- ============================================================================
-- PLAYERS
-- ============================================================================

INSERT INTO Players (first_name, last_name, date_of_birth, nationality, primary_position_id, height_cm, weight_kg) VALUES
-- Manchester United
('David', 'de Gea', '1990-11-03', 'Spain', 1, 182, 79),
('Harry', 'Maguire', '1993-03-05', 'England', 2, 194, 92),
('Aaron', 'Wan-Bissaka', '1997-11-26', 'England', 2, 183, 81),
('Bruno', 'Fernandes', '1994-09-08', 'Portugal', 3, 179, 82),
('Rasmus', 'Hojlund', '2003-02-02', 'Denmark', 4, 194, 85),
('Mason', 'Mount', '1999-01-10', 'England', 3, 183, 78),
('Luke', 'Shaw', '1995-07-22', 'England', 2, 188, 82),
('Casemiro', 'Junior', '1992-02-23', 'Brazil', 3, 184, 82),

-- Liverpool FC
('Alisson', 'Ramses', '1992-10-02', 'Brazil', 1, 188, 91),
('Virgil', 'van Dijk', '1991-07-08', 'Netherlands', 2, 193, 86),
('Trent', 'Alexander-Arnold', '1998-10-07', 'England', 2, 188, 81),
('Mohamed', 'Salah', '1992-06-15', 'Egypt', 4, 175, 78),
('Luis', 'Diaz', '1997-01-13', 'Colombia', 4, 180, 73),
('Ryan', 'Gravenberch', '2002-08-26', 'Netherlands', 3, 185, 80),
('Dominic', 'Szoboszlai', '2000-10-25', 'Hungary', 3, 185, 76),

-- Chelsea FC
('Robert', 'Sánchez', '1996-11-18', 'Spain', 1, 180, 80),
('Thiago', 'Silva', '1984-09-22', 'Brazil', 2, 180, 77),
('Reece', 'James', '2001-12-08', 'England', 2, 190, 88),
('Enzo', 'Fernández', '2001-01-17', 'Argentina', 3, 180, 75),
('Nicolás', 'Jackson', '2001-06-06', 'Senegal', 4, 190, 80),
('Moisés', 'Caicedo', '2003-08-02', 'Ecuador', 3, 188, 78),

-- Manchester City
('Ederson', 'Moraes', '1995-08-17', 'Brazil', 1, 188, 86),
('Ruben', 'Dias', '1997-05-14', 'Portugal', 2, 188, 82),
('Kyle', 'Walker', '1990-05-28', 'England', 2, 188, 88),
('Erling', 'Haaland', '2000-07-21', 'Norway', 4, 194, 88),
('Phil', 'Foden', '2000-05-17', 'England', 3, 180, 73),
('Rodri', 'Hernández', '1996-06-22', 'Spain', 3, 190, 82),

-- Newcastle United
('Nick', 'Pope', '1992-04-07', 'England', 1, 183, 84),
('Sven', 'Botman', '2000-12-08', 'Netherlands', 2, 195, 92),
('Kieran', 'Trippier', '1990-09-19', 'England', 2, 178, 75),
('Alexander', 'Isak', '1996-09-28', 'Sweden', 4, 195, 92),
('Callum', 'Wilson', '1992-09-27', 'England', 4, 188, 85),
('Joelinton', 'Cassio', '1996-08-26', 'Brazil', 3, 186, 86);

-- ============================================================================
-- PLAYER TEAM HISTORY
-- ============================================================================

INSERT INTO PlayerTeamHistory (player_id, team_id, season_id, jersey_number, start_date, end_date, contract_status) VALUES
-- Manchester United 2023-24
(1, 1, 1, 1, '2023-08-15', NULL, 'Active'),
(2, 1, 1, 6, '2023-08-15', NULL, 'Active'),
(3, 1, 1, 29, '2023-08-15', NULL, 'Active'),
(4, 1, 1, 8, '2023-08-15', NULL, 'Active'),
(5, 1, 1, 9, '2023-08-15', NULL, 'Active'),
(6, 1, 1, 7, '2023-08-15', NULL, 'Active'),
(7, 1, 1, 23, '2023-08-15', NULL, 'Active'),
(8, 1, 1, 18, '2023-08-15', NULL, 'Active'),

-- Liverpool 2023-24
(9, 2, 1, 1, '2023-08-15', NULL, 'Active'),
(10, 2, 1, 4, '2023-08-15', NULL, 'Active'),
(11, 2, 1, 66, '2023-08-15', NULL, 'Active'),
(12, 2, 1, 11, '2023-08-15', NULL, 'Active'),
(13, 2, 1, 23, '2023-08-15', NULL, 'Active'),
(14, 2, 1, 38, '2023-08-15', NULL, 'Active'),
(15, 2, 1, 8, '2023-08-15', NULL, 'Active'),

-- Chelsea 2023-24
(16, 3, 1, 1, '2023-08-15', NULL, 'Active'),
(17, 3, 1, 6, '2023-08-15', NULL, 'Active'),
(18, 3, 1, 24, '2023-08-15', NULL, 'Active'),
(19, 3, 1, 5, '2023-08-15', NULL, 'Active'),
(20, 3, 1, 15, '2023-08-15', NULL, 'Active'),
(21, 3, 1, 25, '2023-08-15', NULL, 'Active'),

-- Manchester City 2023-24
(22, 4, 1, 1, '2023-08-15', NULL, 'Active'),
(23, 4, 1, 3, '2023-08-15', NULL, 'Active'),
(24, 4, 1, 2, '2023-08-15', NULL, 'Active'),
(25, 4, 1, 9, '2023-08-15', NULL, 'Active'),
(26, 4, 1, 47, '2023-08-15', NULL, 'Active'),
(27, 4, 1, 16, '2023-08-15', NULL, 'Active'),

-- Newcastle 2023-24
(28, 5, 1, 1, '2023-08-15', NULL, 'Active'),
(29, 5, 1, 6, '2023-08-15', NULL, 'Active'),
(30, 5, 1, 2, '2023-08-15', NULL, 'Active'),
(31, 5, 1, 14, '2023-08-15', NULL, 'Active'),
(32, 5, 1, 19, '2023-08-15', NULL, 'Active'),
(33, 5, 1, 8, '2023-08-15', NULL, 'Active');

-- ============================================================================
-- GAMES
-- ============================================================================

INSERT INTO Games (season_id, home_team_id, away_team_id, venue_id, game_date, game_time, home_goals, away_goals, attendance, referee_name, status) VALUES
(1, 1, 2, 1, '2023-08-20', '15:00', 1, 0, 74140, 'Michael Oliver', 'Completed'),
(1, 3, 4, 3, '2023-08-20', '12:30', 1, 2, 60004, 'Stuart Attwell', 'Completed'),
(1, 5, 1, 5, '2023-08-22', '19:45', 0, 2, 52354, 'Craig Pawson', 'Completed'),
(1, 2, 3, 2, '2023-08-23', '15:00', 3, 1, 61294, 'David Coote', 'Completed'),
(1, 4, 5, 4, '2023-08-23', '19:45', 4, 0, 55097, 'Paul Tierney', 'Completed'),
(1, 1, 4, 1, '2023-09-02', '12:30', 0, 1, 74140, 'Michael Oliver', 'Completed'),
(1, 2, 5, 2, '2023-09-03', '15:00', 2, 1, 61294, 'Stuart Attwell', 'Completed'),
(1, 3, 1, 3, '2023-09-04', '19:45', 2, 2, 60004, 'Craig Pawson', 'Completed');

-- ============================================================================
-- GAME LINEUPS
-- ============================================================================

-- Game 1: Manchester United vs Liverpool (1-0)
INSERT INTO GameLineups (game_id, player_id, team_id, position_id, shirt_number, is_starter, minutes_played) VALUES
(1, 1, 1, 1, 1, TRUE, 90),
(1, 2, 1, 2, 6, TRUE, 90),
(1, 3, 1, 2, 29, TRUE, 88),
(1, 4, 1, 3, 8, TRUE, 90),
(1, 5, 1, 4, 9, TRUE, 90),
(1, 7, 1, 2, 23, TRUE, 70),
(1, 8, 1, 3, 18, TRUE, 90),
(1, 9, 2, 1, 1, TRUE, 90),
(1, 10, 2, 2, 4, TRUE, 90),
(1, 11, 2, 2, 66, TRUE, 90),
(1, 12, 2, 4, 11, TRUE, 85),
(1, 13, 2, 4, 23, TRUE, 90),
(1, 14, 2, 3, 38, TRUE, 90),
(1, 15, 2, 3, 8, TRUE, 90);

-- Game 2: Chelsea vs Manchester City (1-2)
INSERT INTO GameLineups (game_id, player_id, team_id, position_id, shirt_number, is_starter, minutes_played) VALUES
(2, 16, 3, 1, 1, TRUE, 90),
(2, 17, 3, 2, 6, TRUE, 90),
(2, 18, 3, 2, 24, TRUE, 90),
(2, 19, 3, 3, 5, TRUE, 90),
(2, 20, 3, 4, 15, TRUE, 72),
(2, 21, 3, 3, 25, TRUE, 88),
(2, 22, 4, 1, 1, TRUE, 90),
(2, 23, 4, 2, 3, TRUE, 90),
(2, 24, 4, 2, 2, TRUE, 90),
(2, 25, 4, 4, 9, TRUE, 90),
(2, 26, 4, 3, 47, TRUE, 90),
(2, 27, 4, 3, 16, TRUE, 85);

-- ============================================================================
-- PLAYER GAME STATS
-- ============================================================================

-- Game 1: Manchester United vs Liverpool (1-0)
INSERT INTO PlayerGameStats (game_id, player_id, team_id, goals_scored, assists, shots_on_target, total_shots, passes_completed, total_passes, tackles, interceptions, fouls_committed, fouls_suffered, yellow_cards, red_cards, own_goals) VALUES
(1, 5, 1, 1, 0, 2, 4, 15, 22, 1, 1, 0, 0, 0, 0, 0),
(1, 4, 1, 0, 1, 1, 3, 45, 65, 2, 0, 1, 0, 0, 0, 0),
(1, 12, 2, 1, 0, 3, 5, 38, 52, 2, 1, 0, 0, 1, 0, 0),
(1, 13, 2, 0, 0, 1, 2, 32, 48, 1, 0, 0, 0, 0, 0, 0),
(1, 14, 2, 0, 0, 2, 3, 28, 41, 0, 0, 1, 0, 0, 0, 0);

-- Game 2: Chelsea vs Manchester City (1-2)
INSERT INTO PlayerGameStats (game_id, player_id, team_id, goals_scored, assists, shots_on_target, total_shots, passes_completed, total_passes, tackles, interceptions, fouls_committed, fouls_suffered, yellow_cards, red_cards, own_goals) VALUES
(2, 20, 3, 1, 0, 2, 4, 32, 48, 1, 1, 0, 0, 0, 0, 0),
(2, 25, 4, 2, 0, 3, 6, 58, 71, 2, 0, 0, 0, 0, 0, 0),
(2, 26, 4, 0, 1, 1, 3, 42, 54, 3, 1, 0, 0, 0, 0, 0),
(2, 27, 4, 0, 0, 2, 4, 35, 48, 4, 0, 1, 1, 0, 0, 0);

-- Additional games' basic data (minimal stats for demo)
INSERT INTO PlayerGameStats (game_id, player_id, team_id, goals_scored, assists) VALUES
(3, 31, 5, 0, 0),
(3, 5, 1, 2, 0),
(4, 12, 2, 1, 0),
(4, 20, 3, 1, 0),
(5, 25, 4, 2, 0),
(5, 28, 5, 0, 0),
(6, 1, 1, 0, 0),
(6, 25, 4, 1, 0),
(7, 12, 2, 2, 0),
(7, 31, 5, 1, 0),
(8, 4, 1, 0, 0),
(8, 19, 3, 1, 0);
