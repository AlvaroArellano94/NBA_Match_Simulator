USE NBA_Match_Simulator;
--Memphis starter team
INSERT INTO dbo.Players VALUES ('J. Jackson Jr.',4, 3, 0.83, 0.51, 0.39);
INSERT INTO dbo.Players VALUES ('D. Brooks', 3, 2, 0.85, 0.45, 0.40);
INSERT INTO dbo.Players VALUES ('S. Adams', 5, 1, 0.75, 0.52, 0.15);
INSERT INTO dbo.Players VALUES ('J. Morant', 1, 3, 0.88, 0.50, 0.38);
INSERT INTO dbo.Players VALUES ('D. Bane', 2, 3, 0.85, 0.40, 0.43);
--Memphis bench
INSERT INTO dbo.Players VALUES ('T. Jones',1, 1, 0.76, 0.32, 0.35);
INSERT INTO dbo.Players VALUES ('Z. Williams', 2, 2, 0.89, 0.42, 0.38);
INSERT INTO dbo.Players VALUES ('K. Anderson', 3, 2, 0.90, 0.40, 0.39);
INSERT INTO dbo.Players VALUES ('B. Clarke', 4, 2,0.82, 0.45, 0.30);
INSERT INTO dbo.Players VALUES ('X. Tillman', 5, 1, 0.70, 0.43, 0.25);

--Minnesota starter team
INSERT INTO dbo.Players VALUES ("J. Vanderbilt", 4, 1, 0.75, 0.38, 0.37)
INSERT INTO dbo.Players VALUES ("A. Edwards", 3, 3, 0.84, 0.48, 0.36)
INSERT INTO dbo.Players VALUES ("K. Towns", 5, 3, 0.90, 0.55, 0.42)
INSERT INTO dbo.Players VALUES ("P. Beverly", 2, 2, 0.81, 0.41, 0.35)
INSERT INTO dbo.Players VALUES ("D. Russell", 1, 3, 0.89, 0.46, 0.39)
--Minnesota starter team
INSERT INTO dbo.Players VALUES ("J. McLaughlin", 1, 1, 0.79, 0.33, 0.30)
INSERT INTO dbo.Players VALUES ("M. Beasley", 2, 2, 0.88, 0.36, 0.41)
INSERT INTO dbo.Players VALUES ("J. McDaniels", 3, 2, 0.88, 0.35, 0.40)
INSERT INTO dbo.Players VALUES ("T. Prince", 4, 1, 0.76, 0.39, 0.30)
INSERT INTO dbo.Players VALUES ("N. Reid", 5, 1, 0.72, 0.42, 0.28)

--create Teams
INSERT INTO dbo.Teams VALUES ('Memphis Grizzlies', 'WEST')
INSERT INTO dbo.Teams VALUES ('Minnesota Timberwolves', 'WEST')
