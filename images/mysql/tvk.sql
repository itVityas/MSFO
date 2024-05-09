-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Хост: bd
-- Время создания: Сен 10 2023 г., 15:40
-- Версия сервера: 8.0.34
-- Версия PHP: 7.4.27

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `tvk`
--

-- --------------------------------------------------------

--
-- Структура таблицы `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Структура таблицы `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Структура таблицы `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add content type', 4, 'add_contenttype'),
(14, 'Can change content type', 4, 'change_contenttype'),
(15, 'Can delete content type', 4, 'delete_contenttype'),
(16, 'Can view content type', 4, 'view_contenttype'),
(17, 'Can add session', 5, 'add_session'),
(18, 'Can change session', 5, 'change_session'),
(19, 'Can delete session', 5, 'delete_session'),
(20, 'Can view session', 5, 'view_session'),
(21, 'Can add cic', 6, 'add_cic'),
(22, 'Can change cic', 6, 'change_cic'),
(23, 'Can delete cic', 6, 'delete_cic'),
(24, 'Can view cic', 6, 'view_cic'),
(25, 'Can add department', 7, 'add_department'),
(26, 'Can change department', 7, 'change_department'),
(27, 'Can delete department', 7, 'delete_department'),
(28, 'Can view department', 7, 'view_department'),
(29, 'Can add imns', 8, 'add_imns'),
(30, 'Can change imns', 8, 'change_imns'),
(31, 'Can delete imns', 8, 'delete_imns'),
(32, 'Can view imns', 8, 'view_imns'),
(33, 'Can add risk', 9, 'add_risk'),
(34, 'Can change risk', 9, 'change_risk'),
(35, 'Can delete risk', 9, 'delete_risk'),
(36, 'Can view risk', 9, 'view_risk'),
(37, 'Can add examination', 10, 'add_examination'),
(38, 'Can change examination', 10, 'change_examination'),
(39, 'Can delete examination', 10, 'delete_examination'),
(40, 'Can view examination', 10, 'view_examination'),
(41, 'Can add user', 11, 'add_user'),
(42, 'Can change user', 11, 'change_user'),
(43, 'Can delete user', 11, 'delete_user'),
(44, 'Can view user', 11, 'view_user');

-- --------------------------------------------------------

--
-- Структура таблицы `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` bigint NOT NULL
) ;

-- --------------------------------------------------------

--
-- Структура таблицы `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'contenttypes', 'contenttype'),
(5, 'sessions', 'session'),
(6, 'tvk', 'cic'),
(7, 'tvk', 'department'),
(10, 'tvk', 'examination'),
(8, 'tvk', 'imns'),
(9, 'tvk', 'risk'),
(11, 'users', 'user');

-- --------------------------------------------------------

--
-- Структура таблицы `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'tvk', '0001_initial', '2023-09-10 15:36:57.622036'),
(2, 'contenttypes', '0001_initial', '2023-09-10 15:36:57.658446'),
(3, 'contenttypes', '0002_remove_content_type_name', '2023-09-10 15:36:57.705081'),
(4, 'auth', '0001_initial', '2023-09-10 15:36:57.906799'),
(5, 'auth', '0002_alter_permission_name_max_length', '2023-09-10 15:36:57.958816'),
(6, 'auth', '0003_alter_user_email_max_length', '2023-09-10 15:36:57.968882'),
(7, 'auth', '0004_alter_user_username_opts', '2023-09-10 15:36:57.978813'),
(8, 'auth', '0005_alter_user_last_login_null', '2023-09-10 15:36:57.990958'),
(9, 'auth', '0006_require_contenttypes_0002', '2023-09-10 15:36:57.995036'),
(10, 'auth', '0007_alter_validators_add_error_messages', '2023-09-10 15:36:58.003296'),
(11, 'auth', '0008_alter_user_username_max_length', '2023-09-10 15:36:58.013659'),
(12, 'auth', '0009_alter_user_last_name_max_length', '2023-09-10 15:36:58.025048'),
(13, 'auth', '0010_alter_group_name_max_length', '2023-09-10 15:36:58.040895'),
(14, 'auth', '0011_update_proxy_permissions', '2023-09-10 15:36:58.054322'),
(15, 'auth', '0012_alter_user_first_name_max_length', '2023-09-10 15:36:58.063145'),
(16, 'users', '0001_initial', '2023-09-10 15:36:58.401818'),
(17, 'admin', '0001_initial', '2023-09-10 15:36:58.510351'),
(18, 'admin', '0002_logentry_remove_auto_add', '2023-09-10 15:36:58.523651'),
(19, 'admin', '0003_logentry_add_action_flag_choices', '2023-09-10 15:36:58.539022'),
(20, 'sessions', '0001_initial', '2023-09-10 15:36:58.572716'),
(21, 'tvk', '0002_examination_fio', '2023-09-10 15:36:58.598565');

-- --------------------------------------------------------

--
-- Структура таблицы `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Структура таблицы `tvk_cic`
--

