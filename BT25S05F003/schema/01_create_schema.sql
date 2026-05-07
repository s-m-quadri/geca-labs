-- Sports League Database Schema
-- Soccer league tracking system with teams, players, games, and statistics

DROP DATABASE IF EXISTS sports_league;
CREATE DATABASE sports_league;
USE sports_league;

-- ============================================================================
-- LOOKUP TABLES
-- ============================================================================

CREATE TABLE Leagues (
    league_id INT AUTO_INCREMENT PRIMARY KEY,
    league_name VARCHAR(100) NOT NULL UNIQUE,
    country VARCHAR(50),
    founded_year INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Positions (
    position_id INT AUTO_INCREMENT PRIMARY KEY,
    position_name VARCHAR(50) NOT NULL UNIQUE,
    position_abbreviation VARCHAR(5) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Venues (
    venue_id INT AUTO_INCREMENT PRIMARY KEY,
    venue_name VARCHAR(100) NOT NULL,
    city VARCHAR(50) NOT NULL,
    country VARCHAR(50),
    capacity INT,
    surface_type VARCHAR(30),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE KEY unique_venue (venue_name, city, country)
);

CREATE TABLE Coaches (
    coach_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE,
    nationality VARCHAR(50),
    license_level VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ============================================================================
-- TEAM & PLAYER CORE TABLES
-- ============================================================================

CREATE TABLE Teams (
    team_id INT AUTO_INCREMENT PRIMARY KEY,
    team_name VARCHAR(100) NOT NULL,
    league_id INT NOT NULL,
    founded_year INT,
    home_venue_id INT NOT NULL,
    manager_coach_id INT,
    city VARCHAR(50),
    country VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE KEY unique_team (team_name, league_id),
    FOREIGN KEY (league_id) REFERENCES Leagues(league_id) ON DELETE CASCADE,
    FOREIGN KEY (home_venue_id) REFERENCES Venues(venue_id) ON DELETE RESTRICT,
    FOREIGN KEY (manager_coach_id) REFERENCES Coaches(coach_id) ON DELETE SET NULL,
    INDEX idx_league (league_id),
    INDEX idx_venue (home_venue_id)
);

CREATE TABLE Seasons (
    season_id INT AUTO_INCREMENT PRIMARY KEY,
    league_id INT NOT NULL,
    season_year VARCHAR(10) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE KEY unique_season (league_id, season_year),
    FOREIGN KEY (league_id) REFERENCES Leagues(league_id) ON DELETE CASCADE,
    INDEX idx_league (league_id),
    CONSTRAINT check_date_order CHECK (start_date < end_date)
);

CREATE TABLE Players (
    player_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE NOT NULL,
    nationality VARCHAR(50),
    primary_position_id INT NOT NULL,
    height_cm INT,
    weight_kg INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (primary_position_id) REFERENCES Positions(position_id) ON DELETE RESTRICT,
    INDEX idx_position (primary_position_id),
    INDEX idx_name (last_name, first_name)
);

-- ============================================================================
-- HISTORICAL & ASSOCIATION TABLES
-- ============================================================================

CREATE TABLE PlayerTeamHistory (
    player_team_history_id INT AUTO_INCREMENT PRIMARY KEY,
    player_id INT NOT NULL,
    team_id INT NOT NULL,
    season_id INT NOT NULL,
    jersey_number INT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    transfer_fee_millions DECIMAL(10, 2),
    contract_status VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE KEY unique_player_team_season (player_id, team_id, season_id),
    FOREIGN KEY (player_id) REFERENCES Players(player_id) ON DELETE CASCADE,
    FOREIGN KEY (team_id) REFERENCES Teams(team_id) ON DELETE CASCADE,
    FOREIGN KEY (season_id) REFERENCES Seasons(season_id) ON DELETE CASCADE,
    INDEX idx_player (player_id),
    INDEX idx_team (team_id),
    INDEX idx_season (season_id),
    CONSTRAINT check_jersey CHECK (jersey_number BETWEEN 1 AND 99)
);

-- ============================================================================
-- GAMES & MATCH DATA
-- ============================================================================

CREATE TABLE Games (
    game_id INT AUTO_INCREMENT PRIMARY KEY,
    season_id INT NOT NULL,
    home_team_id INT NOT NULL,
    away_team_id INT NOT NULL,
    venue_id INT NOT NULL,
    game_date DATE NOT NULL,
    game_time TIME,
    home_goals INT DEFAULT 0,
    away_goals INT DEFAULT 0,
    attendance INT,
    referee_name VARCHAR(100),
    weather_condition VARCHAR(50),
    status ENUM('Scheduled', 'In Progress', 'Completed', 'Cancelled') DEFAULT 'Scheduled',
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (season_id) REFERENCES Seasons(season_id) ON DELETE CASCADE,
    FOREIGN KEY (home_team_id) REFERENCES Teams(team_id) ON DELETE CASCADE,
    FOREIGN KEY (away_team_id) REFERENCES Teams(team_id) ON DELETE CASCADE,
    FOREIGN KEY (venue_id) REFERENCES Venues(venue_id) ON DELETE RESTRICT,
    INDEX idx_season (season_id),
    INDEX idx_date (game_date),
    INDEX idx_home_team (home_team_id),
    INDEX idx_away_team (away_team_id),
    CONSTRAINT check_different_teams CHECK (home_team_id != away_team_id),
    CONSTRAINT check_goals CHECK (home_goals >= 0 AND away_goals >= 0)
);

CREATE TABLE GameLineups (
    game_lineup_id INT AUTO_INCREMENT PRIMARY KEY,
    game_id INT NOT NULL,
    player_id INT NOT NULL,
    team_id INT NOT NULL,
    position_id INT NOT NULL,
    shirt_number INT NOT NULL,
    is_starter BOOLEAN DEFAULT TRUE,
    minutes_played INT DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE KEY unique_player_in_game (game_id, player_id, team_id),
    FOREIGN KEY (game_id) REFERENCES Games(game_id) ON DELETE CASCADE,
    FOREIGN KEY (player_id) REFERENCES Players(player_id) ON DELETE CASCADE,
    FOREIGN KEY (team_id) REFERENCES Teams(team_id) ON DELETE CASCADE,
    FOREIGN KEY (position_id) REFERENCES Positions(position_id) ON DELETE RESTRICT,
    INDEX idx_game (game_id),
    INDEX idx_player (player_id),
    INDEX idx_team (team_id),
    CONSTRAINT check_minutes CHECK (minutes_played BETWEEN 0 AND 120)
);

CREATE TABLE PlayerGameStats (
    game_stat_id INT AUTO_INCREMENT PRIMARY KEY,
    game_id INT NOT NULL,
    player_id INT NOT NULL,
    team_id INT NOT NULL,
    goals_scored INT DEFAULT 0,
    assists INT DEFAULT 0,
    shots_on_target INT DEFAULT 0,
    total_shots INT DEFAULT 0,
    passes_completed INT DEFAULT 0,
    total_passes INT DEFAULT 0,
    tackles INT DEFAULT 0,
    interceptions INT DEFAULT 0,
    fouls_committed INT DEFAULT 0,
    fouls_suffered INT DEFAULT 0,
    yellow_cards INT DEFAULT 0,
    red_cards INT DEFAULT 0,
    own_goals INT DEFAULT 0,
    distance_covered_km DECIMAL(5, 2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    UNIQUE KEY unique_player_game (game_id, player_id, team_id),
    FOREIGN KEY (game_id) REFERENCES Games(game_id) ON DELETE CASCADE,
    FOREIGN KEY (player_id) REFERENCES Players(player_id) ON DELETE CASCADE,
    FOREIGN KEY (team_id) REFERENCES Teams(team_id) ON DELETE CASCADE,
    INDEX idx_game (game_id),
    INDEX idx_player (player_id),
    INDEX idx_goals (goals_scored),
    CONSTRAINT check_stats CHECK (
        goals_scored >= 0 AND assists >= 0 AND 
        shots_on_target >= 0 AND total_shots >= 0 AND
        yellow_cards BETWEEN 0 AND 3 AND red_cards BETWEEN 0 AND 1
    )
);

-- ============================================================================
-- INDEXES FOR COMMON QUERIES
-- ============================================================================

CREATE INDEX idx_pth_player_season ON PlayerTeamHistory(player_id, season_id);
CREATE INDEX idx_game_date_season ON Games(game_date, season_id);
CREATE INDEX idx_pgs_player ON PlayerGameStats(player_id, goals_scored);

-- ============================================================================
-- VIEW: Team Win/Loss Records
-- ============================================================================

CREATE VIEW TeamStandings AS
SELECT 
    s.season_id,
    s.season_year,
    t.team_id,
    t.team_name,
    COUNT(CASE WHEN g.status = 'Completed' THEN 1 END) AS matches_played,
    COUNT(CASE WHEN g.status = 'Completed' AND g.home_team_id = t.team_id AND g.home_goals > g.away_goals THEN 1 END) +
    COUNT(CASE WHEN g.status = 'Completed' AND g.away_team_id = t.team_id AND g.away_goals > g.home_goals THEN 1 END) AS wins,
    COUNT(CASE WHEN g.status = 'Completed' AND g.home_goals = g.away_goals THEN 1 END) AS draws,
    COUNT(CASE WHEN g.status = 'Completed' AND g.home_team_id = t.team_id AND g.home_goals < g.away_goals THEN 1 END) +
    COUNT(CASE WHEN g.status = 'Completed' AND g.away_team_id = t.team_id AND g.away_goals < g.home_goals THEN 1 END) AS losses,
    SUM(CASE WHEN g.home_team_id = t.team_id THEN g.home_goals ELSE g.away_goals END) AS goals_for,
    SUM(CASE WHEN g.home_team_id = t.team_id THEN g.away_goals ELSE g.home_goals END) AS goals_against
FROM Seasons s
JOIN Teams t ON s.league_id = t.league_id
LEFT JOIN Games g ON s.season_id = g.season_id AND (g.home_team_id = t.team_id OR g.away_team_id = t.team_id)
GROUP BY s.season_id, s.season_year, t.team_id, t.team_name;

-- ============================================================================
-- VIEW: Top Scorers per Season
-- ============================================================================

CREATE VIEW TopScorers AS
SELECT 
    s.season_id,
    s.season_year,
    p.player_id,
    CONCAT(p.first_name, ' ', p.last_name) AS player_name,
    t.team_id,
    t.team_name,
    SUM(pgs.goals_scored) AS total_goals,
    COUNT(DISTINCT pgs.game_id) AS games_played
FROM Seasons s
JOIN Games g ON s.season_id = g.season_id
JOIN PlayerGameStats pgs ON g.game_id = pgs.game_id
JOIN Players p ON pgs.player_id = p.player_id
JOIN Teams t ON pgs.team_id = t.team_id
WHERE g.status = 'Completed'
GROUP BY s.season_id, s.season_year, p.player_id, t.team_id, t.team_name;
