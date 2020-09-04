-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema google_crawler
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema google_crawler
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `google_crawler` DEFAULT CHARACTER SET utf8 ;
USE `google_crawler` ;

-- -----------------------------------------------------
-- Table `mydb`.`URL_Chek`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `google_crawler`.`URL_Chek` (
  `id_url` INT NOT NULL AUTO_INCREMENT,
  `URL` TEXT NOT NULL,
  `Flag` INT(1) NOT NULL DEFAULT 0,
  PRIMARY KEY (`id_url`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `google_crawler`.`Page`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `google_crawler`.`Page` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(255) NOT NULL,
  `snippet` VARCHAR(360) NOT NULL,
  `full_text` TEXT NULL,
  `URL_Chek_id_url` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_Page_URL_Chek_idx` (`URL_Chek_id_url` ASC),
  CONSTRAINT `fk_Page_URL_Chek`
    FOREIGN KEY (`URL_Chek_id_url`)
    REFERENCES `google_crawler`.`URL_Chek` (`id_url`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
