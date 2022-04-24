# CREATE TABLE `entekhab_vahed`.`selection_process` (
#   `lesson_code` INT NOT NULL,
#   `student_code` INT NOT NULL,
#   `date_process` DATETIME NULL,
#   PRIMARY KEY (`lesson_code`, `student_code`),
#   UNIQUE INDEX `lesson_code_UNIQUE` (`lesson_code` ASC) VISIBLE,
#   UNIQUE INDEX `student_code_UNIQUE` (`student_code` ASC) VISIBLE)
# ENGINE = InnoDB
# DEFAULT CHARACTER SET = utf8mb4;CREATE