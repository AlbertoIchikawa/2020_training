-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema theuniversitydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema theuniversitydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `theuniversitydb` DEFAULT CHARACTER SET utf8 ;
SHOW WARNINGS;
USE `theuniversitydb` ;

-- -----------------------------------------------------
-- Table `theuniversitydb`.`program`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `theuniversitydb`.`program` (
  `program_id` INT NOT NULL AUTO_INCREMENT,
  `program_name` VARCHAR(50) NOT NULL,
  `total_credit_points` INT NOT NULL,
  `year_commenced` INT NOT NULL,
  `semeter_year` INT NOT NULL,
  UNIQUE INDEX `program_name_UNIQUE` (`program_name` ASC),
  PRIMARY KEY (`program_id`))
ENGINE = InnoDB;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `theuniversitydb`.`student`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `theuniversitydb`.`student` (
  `student_id` INT NOT NULL AUTO_INCREMENT,
  `given_name` VARCHAR(50) NOT NULL,
  `surname` VARCHAR(50) NOT NULL,
  `birthday` DATE NOT NULL,
  `year_first_enrolled` INT NOT NULL,
  `program_program_id` INT NOT NULL,
  PRIMARY KEY (`student_id`),
  INDEX `fk_student_program1_idx` (`program_program_id` ASC),
  CONSTRAINT `fk_student_program1`
    FOREIGN KEY (`program_program_id`)
    REFERENCES `theuniversitydb`.`program` (`program_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `theuniversitydb`.`course`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `theuniversitydb`.`course` (
  `course_id` INT NOT NULL AUTO_INCREMENT,
  `course_name` VARCHAR(50) NOT NULL,
  `credit_point` INT NOT NULL,
  `year_commenced` INT NOT NULL,
  PRIMARY KEY (`course_id`),
  UNIQUE INDEX `course_name_UNIQUE` (`course_name` ASC))
ENGINE = InnoDB;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `theuniversitydb`.`student_grade`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `theuniversitydb`.`student_grade` (
  `student_student_id` INT NOT NULL,
  `course_course_id` INT NOT NULL,
  `grade_course` VARCHAR(5) NOT NULL,
  `mark_course` VARCHAR(5) NOT NULL,
  INDEX `fk_student_grade_student1_idx` (`student_student_id` ASC),
  INDEX `fk_student_grade_course1_idx` (`course_course_id` ASC),
  PRIMARY KEY (`student_student_id`, `course_course_id`),
  CONSTRAINT `fk_student_grade_student1`
    FOREIGN KEY (`student_student_id`)
    REFERENCES `theuniversitydb`.`student` (`student_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_student_grade_course1`
    FOREIGN KEY (`course_course_id`)
    REFERENCES `theuniversitydb`.`course` (`course_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

SHOW WARNINGS;



-- -----------------------------------------------------
-- Table `theuniversitydb`.`semester`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `theuniversitydb`.`semester` (
  `year` INT NULL,
  `semester` VARCHAR(50) NULL,
  `program_program_id` INT NOT NULL,
  `course_course_id` INT NOT NULL,
  INDEX `fk_semester_program1_idx` (`program_program_id` ASC),
  INDEX `fk_semester_course1_idx` (`course_course_id` ASC),
  PRIMARY KEY (`program_program_id`, `course_course_id`),
  CONSTRAINT `fk_semester_program1`
    FOREIGN KEY (`program_program_id`)
    REFERENCES `theuniversitydb`.`program` (`program_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_semester_course1`
    FOREIGN KEY (`course_course_id`)
    REFERENCES `theuniversitydb`.`course` (`course_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

SHOW WARNINGS;
USE `theuniversitydb` ;

-- -----------------------------------------------------
-- Placeholder table for view `theuniversitydb`.`view1`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `theuniversitydb`.`view1` (`id` INT);
SHOW WARNINGS;

-- -----------------------------------------------------
-- View `theuniversitydb`.`view1`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `theuniversitydb`.`view1`;
SHOW WARNINGS;
USE `theuniversitydb`;

SHOW WARNINGS;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