CREATE TABLE `tvk_cic` (
  `id` bigint NOT NULL,
  `number` varchar(255) DEFAULT NULL,
  `date_state` date NOT NULL,
  `date_from` date NOT NULL,
  `date_to` date NOT NULL,
  `message` varchar(255) DEFAULT NULL,
  `imnss_id` bigint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Структура таблицы `tvk_department`
--

CREATE TABLE `tvk_department` (
  `id` bigint NOT NULL,
  `name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `tvk_department`
--

INSERT INTO `tvk_department` (`id`, `name`) VALUES
(2, 'Учет'),
(3, 'Контрольная работа'),
(4, 'Камеральные проверки'),
(5, 'Налогообложения физических лиц'),
(6, 'Оперативные мероприятия'),
(7, 'Бухгалтерской учет и отчетность'),
(8, 'Информационно-разъяснительная работа'),
(9, 'Правовой работы'),
(10, 'Кадровой работы'),
(11, 'Информационного обеспечения'),
(12, 'Информационная безопасность'),
(13, 'Организационно-технического обеспечения');

-- --------------------------------------------------------

--
-- Структура таблицы `tvk_examination`
--

CREATE TABLE `tvk_examination` (
  `id` bigint NOT NULL,
  `count_all` int NOT NULL,
  `count_contravention` int NOT NULL,
  `description` longtext,
  `cic_id` bigint NOT NULL,
  `department_id` bigint NOT NULL,
  `obj_id` bigint NOT NULL,
  `risk_id` bigint NOT NULL,
  `fio` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Структура таблицы `tvk_imns`
--

CREATE TABLE `tvk_imns` (
  `id` bigint NOT NULL,
  `number` int NOT NULL,
  `name` varchar(255) NOT NULL,
  `shot_name` varchar(255) NOT NULL,
  `address` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `post` varchar(255) DEFAULT NULL,
  `unp` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `tvk_imns`
--

INSERT INTO `tvk_imns` (`id`, `number`, `name`, `shot_name`, `address`, `email`, `post`, `unp`) VALUES
(1, 301, 'Инспекция МНС по Витебской области', 'ИМНС по Витебской области', 'г. Витебск, ул. Гоголя, 8.', 'imns301@nalog.gov.by', '210010', '300003568'),
(2, 305, 'Инспекция МНС по Витебскому району', 'ИМНС по Витебскому району', 'г. Витебск, ул. Суворова 42/13', 'imns305@nalog.gov.by', '210026', '300003606'),
(3, 306, 'Инспекция МНС по Глубокскому району', 'ИМНС по Глубокскому району', 'г. Глубокое, ул. Красноармейская, 8.', 'imns306@nalog.gov.by', '211793', '300003619'),
(4, 313, 'Инспекция МНС по Оршанскому району', 'ИМНС по Оршанскому району', 'г. Орша, ул. Мира, 17.', 'imns313@nalog.gov.by', '211391', '300990776'),
(5, 314, 'Инспекция МНС по Полоцкому району', 'ИМНС по Полоцкому району', 'г. Полоцк, ул. Свердлова, 9.', 'imns314@nalog.gov.by', '211400', '300990842'),
(6, 315, 'Инспекция МНС по Поставскому району', 'ИМНС по Поставскому району', 'г. Поставы, ул. Советская, 84а.', 'imns315@nalog.gov.by', '211875', '300003700'),
(7, 341, 'Инспекция МНС по Лепельскому району', 'ИМНС по Лепельскому району', 'г. Лепель, пл.Свободы, 10.', 'imns341@nalog.gov.by', '211174', '300003805'),
(8, 351, 'Инспекция МНС по г. Новополоцку', 'ИМНС по г.Новополоцку', 'г. Новополоцк, ул. Молодежная 49/2.', 'imns351@nalog.gov.by', '211440', '300003818'),
(9, 362, 'Инспекция МНС по Железнодорожному району г. Витебска', 'ИМНС по Железнодорожному району г.Витебска', 'г. Витебск, ул. Зеньковой, 1 корп. 10.', 'imns362@nalog.gov.by', '210001', '300003846'),
(10, 363, 'Инспекция МНС Октябрьскому району г. Витебска', 'ИМНС по Октябрьскому району г. Витебска', 'г. Витебск, ул. Смоленская, 9.', 'imns363@nalog.gov.by', '210029', '300003859'),
(11, 364, 'Инспекция МНС по Первомайскому району г. Витебска', 'ИМНС по Первомайскому району г.Витебска', 'г. Витебск, ул. Гоголя, 8.', 'imns364@nalog.gov.by', '210010', '300003861'),
(20, 300, 'Витебская область', 'Область', 'г. Витебск, ул. Гоголя 8', 'imns301@nalog.gov.by', '210000', '300003568');

-- --------------------------------------------------------

--
-- Структура таблицы `tvk_risk`
--

CREATE TABLE `tvk_risk` (
  `id` bigint NOT NULL,
  `code` varchar(50) NOT NULL,
  `name` longtext NOT NULL,
  `description` longtext,
  `enable` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Структура таблицы `users_user`
--

CREATE TABLE `users_user` (
  `id` bigint NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `access` int DEFAULT NULL,
  `imns_id` bigint DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `users_user`
--

INSERT INTO `users_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`, `access`, `imns_id`) VALUES
(1, 'pbkdf2_sha256$600000$jKTngyRxZWGFl4U10JP00F$EYaRCJwCaIrTP/tQLwI9cVR/n1LM1aUBt16DzdNuZso=', '2023-09-10 15:39:35.631647', 1, 'admin', '', '', '', 1, 1, '2023-07-15 11:36:45.000000', 1, 1),
(3, 'pbkdf2_sha256$600000$c8MrV9TOVU10uQP7o5l44e$JQ0Q4bLCIvJZpX5O4B1GRhhW9iyYhzhyKicZ8cxrwhk=', '2023-07-17 12:44:40.199000', 0, 'imns301', '', '', '', 0, 1, '2023-07-15 13:35:13.803000', 1, 1);

-- --------------------------------------------------------

--
-- Структура таблицы `users_user_groups`
--

CREATE TABLE `users_user_groups` (
  `id` bigint NOT NULL,
  `user_id` bigint NOT NULL,
  `group_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Структура таблицы `users_user_user_permissions`
--

CREATE TABLE `users_user_user_permissions` (
  `id` bigint NOT NULL,
  `user_id` bigint NOT NULL,
  `permission_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Индексы таблицы `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Индексы таблицы `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Индексы таблицы `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_users_user_id` (`user_id`);

--
-- Индексы таблицы `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Индексы таблицы `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Индексы таблицы `tvk_cic`
--
ALTER TABLE `tvk_cic`
  ADD PRIMARY KEY (`id`),
  ADD KEY `tvk_cic_imnss_id_351d55c1_fk_tvk_imns_id` (`imnss_id`);

--
-- Индексы таблицы `tvk_department`
--
ALTER TABLE `tvk_department`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `tvk_examination`
--
ALTER TABLE `tvk_examination`
  ADD PRIMARY KEY (`id`),
  ADD KEY `tvk_examination_cic_id_eb85ec1e_fk_tvk_cic_id` (`cic_id`),
  ADD KEY `tvk_examination_department_id_8470b83d_fk_tvk_department_id` (`department_id`),
  ADD KEY `tvk_examination_obj_id_8ade8eca_fk_tvk_imns_id` (`obj_id`),
  ADD KEY `tvk_examination_risk_id_1ace2e68_fk_tvk_risk_id` (`risk_id`);

--
-- Индексы таблицы `tvk_imns`
--
ALTER TABLE `tvk_imns`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `tvk_risk`
--
ALTER TABLE `tvk_risk`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `code` (`code`);

--
-- Индексы таблицы `users_user`
--
ALTER TABLE `users_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD KEY `users_user_imns_id_3450fc1a_fk_tvk_imns_id` (`imns_id`);

--
-- Индексы таблицы `users_user_groups`
--
ALTER TABLE `users_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `users_user_groups_user_id_group_id_b88eab82_uniq` (`user_id`,`group_id`),
  ADD KEY `users_user_groups_group_id_9afc8d0e_fk_auth_group_id` (`group_id`);

--
-- Индексы таблицы `users_user_user_permissions`
--
ALTER TABLE `users_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `users_user_user_permissions_user_id_permission_id_43338c45_uniq` (`user_id`,`permission_id`),
  ADD KEY `users_user_user_perm_permission_id_0b93982e_fk_auth_perm` (`permission_id`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT для таблицы `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT для таблицы `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=45;

--
-- AUTO_INCREMENT для таблицы `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT для таблицы `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT для таблицы `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT для таблицы `tvk_cic`
--
ALTER TABLE `tvk_cic`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT для таблицы `tvk_department`
--
ALTER TABLE `tvk_department`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT для таблицы `tvk_examination`
--
ALTER TABLE `tvk_examination`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT для таблицы `tvk_imns`
--
ALTER TABLE `tvk_imns`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT для таблицы `tvk_risk`
--
ALTER TABLE `tvk_risk`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT для таблицы `users_user`
--
ALTER TABLE `users_user`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT для таблицы `users_user_groups`
--
ALTER TABLE `users_user_groups`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT для таблицы `users_user_user_permissions`
--
ALTER TABLE `users_user_user_permissions`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- Ограничения внешнего ключа сохраненных таблиц
--

--
-- Ограничения внешнего ключа таблицы `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Ограничения внешнего ключа таблицы `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Ограничения внешнего ключа таблицы `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`);

--
-- Ограничения внешнего ключа таблицы `tvk_cic`
--
ALTER TABLE `tvk_cic`
  ADD CONSTRAINT `tvk_cic_imnss_id_351d55c1_fk_tvk_imns_id` FOREIGN KEY (`imnss_id`) REFERENCES `tvk_imns` (`id`);

--
-- Ограничения внешнего ключа таблицы `tvk_examination`
--
ALTER TABLE `tvk_examination`
  ADD CONSTRAINT `tvk_examination_cic_id_eb85ec1e_fk_tvk_cic_id` FOREIGN KEY (`cic_id`) REFERENCES `tvk_cic` (`id`),
  ADD CONSTRAINT `tvk_examination_department_id_8470b83d_fk_tvk_department_id` FOREIGN KEY (`department_id`) REFERENCES `tvk_department` (`id`),
  ADD CONSTRAINT `tvk_examination_obj_id_8ade8eca_fk_tvk_imns_id` FOREIGN KEY (`obj_id`) REFERENCES `tvk_imns` (`id`),
  ADD CONSTRAINT `tvk_examination_risk_id_1ace2e68_fk_tvk_risk_id` FOREIGN KEY (`risk_id`) REFERENCES `tvk_risk` (`id`);

--
-- Ограничения внешнего ключа таблицы `users_user`
--
ALTER TABLE `users_user`
  ADD CONSTRAINT `users_user_imns_id_3450fc1a_fk_tvk_imns_id` FOREIGN KEY (`imns_id`) REFERENCES `tvk_imns` (`id`);

--
-- Ограничения внешнего ключа таблицы `users_user_groups`
--
ALTER TABLE `users_user_groups`
  ADD CONSTRAINT `users_user_groups_group_id_9afc8d0e_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `users_user_groups_user_id_5f6f5a90_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`);

--
-- Ограничения внешнего ключа таблицы `users_user_user_permissions`
--
ALTER TABLE `users_user_user_permissions`
  ADD CONSTRAINT `users_user_user_perm_permission_id_0b93982e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `users_user_user_permissions_user_id_20aca447_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
