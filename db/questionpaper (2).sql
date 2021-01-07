-- phpMyAdmin SQL Dump
-- version 3.3.9
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Jan 03, 2021 at 05:41 AM
-- Server version: 5.5.8
-- PHP Version: 5.3.5

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `questionpaper`
--

-- --------------------------------------------------------

--
-- Table structure for table `alocation_info`
--

CREATE TABLE IF NOT EXISTS `alocation_info` (
  `alocation_id` int(50) NOT NULL AUTO_INCREMENT,
  `packet_id` varchar(50) NOT NULL,
  `subject_id` varchar(50) NOT NULL,
  `faculty_id` varchar(50) NOT NULL,
  `noofpapers` varchar(50) NOT NULL,
  PRIMARY KEY (`alocation_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=7 ;

--
-- Dumping data for table `alocation_info`
--

INSERT INTO `alocation_info` (`alocation_id`, `packet_id`, `subject_id`, `faculty_id`, `noofpapers`) VALUES
(5, 'AQU11', '5', '2', ''),
(6, 'NonePQR-125', '2', '1', '');

-- --------------------------------------------------------

--
-- Table structure for table `alocation_info1`
--

CREATE TABLE IF NOT EXISTS `alocation_info1` (
  `alocation_id` int(50) NOT NULL AUTO_INCREMENT,
  `packet_id` varchar(50) NOT NULL,
  `subject_id` varchar(50) NOT NULL,
  `faculty_id` varchar(50) NOT NULL,
  `noofpapers` varchar(50) NOT NULL,
  PRIMARY KEY (`alocation_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `alocation_info1`
--


-- --------------------------------------------------------

--
-- Table structure for table `alocation_info2`
--

CREATE TABLE IF NOT EXISTS `alocation_info2` (
  `alocation_id` int(50) NOT NULL AUTO_INCREMENT,
  `packet_id` varchar(50) NOT NULL,
  `subject_id` varchar(50) NOT NULL,
  `faculty_id` varchar(50) NOT NULL,
  `noofpapers` varchar(50) NOT NULL,
  PRIMARY KEY (`alocation_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `alocation_info2`
--


-- --------------------------------------------------------

--
-- Table structure for table `college_info`
--

CREATE TABLE IF NOT EXISTS `college_info` (
  `college_id` int(11) NOT NULL AUTO_INCREMENT,
  `college_name` varchar(50) NOT NULL,
  PRIMARY KEY (`college_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `college_info`
--

INSERT INTO `college_info` (`college_id`, `college_name`) VALUES
(2, 'MES');

-- --------------------------------------------------------

--
-- Table structure for table `faculty_info`
--

CREATE TABLE IF NOT EXISTS `faculty_info` (
  `faculty_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `college` varchar(50) NOT NULL,
  `Mail_id` varchar(50) NOT NULL,
  `Phone_No` varchar(50) NOT NULL,
  `Subject_Id` varchar(50) NOT NULL,
  `Semester` varchar(50) NOT NULL,
  PRIMARY KEY (`faculty_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `faculty_info`
--

INSERT INTO `faculty_info` (`faculty_id`, `name`, `college`, `Mail_id`, `Phone_No`, `Subject_Id`, `Semester`) VALUES
(1, 'manu', 'Ma', 'manu@gmail.com', '9985457587', '2', '0'),
(2, 'aneeja', 'MES', 'aneeja@gmail.com', '997458548', '5', 'sem2');

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE IF NOT EXISTS `login` (
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`username`, `password`) VALUES
('admin', 'admin');

-- --------------------------------------------------------

--
-- Table structure for table `packet_info`
--

CREATE TABLE IF NOT EXISTS `packet_info` (
  `packet_id` varchar(50) NOT NULL,
  `semester` varchar(50) NOT NULL,
  `subject_id` int(11) NOT NULL,
  `noofpaper` int(11) NOT NULL,
  PRIMARY KEY (`packet_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `packet_info`
--

INSERT INTO `packet_info` (`packet_id`, `semester`, `subject_id`, `noofpaper`) VALUES
('AQU11', 'Sem1', 5, 15),
('NonePQR-125', 'Sem1', 2, 25);

-- --------------------------------------------------------

--
-- Table structure for table `serious`
--

CREATE TABLE IF NOT EXISTS `serious` (
  `sid` int(11) NOT NULL AUTO_INCREMENT,
  `sem` varchar(50) NOT NULL,
  `Serious` varchar(50) NOT NULL,
  PRIMARY KEY (`sid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `serious`
--

INSERT INTO `serious` (`sid`, `sem`, `Serious`) VALUES
(2, 'Sem1', 'ABC'),
(3, 'Sem1', 'PQR');

-- --------------------------------------------------------

--
-- Table structure for table `subject_info`
--

CREATE TABLE IF NOT EXISTS `subject_info` (
  `subject_id` int(11) NOT NULL AUTO_INCREMENT,
  `subject_name` varchar(50) NOT NULL,
  `semester` varchar(50) NOT NULL,
  PRIMARY KEY (`subject_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=6 ;

--
-- Dumping data for table `subject_info`
--

INSERT INTO `subject_info` (`subject_id`, `subject_name`, `semester`) VALUES
(2, 'Physics', 'sem1'),
(5, 'C programing', 'sem2');
