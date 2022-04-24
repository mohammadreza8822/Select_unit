# CREATE TABLE `entekhab_vahed`.`lesson` (
#   `ID` INT NOT NULL,
#   `name` NVARCHAR(45) NOT NULL,
#   `book` NVARCHAR(45) NULL,
#   `day/hour` DATETIME NULL,
#   `lessoncode` INT NOT NULL AUTO_INCREMENT,
#   PRIMARY KEY (`ID`),
#   UNIQUE INDEX `lesson_code_UNIQUE` (`ID` ASC) VISIBLE,
#   UNIQUE INDEX `lessoncode_UNIQUE` (`lessoncode` ASC) VISIBLE);