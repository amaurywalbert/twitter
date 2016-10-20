-- MySQL Script generated by MySQL Workbench
-- Qua 19 Out 2016 22:01:22 BRST
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema twitter
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema twitter
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `twitter` DEFAULT CHARACTER SET utf8 ;
USE `twitter` ;

-- -----------------------------------------------------
-- Table `twitter`.`USER`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `twitter`.`USER` (
  `user_iduser` BIGINT NOT NULL,
  `user_created_at` VARCHAR(45) NULL,
  `user_description` LONGBLOB NULL,
  `user_favourites_count` INT NULL,
  `user_followers_count` INT NULL,
  `user_following` VARCHAR(45) NULL,
  `user_friends_count` INT NULL,
  `user_geo_enabled` VARCHAR(45) NULL,
  `user_lang` VARCHAR(45) NULL,
  `user_listed_count` INT NULL,
  `user_location` VARCHAR(45) NULL,
  `user_name` LONGBLOB NULL,
  `user_profile_image_url` VARCHAR(255) NULL,
  `user_screen_name` VARCHAR(45) NULL,
  `user_statuses_count` INT NULL,
  `user_time_zone` VARCHAR(45) NULL,
  `user_url` VARCHAR(255) NULL,
  PRIMARY KEY (`user_iduser`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `twitter`.`REGION`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `twitter`.`REGION` (
  `region_idregion` INT NOT NULL AUTO_INCREMENT,
  `region_description` VARCHAR(45) NULL,
  `region_latitude_in` VARCHAR(45) NULL,
  `region_longitude_in` VARCHAR(45) NULL,
  `region_latitude_end` VARCHAR(45) NULL,
  `region_longitude_end` VARCHAR(45) NULL,
  PRIMARY KEY (`region_idregion`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `twitter`.`TWEET`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `twitter`.`TWEET` (
  `tweet_idtweet` BIGINT NOT NULL,
  `tweet_contributors` VARCHAR(255) NULL,
  `tweet_geo_latitude` VARCHAR(45) NULL,
  `tweet_geo_longitude` VARCHAR(45) NULL,
  `tweet_created_at` VARCHAR(45) NULL,
  `favorite_count` INT NULL,
  `tweet_favorited` VARCHAR(45) NULL,
  `tweet_filter_level` VARCHAR(45) NULL,
  `tweet_in_reply_to_status_id` VARCHAR(255) NULL,
  `tweet_in_reply_to_user_id` VARCHAR(255) NULL,
  `tweet_is_quote_status` VARCHAR(45) NULL,
  `tweet_lang` VARCHAR(45) NULL,
  `tweet_retweet_count` INT NULL,
  `tweet_retweeted` VARCHAR(45) NULL,
  `tweet_source` VARCHAR(255) NULL,
  `tweet_text` LONGBLOB NULL,
  `tweet_timestamp_ms` VARCHAR(45) NULL,
  `tweet_truncated` VARCHAR(45) NULL,
  `tweet_timestamp_db` TIMESTAMP NOT NULL,
  `tweet_iduser_fk` BIGINT NOT NULL,
  `tweet_idregion_fk` INT NOT NULL,
  PRIMARY KEY (`tweet_idtweet`),
  INDEX `fk_TWEET_1_idx` (`tweet_iduser_fk` ASC),
  INDEX `fk_TWEET_2_idx` (`tweet_idregion_fk` ASC),
  CONSTRAINT `fk_TWEET_1`
    FOREIGN KEY (`tweet_iduser_fk`)
    REFERENCES `twitter`.`USER` (`user_iduser`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_TWEET_2`
    FOREIGN KEY (`tweet_idregion_fk`)
    REFERENCES `twitter`.`REGION` (`region_idregion`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `twitter`.`PLACE`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `twitter`.`PLACE` (
  `place_idplace` BIGINT NOT NULL AUTO_INCREMENT,
  `place_idtweet_fk` BIGINT NOT NULL,
  `place_bounding_box` VARCHAR(255) NULL,
  `place_country` VARCHAR(45) NULL,
  `place_country_code` VARCHAR(45) NULL,
  `place_full_name` VARCHAR(100) NULL,
  `place_id_place` VARCHAR(45) NULL,
  `place_name` VARCHAR(45) NULL,
  `place_place_type` VARCHAR(45) NULL,
  `place_url` VARCHAR(255) NULL,
  PRIMARY KEY (`place_idplace`),
  INDEX `fk_PLACE_1_idx` (`place_idtweet_fk` ASC),
  CONSTRAINT `fk_PLACE_1`
    FOREIGN KEY (`place_idtweet_fk`)
    REFERENCES `twitter`.`TWEET` (`tweet_idtweet`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `twitter`.`ENTITIES`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `twitter`.`ENTITIES` (
  `entities_identities` BIGINT NOT NULL AUTO_INCREMENT,
  `entities_idtweet_fk` BIGINT NOT NULL,
  `entities_hashtags` LONGBLOB NULL,
  `entities_symbols` LONGBLOB NULL,
  `entities_urls` LONGBLOB NULL,
  `entities_user_mentions` LONGBLOB NULL,
  PRIMARY KEY (`entities_identities`),
  INDEX `fk_ENTITIES_1_idx` (`entities_idtweet_fk` ASC),
  CONSTRAINT `fk_ENTITIES_1`
    FOREIGN KEY (`entities_idtweet_fk`)
    REFERENCES `twitter`.`TWEET` (`tweet_idtweet`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
