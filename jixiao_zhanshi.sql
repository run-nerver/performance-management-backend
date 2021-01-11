/*
 Navicat Premium Data Transfer

 Source Server         : 阿里云6个月
 Source Server Type    : MySQL
 Source Server Version : 50725
 Source Host           : rm-2ze9c7bp86pc6m9qd3o.mysql.rds.aliyuncs.com
 Source Database       : jixiao_zhanshi

 Target Server Type    : MySQL
 Target Server Version : 50725
 File Encoding         : utf-8

 Date: 01/11/2021 00:56:32 AM
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `alembic_version`
-- ----------------------------
DROP TABLE IF EXISTS `alembic_version`;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
--  Records of `alembic_version`
-- ----------------------------
BEGIN;
INSERT INTO `alembic_version` VALUES ('2639724a299a');
COMMIT;

-- ----------------------------
--  Table structure for `counselorsworkload`
-- ----------------------------
DROP TABLE IF EXISTS `counselorsworkload`;
CREATE TABLE `counselorsworkload` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `total_people` int(11) DEFAULT NULL,
  `beyond_workload_people` int(11) DEFAULT NULL,
  `months` int(11) DEFAULT NULL,
  `counselors_beyond_workload` decimal(20,2) DEFAULT NULL,
  `counselors_beyond_workload_score` decimal(20,2) DEFAULT NULL,
  `total_money` decimal(20,2) DEFAULT NULL,
  `year` varchar(4) DEFAULT NULL,
  `notes` text,
  `user_id` int(11) DEFAULT NULL,
  `students_money` decimal(20,2) DEFAULT NULL,
  `counselors_beyond_workload_money` decimal(20,2) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `counselorsworkload_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=82 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
--  Records of `counselorsworkload`
-- ----------------------------
BEGIN;
INSERT INTO `counselorsworkload` VALUES ('71', '490', '290', '7', '169.17', '84.58', '10920.60', '2020', null, '755', '5000.00', '5920.60'), ('72', '131', '0', '11', '0.00', '0.00', '5001.00', '2020', null, '756', '5001.00', '0.00'), ('73', '621', '221', '11', '110.67', '55.33', '8875.10', '2020', null, '757', '5002.00', '3873.10'), ('74', '824', '287', '11', '60.58', '30.29', '7123.30', '2020', null, '758', '5003.00', '2120.30'), ('75', '179', '0', '11', '0.00', '0.00', '5004.00', '2020', null, '759', '5004.00', '0.00'), ('76', '999', '599', '12', '244.92', '122.46', '13577.20', '2020', null, '760', '5005.00', '8572.20'), ('77', '647', '247', '12', '76.75', '38.38', '7692.60', '2020', null, '761', '5006.00', '2686.60'), ('78', '874', '474', '8', '181.83', '90.92', '11371.40', '2020', null, '762', '5007.00', '6364.40'), ('79', '969', '569', '11', '233.08', '116.54', '13165.80', '2020', null, '763', '5008.00', '8157.80'), ('80', '1008', '608', '11', '263.25', '131.63', '14222.40', '2020', null, '764', '5009.00', '9213.40'), ('81', '2217', '1440', '12', '405.00', '202.50', '19185.00', '2020', null, '765', '5010.00', '14175.00');
COMMIT;

-- ----------------------------
--  Table structure for `information`
-- ----------------------------
DROP TABLE IF EXISTS `information`;
CREATE TABLE `information` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(60) DEFAULT NULL,
  `pic_name` varchar(120) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `timestamp` datetime DEFAULT NULL,
  `type` varchar(10) DEFAULT NULL,
  `rule_id` int(11) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `score` decimal(20,2) DEFAULT NULL,
  `filesUrl` varchar(1024) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `rule_id` (`rule_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `information_ibfk_1` FOREIGN KEY (`rule_id`) REFERENCES `rules` (`id`),
  CONSTRAINT `information_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=88 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
--  Table structure for `othersworkload`
-- ----------------------------
DROP TABLE IF EXISTS `othersworkload`;
CREATE TABLE `othersworkload` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `attendances` decimal(20,2) DEFAULT NULL,
  `union_activities` decimal(20,2) DEFAULT NULL,
  `ideological` decimal(20,2) DEFAULT NULL,
  `news` decimal(20,2) DEFAULT NULL,
  `counselors` decimal(20,2) DEFAULT NULL,
  `characteristics_activities` decimal(20,2) DEFAULT NULL,
  `mini_professional` decimal(20,2) DEFAULT NULL,
  `information` decimal(20,2) DEFAULT NULL,
  `undergraduatecolleges` decimal(20,2) DEFAULT NULL,
  `graduation_design_manage` decimal(20,2) DEFAULT NULL,
  `course_quality` decimal(20,2) DEFAULT NULL,
  `organization` decimal(20,2) DEFAULT NULL,
  `graduation_design_personal` decimal(20,2) DEFAULT NULL,
  `professional_tab` decimal(20,2) DEFAULT NULL,
  `mentor` decimal(20,2) DEFAULT NULL,
  `discipline_competition` decimal(20,2) DEFAULT NULL,
  `teaching_watch` decimal(20,2) DEFAULT NULL,
  `competition_judges` decimal(20,2) DEFAULT NULL,
  `union_work` decimal(20,2) DEFAULT NULL,
  `extra_score` decimal(20,2) DEFAULT NULL,
  `total_score` decimal(20,2) DEFAULT NULL,
  `total_money` decimal(20,2) DEFAULT NULL,
  `year` varchar(4) DEFAULT NULL,
  `notes` text,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `othersworkload_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=100 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
--  Records of `othersworkload`
-- ----------------------------
BEGIN;
INSERT INTO `othersworkload` VALUES ('90', '10.00', '6.30', '2.00', '0.00', '0.00', '0.00', '2.00', '0.00', '0.00', '0.00', '2.30', '4.00', '3.50', '3.00', '3.50', '2.00', '0.00', '1.11', '2.65', '0.00', '42.36', '2965.20', '2020', null, '755'), ('91', '8.00', '7.30', '0.00', '0.00', '0.00', '3.00', '0.00', '1.00', '0.00', '1.00', '0.00', '3.00', '2.00', '2.00', '5.60', '0.00', '3.00', '0.00', '0.00', '6.12', '42.02', '2941.40', '2020', null, '756'), ('92', '9.00', '8.30', '0.00', '3.00', '3.00', '0.00', '0.00', '0.00', '3.00', '0.00', '1.00', '4.00', '3.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '34.30', '2401.00', '2020', null, '757'), ('93', '10.00', '9.30', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '2.00', '2.00', '0.00', '1.00', '5.00', '3.00', '0.00', '1.00', '3.00', '5.60', '5.32', '0.00', '47.22', '3305.40', '2020', null, '758'), ('94', '11.00', '10.30', '0.00', '0.00', '0.00', '0.00', '0.00', '1.00', '1.00', '0.00', '0.00', '6.00', '4.00', '0.00', '2.00', '0.00', '0.00', '0.00', '0.00', '0.00', '35.30', '2471.00', '2020', null, '759'), ('95', '12.00', '11.30', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '1.00', '5.00', '0.00', '2.60', '0.00', '0.00', '0.00', '3.35', '8.69', '0.00', '43.94', '3075.80', '2020', null, '760'), ('96', '13.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '3.00', '0.00', '0.00', '1.00', '0.00', '0.00', '0.00', '2.00', '0.00', '0.00', '0.00', '19.00', '1330.00', '2020', null, '761'), ('97', '14.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '5.00', '0.00', '4.00', '0.00', '0.00', '0.00', '3.00', '0.00', '0.00', '0.00', '0.00', '0.00', '26.00', '1820.00', '2020', null, '762'), ('98', '15.00', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00', '4.70', '0.00', '3.60', '0.00', '1.00', '0.00', '0.00', '0.00', '1.00', '0.00', '0.00', '0.00', '0.00', '25.30', '1771.00', '2020', null, '763'), ('99', '8.00', '1.00', '2.00', '0.00', '0.00', '0.00', '5.90', '0.00', '0.00', '0.00', '0.00', '0.00', '1.00', '0.00', '0.00', '2.00', '0.00', '0.00', '3.89', '1.00', '24.79', '1735.30', '2020', null, '764');
COMMIT;

-- ----------------------------
--  Table structure for `rules`
-- ----------------------------
DROP TABLE IF EXISTS `rules`;
CREATE TABLE `rules` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `workload_name` varchar(120) NOT NULL,
  `key_name` varchar(20) DEFAULT NULL,
  `score` decimal(20,2) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `workload_name` (`workload_name`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
--  Records of `rules`
-- ----------------------------
BEGIN;
INSERT INTO `rules` VALUES ('2', '学生', '学生', '1.50'), ('3', '核心期刊', '核心期刊', '1.10'), ('23', '辅导员', '辅导员', '1.00');
COMMIT;

-- ----------------------------
--  Table structure for `scientificworkload`
-- ----------------------------
DROP TABLE IF EXISTS `scientificworkload`;
CREATE TABLE `scientificworkload` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `scientific_name` varchar(128) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `scientific_type` varchar(64) DEFAULT NULL,
  `scientific_money` decimal(20,2) DEFAULT NULL,
  `year` varchar(4) DEFAULT NULL,
  `notes` text,
  `confirm_status` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `scientificworkload_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
--  Records of `scientificworkload`
-- ----------------------------
BEGIN;
INSERT INTO `scientificworkload` VALUES ('37', '本科高校课程思政生态体系实践', '755', '科研项目', '10000.00', '2020', null, null), ('38', 'Intelligent analysis of medical ', '756', 'SCI', '20000.00', '2020', null, null), ('39', 'Design and Analysis of Distributed Computer Network Monitoring ', '757', 'SCI', '10000.00', '2020', null, null), ('40', 'Coal mine resource ', '758', 'EI', '5000.00', '2020', null, null), ('41', '基于多目标决策的时间序列数据', '759', '全国中文核心期刊研究论文', '1000.00', '2020', null, null), ('42', '大数据下监控网络混合入侵信息检索', '760', '全国中文核心期刊研究论文', '1000.00', '2020', null, null), ('43', '光纤网络离群恶意数据自动检测研究', '761', '全国中文核心期刊研究论文', '1000.00', '2020', null, null), ('44', 'SVD域的水印置乱新研究', '762', '全国中文核心期刊研究论文', '1000.00', '2020', null, null);
COMMIT;

-- ----------------------------
--  Table structure for `settings`
-- ----------------------------
DROP TABLE IF EXISTS `settings`;
CREATE TABLE `settings` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) DEFAULT NULL,
  `coefficient` decimal(20,2) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
--  Records of `settings`
-- ----------------------------
BEGIN;
INSERT INTO `settings` VALUES ('3', '正高', '1.36'), ('4', '副高', '1.15'), ('5', '中级', '1.00'), ('6', '初级', '0.79'), ('7', '正处级', '1.30'), ('8', '副处级', '1.15'), ('9', '正科级', '1.00'), ('10', '副科级', '1.00'), ('11', '员级', '0.79'), ('12', '工作量金额', '70.00'), ('13', '无', '0.00'), ('14', '教学合格工作量', '280.00'), ('15', '教研室主任', '196.00'), ('16', '管理岗系数1', '316.00'), ('17', '管理岗系数2', '0.90'), ('18', '辅导员', '0.78'), ('19', '管理岗超工作量', '160.00'), ('20', '辅导员岗超工作量', '100.00'), ('21', '教辅岗超工作量', '100.00'), ('22', '教学辅助岗', '0.79');
COMMIT;

-- ----------------------------
--  Table structure for `teachingworkload`
-- ----------------------------
DROP TABLE IF EXISTS `teachingworkload`;
CREATE TABLE `teachingworkload` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `teaching_workload` decimal(20,2) DEFAULT NULL,
  `teaching_qualified_workload` decimal(20,2) DEFAULT NULL,
  `teaching_excellent_workload` decimal(20,2) DEFAULT NULL,
  `teaching_beyond_workload` decimal(20,2) DEFAULT NULL,
  `teaching_beyond_workload_num` decimal(20,2) DEFAULT NULL,
  `teaching_beyond_workload_money` decimal(20,2) DEFAULT NULL,
  `manage_beyond_workload_money` decimal(20,2) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `total_money` decimal(20,2) DEFAULT NULL,
  `year` varchar(4) DEFAULT NULL,
  `notes` text,
  `confirm_status` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `teachingworkload_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3134 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
--  Records of `teachingworkload`
-- ----------------------------
BEGIN;
INSERT INTO `teachingworkload` VALUES ('3118', '490.07', '280.00', '0.00', '210.07', '0.00', '0.00', '0.00', '755', '0.00', '2020', null, '已确认'), ('3119', '347.76', '280.00', '0.00', '67.76', '0.00', '0.00', '0.00', '756', '0.00', '2020', null, '未确认'), ('3120', '651.51', '280.00', '28.00', '399.51', '0.00', '0.00', '0.00', '757', '0.00', '2020', null, '未确认'), ('3121', '952.26', '280.00', '0.00', '672.26', '0.00', '0.00', '0.00', '758', '0.00', '2020', null, '未确认'), ('3122', '444.44', '280.00', '28.00', '192.44', '0.00', '0.00', '0.00', '759', '0.00', '2020', null, '未确认'), ('3123', '377.71', '0.00', '0.00', '160.00', '0.00', '0.00', '0.00', '760', '0.00', '2020', null, '未确认'), ('3124', '462.00', '0.00', '28.00', '188.00', '0.00', '0.00', '0.00', '761', '0.00', '2020', null, '未确认'), ('3125', '816.50', '0.00', '28.00', '188.00', '0.00', '0.00', '0.00', '762', '0.00', '2020', null, '未确认'), ('3126', '913.97', '0.00', '28.00', '128.00', '0.00', '0.00', '0.00', '763', '0.00', '2020', null, '未确认'), ('3127', '449.07', '0.00', '0.00', '100.00', '0.00', '0.00', '0.00', '764', '0.00', '2020', null, '未确认'), ('3128', '809.41', '0.00', '28.00', '128.00', '0.00', '0.00', '0.00', '765', '0.00', '2020', null, '未确认'), ('3129', '200.78', '0.00', '0.00', '100.00', '0.00', '0.00', '0.00', '766', '0.00', '2020', null, '未确认'), ('3130', '476.97', '0.00', '0.00', '100.00', '0.00', '0.00', '0.00', '767', '0.00', '2020', null, '未确认'), ('3131', '558.19', '0.00', '28.00', '128.00', '0.00', '0.00', '0.00', '768', '0.00', '2020', null, '未确认'), ('3132', '549.79', '0.00', '0.00', '100.00', '0.00', '0.00', '0.00', '769', '0.00', '2020', null, '未确认'), ('3133', '479.07', '0.00', '28.00', '128.00', '0.00', '0.00', '0.00', '770', '0.00', '2020', null, '未确认');
COMMIT;

-- ----------------------------
--  Table structure for `user`
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(120) NOT NULL,
  `_password` varchar(120) NOT NULL,
  `department` varchar(60) DEFAULT NULL,
  `auth` smallint(6) DEFAULT NULL,
  `workload` decimal(20,2) DEFAULT NULL,
  `name` varchar(20) DEFAULT NULL,
  `work_number` int(11) DEFAULT NULL,
  `job_catecory` varchar(30) DEFAULT NULL,
  `teacher_postion` varchar(30) DEFAULT NULL,
  `teacher_postion_num` decimal(20,2) DEFAULT NULL,
  `teacher_title` varchar(30) DEFAULT NULL,
  `teacher_title_num` decimal(20,2) DEFAULT NULL,
  `notes` text,
  `postion_status` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=771 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
--  Records of `user`
-- ----------------------------
BEGIN;
INSERT INTO `user` VALUES ('755', 'cjgly', 'pbkdf2:sha256:150000$fEEiDCEN$42e990422c13ec47cf51cf24a4e711b7abce0cdca85e4dc2e37931aeef886d2c', '计算机学院', '3', '0.00', '超级管理员', '10000', '教学岗', '无', '0.00', '初级', '0.79', null, null), ('756', 'ls', 'pbkdf2:sha256:150000$3rwl2aO3$a748bd105484b982a532a98055606792f5004d9906888198416ba8576a991184', '计算机学院', '1', '0.00', '李四', '10001', '教学岗', '无', '0.00', '中级', '1.00', null, null), ('757', 'ww', 'pbkdf2:sha256:150000$FSA84snr$b992d926ff9f595523abe67fc4f66f09989642f4dd91fabdc43bc5dbafce6866', '计算机学院', '1', '0.00', '王五', '10002', '教学岗', '无', '0.00', '副高', '1.15', null, null), ('758', 'dyx', 'pbkdf2:sha256:150000$mqo4fUyn$170085e8af4fc07ec6eebf226da0c02acda63c9af098f9fba5458a2d5430915e', '计算机学院', '1', '0.00', '杜元晓', '10003', '教学岗', '无', '0.00', '正高', '1.36', null, null), ('759', 'wly', 'pbkdf2:sha256:150000$dtt6ZY0R$d4c8aee2f20e78e2d33b91450dab986431146ea78d2feb99ededa7d364d9a2de', '计算机学院', '1', '0.00', '王来有', '10004', '教学岗', '正处级', '1.30', '初级', '0.79', null, null), ('760', 'lf', 'pbkdf2:sha256:150000$WEfy9lhr$7ecff9b341fe7773569303cae0c61d7121c9693bd0c8dc538bfe1fecc9f47ebf', '计算机学院', '1', '0.00', '梁飞', '10005', '管理岗', '副处级', '1.15', '副高', '1.15', null, null), ('761', 'gjm', 'pbkdf2:sha256:150000$6w3aoPcZ$f0d98a4451a855d0ea40346dc8b3d0f7cbc337a98cfe9e5f6efd638de3f7685f', '计算机学院', '1', '0.00', '高建明', '10006', '管理岗', '正科级', '1.00', '中级', '1.00', null, null), ('762', 'zyq', 'pbkdf2:sha256:150000$8hfxaOBm$32e430013b41ce6f96c7d7bed28a5cdee349abd0ec4808ba7c3fabd5d7bf03ae', '计算机学院', '1', '0.00', '张永强', '10007', '管理岗', '副科级', '1.00', '正高', '1.36', null, null), ('763', 'ly', 'pbkdf2:sha256:150000$z10bA6tt$9e4a5717b2948d1ff3958a4c34813d78be8b824255bab2ab6bc72af2a529ce7d', '计算机学院', '1', '0.00', '刘宇', '10008', '教学辅助岗', '无', '1.00', '中级', '1.00', null, null), ('764', 'dy', 'pbkdf2:sha256:150000$QcOPXYJi$ef1d7b4a9644c8141326c70d0ff2df0f08947f4a5264e30570e51e93f9483916', '计算机学院', '1', '0.00', '杜云', '10009', '教学辅助岗', '无', '1.15', '副高', '1.15', null, null), ('765', 'ggq', 'pbkdf2:sha256:150000$UdBdEF2V$2f54fb0a56438317da6ccf6c407fa174da2d09e6d591207164d4330ec045eab9', '计算机学院', '1', '0.00', '高贵清', '10010', '教学辅助岗', '无', '1.15', '副高', '1.15', null, null), ('766', 'lec', 'pbkdf2:sha256:150000$hnmn5dqM$b13ea07559dbff134d56266edd7043074e977082108328e8c516170e40a59b3a', '计算机学院', '1', '0.00', '李二才', '10011', '教学辅助岗', '无', '0.79', '初级', '0.79', null, null), ('767', 'lzk', 'pbkdf2:sha256:150000$ITPSZzv3$c06119c35c34052fcb97a52f1fd4d18a81ec34aa39b85cc59029319d9ef74713', '计算机学院', '1', '0.00', '刘占宽', '10012', '辅导员管理岗', '无', '0.00', '初级', '0.79', null, null), ('768', 'jy', 'pbkdf2:sha256:150000$49pMIr9l$c893b39ffb076353004e954b5198d2fc63ac581e59b1bc5e24930742bcfdf9d5', '计算机学院', '1', '0.00', '金云', '10013', '辅导员管理岗', '无', '0.00', '初级', '0.79', null, null), ('769', 'srj', 'pbkdf2:sha256:150000$BuAJaTct$0386325f69e234b593095164c4de0a3966880e545c64b2b842c773967a6b48e1', '计算机学院', '1', '0.00', '孙瑞军', '10014', '辅导员管理岗', '无', '0.00', '初级', '0.79', null, null), ('770', 'st', 'pbkdf2:sha256:150000$zdhsBrP2$45472f6842148f12f93d50e9424c26379ddedc8cf8356a405260abd49d056d05', '计算机学院', '1', '0.00', '石头', '10015', '辅导员管理岗', '无', '0.00', '初级', '0.79', null, null);
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
