# CREATE TABLE `entekhab_vahed`.`student` (
#   `ID` INT NOT NULL,
#   `name` NVARCHAR(45) NOT NULL,
#   `family` NVARCHAR(45) NOT NULL,
#   `studentcode` INT NOT NULL AUTO_INCREMENT,
#   `role` INT NULL,
#   UNIQUE INDEX `ID_UNIQUE` (`ID` ASC) VISIBLE,
#   UNIQUE INDEX `studentcode_UNIQUE` (`studentcode` ASC) VISIBLE);