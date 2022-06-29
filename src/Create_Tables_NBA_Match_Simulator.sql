USE NBA_Match_Simulator
--In order to be able to drop the tables is important the order 
--(dropping children tables first) 
DROP TABLE IF EXISTS Player_Stats_Match;
DROP TABLE IF EXISTS Player_Actions_Match;
DROP TABLE IF EXISTS Players;
DROP TABLE IF EXISTS Teams;
DROP TABLE IF EXISTS Match;
DROP TABLE IF EXISTS Rosters;

CREATE TABLE Players (
    Id_Player int IDENTITY(1,1) PRIMARY KEY,
    Player_Name varchar(255) NOT NULL,
    Position int,
    Offense_Participation int,
    Fga_1_Average float,
    Fga_2_Average float,
    Fga_3_Average float
);

CREATE TABLE Teams (
    Id_Team int IDENTITY(1,1) PRIMARY KEY,
    Team_Name varchar(255) NOT NULL,
    Team_Conference varchar(255)
);


CREATE TABLE Rosters (
    Id_Team int,
    Id_Player int,
    CONSTRAINT PK_Rosters PRIMARY KEY(Id_Team, Id_Player)
);


--it needs to be implemented in the python app
CREATE TABLE Match (
    Id_Match int IDENTITY(1,1) PRIMARY KEY,
    Id_Team_Local int,
    Id_Team_Abroad int,
    Start_Time smalldatetime,
    End_Time smalldatetime,
    Winner_Team_Id int
);

--This table is created as a "log" of what's happening in the match, but it is not inserted into the model
--This table for this stage is not working yet
/*
CREATE TABLE Player_Actions_Match (
    Id_Match int NOT NULL,
    Id_Player int,
    Action_Time int,
    Action_Name varchar(255),
    CONSTRAINT PK_Player_Actions_Match PRIMARY KEY(Id_Match, Id_Player, Action_Time)
);
*/

CREATE TABLE Player_Stats_Match (
    Id_Match int NOT NULL,
    Id_Player int,
    Id_Team int,
    Attempt_1 int,
    Attempt_1_Made int,
    Attempt_2 int,
    Attempt_2_Made int,
    Attempt_3 int,
    Attempt_3_Made int,  
    Points_Made int,
    Rebounds_Made int,
    Assists_Made int,
    Steals_Made int,
    Blocks_Made int,
    Turnovers_Made int,
    Fouls_Made int,
    Fouled_Out int,
    On_Court bit,  --bit datatype is used because in sql server there is not boolean data type
    Seconds_Played int,
    CONSTRAINT FK_Id_Match FOREIGN KEY (Id_Match) REFERENCES Match(Id_Match),
    CONSTRAINT FK_Id_Player FOREIGN KEY (Id_Player) REFERENCES Players(Id_Player),
    CONSTRAINT FK_Id_Team FOREIGN KEY (Id_Team) REFERENCES Teams(Id_Team),
    CONSTRAINT FK_Roster FOREIGN KEY (Id_Team, Id_Player) REFERENCES Rosters(Id_Team, Id_Player),
    CONSTRAINT PK_Player_Stats_Match PRIMARY KEY(Id_Match, Id_Player)
);