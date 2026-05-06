# Sports League Database — Design Document

## Scope
A **soccer league management system** tracking teams, players, games, and match statistics across multiple seasons.

## Entities & Relationships

### Core Tables

1. **Leagues** — League/division metadata
   - `league_id` (PK)
   - `league_name` (e.g., "Premier League", "Division 2")
   - `country`, `founded_year`

2. **Seasons** — Seasons within a league (2023-24, 2024-25, etc.)
   - `season_id` (PK)
   - `league_id` (FK → Leagues)
   - `season_year` (e.g., "2023-24")
   - `start_date`, `end_date`

3. **Venues** — Stadiums/fields
   - `venue_id` (PK)
   - `venue_name`, `city`, `capacity`, `country`

4. **Coaches** — Team coaches
   - `coach_id` (PK)
   - `first_name`, `last_name`, `dob`, `nationality`

5. **Teams** — Teams in league(s)
   - `team_id` (PK)
   - `team_name`, `founded_year`
   - `home_venue_id` (FK → Venues)
   - `league_id` (FK → Leagues)
   - `manager_coach_id` (FK → Coaches)

6. **Positions** — Player positions (Goalkeeper, Defender, Midfielder, Forward, etc.)
   - `position_id` (PK)
   - `position_name`
   - `position_abbreviation` (e.g., "GK", "DF", "MF", "FW")

7. **Players** — Player master data
   - `player_id` (PK)
   - `first_name`, `last_name`, `dob`, `nationality`
   - `primary_position_id` (FK → Positions)
   - `height_cm`, `weight_kg`

8. **PlayerTeamHistory** — Track player transfers across teams/seasons
   - `player_team_history_id` (PK)
   - `player_id` (FK → Players)
   - `team_id` (FK → Teams)
   - `season_id` (FK → Seasons)
   - `jersey_number`, `start_date`, `end_date`
   - *UNIQUE(player_id, team_id, season_id)*

9. **Games** — Individual matches
   - `game_id` (PK)
   - `season_id` (FK → Seasons)
   - `home_team_id` (FK → Teams)
   - `away_team_id` (FK → Teams)
   - `venue_id` (FK → Venues)
   - `game_date`, `game_time`
   - `home_goals`, `away_goals`
   - `attendance`, `referee_name`
   - `status` (Scheduled, Completed, Cancelled)

10. **GameLineups** — Who played in each game
    - `game_lineup_id` (PK)
    - `game_id` (FK → Games)
    - `player_id` (FK → Players)
    - `team_id` (FK → Teams)
    - `shirt_number`, `position_id` (FK → Positions)
    - `is_starter` (yes/no)
    - `minutes_played`
    - *UNIQUE(game_id, player_id, team_id)*

11. **PlayerGameStats** — Per-game performance metrics
    - `game_stat_id` (PK)
    - `game_id` (FK → Games)
    - `player_id` (FK → Players)
    - `team_id` (FK → Teams)
    - `goals_scored`, `assists`, `shots_on_target`, `passes_completed`
    - `tackles`, `interceptions`, `fouls_committed`, `fouls_suffered`
    - `yellow_cards`, `red_cards`
    - `own_goals`
    - *UNIQUE(game_id, player_id, team_id)*

## Normalization

- **BCNF/3NF**: All attributes are functionally dependent on primary keys only
- **No transitive dependencies**: Position attributes stay in Positions table
- **No partial dependencies**: Game-specific coach info not stored (could query via team)
- **Referential integrity**: All FKs properly defined with CASCADE deletes where appropriate

## Key Constraints

- Teams cannot play themselves
- Game goals and player stats should only be entered after game is completed
- Player cannot have multiple active entries in PlayerTeamHistory for same season
- Jersey number unique per team per season

## Example Queries

1. Top scorers in a season
2. Team win/loss/draw records
3. Player transfer history
4. Head-to-head team statistics
5. Average team possession by position
