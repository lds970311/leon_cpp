INSERT INTO `system_slider`
VALUES ('1', '标题', null, '10', '/static/home/banner/banner1.jpg', '1', null, null, null, '1',
        '2020-08-16 05:30:27.000000', '2020-08-16 05:30:30.000000');
INSERT INTO `system_slider`
VALUES ('2', '标题2', null, '10', '/static/home/banner/banner2.jpg', '1', null, null, null, '1',
        '2020-08-16 05:31:04.000000', '2020-08-16 05:31:06.000000');
INSERT INTO `system_slider`
VALUES ('3', '标题3', null, '10', '/static/home/banner/banner3.jpg', '1', null, null, null, '1',
        '2022-08-16 05:31:04.000000', '2022-08-16 05:31:06.000000');


DROP TABLE IF EXISTS `sight`;
CREATE TABLE `sight`
(
    `id`         int(11)      NOT NULL AUTO_INCREMENT,
    `is_valid`   tinyint(1)   NOT NULL,
    `created_at` datetime(6)  NOT NULL,
    `updated_at` datetime(6)  NOT NULL,
    `name`       varchar(64)  NOT NULL,
    `desc`       varchar(256) NOT NULL,
    `main_img`   varchar(256) NOT NULL,
    `content`    longtext     NOT NULL,
    `score`      double       NOT NULL,
    `min_price`  double       NOT NULL,
    `province`   varchar(32)  NOT NULL,
    `city`       varchar(32)  NOT NULL,
    `area`       varchar(32) DEFAULT NULL,
    `town`       varchar(32) DEFAULT NULL,
    `is_top`     tinyint(1)   NOT NULL,
    `is_hot`     tinyint(1)   NOT NULL,
    `banner_img` varchar(255) NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE = InnoDB
  AUTO_INCREMENT = 11
  DEFAULT CHARSET = utf8mb4;

INSERT INTO `sight`
VALUES ('1', '1', '2020-06-10 03:40:31.485435', '2020-07-10 03:43:55.928261', '广州长隆旅游度假区',
        '长隆旅游度假区(AAAAA景区)', '/static/home/hot/h2.jpg',
        '<p>特色看点</p>\r\n\r\n<p><img src=\"http://img1.qunarzz.com/sight/p0/1411/ce/da6f0116187f2930189199932433852e.water.jpg_710x420_22391145.jpg\" /></p>\r\n\r\n<p>大马戏</p>\r\n\r\n<p>长隆国际大马戏拥有全球首创实景式马戏舞台，为你打造令人惊叹的视听盛宴。</p>\r\n\r\n<p><img src=\"http://img1.qunarzz.com/sight/p0/1501/d4/cadd9d2178cf23a63f78a1d0fa15aa9a.water.jpg_710x420_603f6085.jpg\" /></p>\r\n\r\n<p>过山车之王</p>\r\n\r\n<p>这里有全球过山车之王--垂直过山车，敢挑战吗？</p>\r\n\r\n<p><img src=\"http://img1.qunarzz.com/sight/p0/1501/76/9143ba5ff87ad17f0e0a10bc01d81898.water.jpg_710x420_423ed2b4.jpg\" /></p>\r\n\r\n<p>经典任务</p>\r\n\r\n<p>还记得《爸爸去哪儿》大电影里让爸爸们胆寒的大蟒蛇吗？同样的地方，同样的蟒蛇，你敢来体验&ldquo;任务&rdquo;吗？</p>\r\n\r\n<p><img src=\"http://img1.qunarzz.com/sight/p0/1501/51/88b46bd30102874cbefbc4a4e861f796.water.jpg_710x420_483f55f8.jpg\" /></p>\r\n\r\n<p>电影场景</p>\r\n\r\n<p>《爸爸去哪儿》大电影中，星爸萌娃们住过的小木屋，你也来住住看吧！</p>',
        '5', '69', '广东省', '广州市', '番禺区', '番禺大道', '1', '1', '/static/home/hot/h2_max.jpg');
INSERT INTO `sight`
VALUES ('2', '1', '2020-06-10 03:43:42.795701', '2020-06-10 03:43:42.795734', '南沙百万葵园', '南沙百万葵园',
        '/static/home/hot/h4.jpg',
        '<p>彩虹乐园</p>\r\n\r\n<p><img src=\"http://img1.qunarzz.com/sight/p0/1602/24/2403315d0b61473590.water.jpg_710x420_12889829.jpg\" /></p>\r\n\r\n<p>百万葵园</p>\r\n\r\n<p>以迷人的北海道七彩花田、浪漫的普罗旺斯&ldquo;薰之恋&rdquo;、热情的英伦玫瑰苑、缤纷的七彩天鹅鲜花地以及神奇的万朵鲜花天上飘等等不同亮点组合而成，真所谓花花世界，美景无敌。</p>\r\n\r\n<p><img src=\"http://img1.qunarzz.com/sight/p0/1602/62/62acf31e038b4fea90.water.jpg_710x420_03cf5ca9.jpg\" /></p>\r\n\r\n<p>彩虹世界</p>\r\n\r\n<p>追寻孩子纯真乐趣的你，面对如此神奇欢乐的魔法城堡，怎能不来。</p>\r\n\r\n<p><img src=\"http://img1.qunarzz.com/sight/p0/201405/16/9f5888734c64f01165690d09a4107c3d.jpg_710x420_0362b6c3.jpg\" /></p>\r\n\r\n<p>蓝天与向日葵</p>\r\n\r\n<p>头顶蓝天白云，眼底一大片绿色撑起的金色海洋，在微风中如波浪一般轻轻摆动，一朵朵向着太阳的葵花展开灿烂的笑脸。</p>\r\n\r\n<p><img src=\"http://img1.qunarzz.com/sight/p0/201405/16/3d2d95fdcfbd746dfe7f26a170dc2035.jpg_710x420_43c1de5b.jpg\" /></p>\r\n\r\n<p>葵花之海</p>\r\n\r\n<p>向日葵在阳光下咧着嘴笑，风吹过，翩翩起舞，金色的波浪散开来。</p>\r\n\r\n<p><img src=\"http://img1.qunarzz.com/sight/p0/1411/51/4f52d37dc64fb10ed24b0e86c54967bd.water.jpg_710x420_c89ee547.jpg\" /></p>\r\n\r\n<p>爱笑的向日葵</p>\r\n\r\n<p>花蕊散发淡淡的清香，甜甜地蔓延开来，一下子空气里全是闲适的味道。</p>\r\n\r\n<p><img src=\"http://img1.qunarzz.com/sight/p0/1411/19/f6f8c179920f612a85c707ebeecb091a.water.jpg_710x420_691356cf.jpg\" /></p>\r\n\r\n<p>吃松果</p>\r\n\r\n<p>500多只可爱的小松鼠构成一个充满温馨与情趣的童话世界</p>\r\n\r\n<p><img src=\"http://img1.qunarzz.com/sight/p0/1411/74/76d8b66b48e00750b4e4090de2e49514.water.jpg_710x420_2349c55f.jpg\" /></p>\r\n\r\n<p>风车与花海</p>\r\n\r\n<p>风车与花海，牵手漫步园中小径，花儿有点香，风儿吹着人有点醉。</p>\r\n\r\n<p><img src=\"http://img1.qunarzz.com/sight/p0/1411/3d/755609a40bb36fb27613f0be269e482d.water.jpg_710x420_0ac8cc10.jpg\" /></p>\r\n\r\n<p>彩虹花海</p>\r\n\r\n<p>一条条花带连起来，在大地上铺成彩虹，停下来，享受这一刻的美。</p>',
        '5', '69', '广东省', '广州市', '南沙区', '万顷沙镇', '1', '1', '/static/home/hot/h4_max.jpg');
INSERT INTO `sight`
VALUES ('3', '1', '2020-06-10 03:46:32.580639', '2020-06-10 03:46:32.580679', '广州塔', '广州塔(AAAA景区)',
        '/static/home/hot/h7.jpg',
        '<p>特色看点</p>\r\n\r\n<p><img src=\"http://img1.qunarzz.com/sight/p0/1412/8c/3026248924ee92dc265ca6097bc5c16a.water.jpg_710x420_dba0bf5a.jpg\" /></p>\r\n\r\n<p>城市之巅</p>\r\n\r\n<p>488摄影观景平台坐落于广州塔488米高天线桅杆处。站在平台上，可360度俯瞰羊城全貌，感受居高临下的王者之风。</p>\r\n\r\n<p><img src=\"http://img1.qunarzz.com/sight/p0/1507/72/96dc579eea7900d755d5c72fa66cb7a0.water.jpg_710x420_008a4f08.jpg\" /></p>\r\n\r\n<p>横向摩天轮</p>\r\n\r\n<p>广州塔摩天轮位于塔顶455米高空处。</p>\r\n\r\n<p><img src=\"http://img1.qunarzz.com/sight/p0/1412/36/ca2332e7d6fe263aad2a13ac2765ec9b.water.jpg_710x420_0a05774a.jpg\" /></p>\r\n\r\n<p>减振系统游览厅</p>\r\n\r\n<p>能看到全球首创的利用两个消防水箱作为被动控制阻尼质量块。</p>\r\n\r\n<p><img src=\"http://img1.qunarzz.com/sight/p0/1412/d3/336cf08fbada636cb0189a97724f1086.water.jpg_710x420_4814c9f6.jpg\" /></p>\r\n\r\n<p>观光大厅</p>\r\n\r\n<p>广州塔别具匠心地在428米及433.2米高度处分设白云和星空主题观光大厅，全透明钢化夹胶玻璃构造的&ldquo;悬空走廊&rdquo;，带来前所未有的凌空观景刺激感受。</p>\r\n\r\n<p><img src=\"http://img1.qunarzz.com/sight/p0/1412/7b/f0dff7f06b52b17e9f72a7b8990a4043.water.jpg_710x420_22681611.jpg\" /></p>\r\n\r\n<p>空中云梯</p>\r\n\r\n<p>蜘蛛侠栈道。</p>\r\n\r\n<p><img src=\"http://img1.qunarzz.com/sight/p0/201405/22/66a2b20b77262f69fc612db5d35098ba.jpg_710x420_ad085e17.jpg\" /></p>\r\n\r\n<p>夜中广州塔</p>\r\n\r\n<p>夜中远观广州塔，在夜色中&ldquo;小蛮腰&rdquo;变换缤纷颜色，江面也亮起灯，浪漫极了。</p>',
        '5', '147', '广东省', '广州市', '海珠区', '阅江西路', '1', '1', '/static/home/hot/h7_max.jpg');
INSERT INTO `sight`
VALUES ('4', '1', '2020-06-10 03:48:48.486065', '2020-06-10 03:48:48.486095', '广州融创雪世界', '广州融创雪世界',
        '/static/home/hot/h1.jpg',
        '<p>雪世界介绍</p>\r\n\r\n<p>滑雪区</p>\r\n\r\n<p>滑雪区拥有4条不同难度的雪道，平均宽度 35米，其中2条为立体交叉雪道。室内娱雪滑道落差达66米，室内初级雪道长度达460米 。</p>\r\n\r\n<p><img src=\"http://img1.qunarzz.com/sight/p0/1907/c6/c6580445d593100ea3.img.png_710x420_b60e6e16.png\" /></p>\r\n\r\n<p>小熊道</p>\r\n\r\n<p>小熊道雪道开阔，速度较缓，适合零基础滑雪者，小朋友可以在这里大胆尝试练习。</p>\r\n\r\n<p><img src=\"http://img1.qunarzz.com/sight/p0/1907/9d/9dedd22c2002f59ca3.img.png_710x420_207217e7.png\" /></p>\r\n\r\n<p>雪兔道</p>\r\n\r\n<p>雪兔道总长323米，适合初学滑雪者。</p>\r\n\r\n<p><img src=\"http://img1.qunarzz.com/sight/p0/1907/56/56bffe8d162b99ca3.img.png_710x420_af80a09e.png\" /></p>\r\n\r\n<p>老虎道</p>\r\n\r\n<p>老虎道适合高级滑雪者，落差达66米，足以让资深滑雪爱好者在感受风驰电掣般滑行的快感中深呼吸，体验惊险与刺激。</p>\r\n\r\n<p><img src=\"http://img1.qunarzz.com/sight/p0/1905/2c/2c067a67e21bf514a3.img.jpg_710x420_f76099bd.jpg\" /></p>\r\n\r\n<p>&nbsp;</p>\r\n\r\n<p>缆车</p>\r\n\r\n<p><img src=\"http://img1.qunarzz.com/sight/p0/1907/6b/6bca5392887a59e5a3.img.png_710x420_e0da9c00.png\" /></p>\r\n\r\n<p>&nbsp;</p>\r\n\r\n<p>魔毯</p>\r\n\r\n<p>娱雪玩雪区</p>\r\n\r\n<p>除了滑雪以外，冰雪娱乐区也有很多选择：飞跃冰川、雪上飞碟、冰上碰碰车、探险步道等项目，不会滑雪也能玩！</p>\r\n\r\n<p><img src=\"http://img1.qunarzz.com/sight/p0/1907/d1/d19b9125c99fe8cca3.img.jpg_710x420_30e31289.jpg\" /></p>\r\n\r\n<p>雪上飞碟</p>\r\n\r\n<p>上飞碟形状的充气雪圈，从雪山顶飞驰而下，清爽的雪风扑面而来，在眨眼间滑落山底，在意犹未尽中感受雪地速度与激爽。</p>\r\n\r\n<p><img src=\"http://img1.qunarzz.com/sight/p0/1907/e3/e375ecb057e6b345a3.img.png_710x420_63be7635.png\" /></p>\r\n\r\n<p>冰上碰碰车</p>\r\n\r\n<p>光滑的冰面减少摩擦，碰碰游戏更能带来刺激感与乐趣，在南方也可体验北方冬天的热门游戏。</p>\r\n\r\n<p><img src=\"http://img1.qunarzz.com/sight/p0/1907/d8/d8fdc36f015fd431a3.img.png_710x420_bcf6c21c.png\" /></p>\r\n\r\n<p>冰上自行车</p>\r\n\r\n<p>光滑的冰面踩单车？南方的小伙伴们一定第一次玩了，充满意想不到的乐趣，是老少咸宜的冰上项目。</p>\r\n\r\n<p><img src=\"http://img1.qunarzz.com/sight/p0/1907/b9/b95a946b8704f2f8a3.img.png_710x420_3052b2bb.png\" /></p>\r\n\r\n<p>探险步道</p>\r\n\r\n<p>国内滑雪场首条探险步道，集趣味、娱乐、拓展功能为一体，在高空、速度、力量、毅力等元素的挑战中，感受感官上的刺激和闯关成功的成就感。</p>\r\n\r\n<p><img src=\"http://img1.qunarzz.com/sight/p0/1907/b3/b315bcaaf96ac141a3.img.png_710x420_45b88474.png\" /></p>\r\n\r\n<p>飞跃冰川</p>\r\n\r\n<p>首台室内滑雪场同向双溜索（比翼双飞），高空横跨滑雪场。单条长83米，高差10米，让游客体验从白雪皑皑的上空急速滑过的拉风感觉。</p>',
        '5', '145', '广东省', '广州市', '花都区', '平步大道', '1', '1', '/static/home/hot/h1_max.jpg');
INSERT INTO `sight`
VALUES ('5', '1', '2020-06-10 03:51:37.063462', '2020-06-10 03:51:37.063495', '广州正佳极地海洋世界', '海洋欢乐颂',
        '/static/home/hot/h3.jpg',
        '<p>正佳极地海洋世界坐落于广州天河核心商圈正佳广场，总建筑面积超58000平方米，拥有共500种超30000只极地海洋动物，是座室内空中极地海洋馆。</p>\r\n\r\n<p><img src=\"http://img1.qunarzz.com/sight/p0/1709/b2/b245c37047393197a3.img.jpg_710x420_8a20804b.jpg\" /></p>\r\n\r\n<p><img src=\"http://img1.qunarzz.com/sight/p0/1709/7e/7e4a76858167fddba3.img.jpg_710x420_d3d15109.jpg\" /></p>\r\n\r\n<p>展馆内设有二十一大主题展区，44米亚克力单体水族展示缸、20米超长幻彩水母大道、360度超大广角海底隧道等，专业的建筑及视觉设计团队，开创性地将生物展示和声光电技术完美融合，集观赏、娱乐、休闲、科普、环保于一体的梦幻主题式极地海洋体验。</p>\r\n\r\n<p><img src=\"http://img1.qunarzz.com/sight/p0/1709/e9/e9fdbc2c83ee75d9a3.img.jpg_710x420_f803b71d.jpg\" /></p>\r\n\r\n<p><img src=\"http://img1.qunarzz.com/sight/p0/1709/7e/7e0c973d2fc257aea3.img.jpg_710x420_f5d7a3c4.jpg\" /></p>',
        '5', '80', '广东省', '广州市', '天河区', '天河路', '1', '1', '/static/home/hot/h3_max.jpg');
INSERT INTO `sight`
VALUES ('6', '1', '2020-06-10 03:54:41.685676', '2020-06-10 03:54:41.685707', '宝墨园', '宝墨园(AAAA景区)',
        '/static/home/hot/h5.jpg',
        '<p>满园樱色</p>\r\n\r\n<p><img src=\"http://img1.qunarzz.com/sight/p0/1603/20/208ed6bc971a41cf90.img.jpg_710x420_9878bc3b.jpg\" /></p>\r\n\r\n<p>花色丰富</p>\r\n\r\n<p>樱园一带以小日樱花为主，收集了早樱、晚樱和垂枝樱等共6种10余个佳品的樱花，花色丰富，绚丽多彩，枝、干多异且花期不同。</p>\r\n\r\n<p><img src=\"http://img1.qunarzz.com/sight/p0/1603/bf/bf5079558989b5f590.img.jpg_710x420_1b050232.jpg\" /></p>\r\n\r\n<p>漫山樱色</p>\r\n\r\n<p>盛开时节，樱园酷似花的海洋，成千上万游客慕名而至，留连观赏，如醉如痴</p>\r\n\r\n<p><img src=\"http://img1.qunarzz.com/sight/p0/1603/c2/c24ab9c56b47b7b990.img.jpg_710x420_e26d26ff.jpg\" /></p>\r\n\r\n<p>晚樱</p>\r\n\r\n<p>每当寒冬过后，梅花凋谢之时，早樱开放，继而小日樱花、垂枝樱花、晚樱等开放。</p>',
        '5', '41', '广东省', '广州市', '番禺区', '沙湾镇紫妮村', '1', '1', '/static/home/hot/h5_max.jpg');
INSERT INTO `sight`
VALUES ('7', '1', '2020-06-10 03:57:02.836359', '2020-06-10 03:57:02.836391', '广东科学中心', '广东科学中心(AAAA景区)',
        '/static/home/hot/h6.jpg',
        '<p><img src=\"http://img1.qunarzz.com/sight/p0/1412/93/ec106a80128ac36fdf64a316eeb3810b.water.jpg_710x420_40024707.jpg\" /></p>\r\n\r\n<p>儿童天地</p>\r\n\r\n<p>本展馆主要面向12岁以下儿童，通过角色扮演、情景体验等丰富多彩的形式，让儿童了解与日常生活和周围世界有关的浅显的科学知识，从而丰富小朋友的童年生活感受和经历。</p>\r\n\r\n<p><img src=\"http://img1.qunarzz.com/sight/p0/1412/69/4a4b8ce9db8f4f11a74321751063b8b6.water.jpg_710x420_175b7f05.jpg\" /></p>\r\n\r\n<p>飞天之梦</p>\r\n\r\n<p>本展馆展示了人类千百年来的梦想--翱翔蓝天，挣脱了地球引力，实现了千百年来的梦想。</p>\r\n\r\n<p><img src=\"http://img1.qunarzz.com/sight/p0/1412/a2/3e8e996372ca6771063b2a6d0235efd3.water.jpg_710x420_231aebe6.jpg\" /></p>\r\n\r\n<p>绿色家园</p>\r\n\r\n<p>本展馆以环保为主题，岭南特色为背景，以生动有趣的形式将美丽的大自然全景式地展现在观众面前。</p>',
        '4.5', '42', '广东省', '广州市', '番禺区', '大学城西六路168号', '1', '1', '/static/home/hot/h6_max.jpg');
INSERT INTO `sight`
VALUES ('8', '1', '2020-06-10 03:58:51.478626', '2020-06-10 03:58:51.478658', '珠江夜游', '珠江夜游',
        '/static/home/hot/h10.jpg',
        '<p><img src=\"http://img1.qunarzz.com/sight/p0/1501/46/462186e0e32146e9.water.jpg_710x420_9b0f6c53.jpg\" /></p>\r\n\r\n<p>特色</p>\r\n\r\n<p>宽大的空间在悠和的灯光映衬下，尤如置身于五星级殿堂。</p>\r\n\r\n<p><img src=\"http://img1.qunarzz.com/sight/p0/1501/71/7190e54ed15c0a3e.water.jpg_710x420_75b86aa1.jpg\" /></p>\r\n\r\n<p>特色</p>\r\n\r\n<p>出游时播放江面景观的室内视频，即使下雨，亦可在室内观赏珠江两岸的景色</p>\r\n\r\n<p><img src=\"http://img1.qunarzz.com/sight/p0/1501/9c/9c8d9add730ca143.water.jpg_710x420_fb5f4026.jpg\" /></p>\r\n\r\n<p>特色</p>\r\n\r\n<p>完备的高保真音响配置，使尊贵的你在游览珠江两岸风情的同时，听觉上也可大大的享受</p>',
        '4.5', '47.5', '广东省', '广州市', '越秀区', '珠江', '0', '1', '/static/home/hot/h10_max.jpg');
INSERT INTO `sight`
VALUES ('9', '1', '2020-06-10 04:01:59.674665', '2020-06-10 04:01:59.674703', '岭南印象园', '岭南印象园(AAAA景区)',
        '/static/home/hot/h8.jpg',
        '<p>岭南乡土风情和民俗文化</p>\r\n\r\n<p><img src=\"http://img1.qunarzz.com/sight/p0/1411/67/a741e142e49ab83ba93ec0a502ffb29b.water.jpg_710x420_7cb7fe86.jpg\" /></p>\r\n\r\n<p>岭南印象</p>\r\n\r\n<p>岭南少数民族独特的歌舞，带你感受这个民族的文化魅力，吸引你探索这篇土地的风土民情。</p>\r\n\r\n<p><img src=\"http://img1.qunarzz.com/sight/p0/1511/b8/b88c54e6682cd12490.water.jpg_710x420_5edc96b7.jpg\" /></p>\r\n\r\n<p>建筑群落</p>\r\n\r\n<p>悠长的青云巷、古朴的趟栊门、精致的满洲窗，小溪蜿蜒，池塘清澈，处处散发着岭南水乡的韵味。</p>\r\n\r\n<p><img src=\"http://img1.qunarzz.com/sight/p0/1505/fd/fd8124c334568f28.water.jpg_710x420_084ba679.jpg\" /></p>\r\n\r\n<p>宗祠艺术</p>\r\n\r\n<p>这里的霍氏大宗祠和萧氏宗祠包含了木雕、砖雕、石雕、灰塑、陶塑等传统工艺，凝聚了众多艺术创作者的心血，具有很高的艺术价值。</p>\r\n\r\n<p><img src=\"http://img1.qunarzz.com/sight/p0/1409/18/aff9b12820e1aab9fa59db2f7d5bc229.jpg_710x420_5ae37958.jpg\" /></p>\r\n\r\n<p>民族工艺品</p>\r\n\r\n<p>精致的工艺品，体现了这里独有的民族特色。</p>\r\n\r\n<p><img src=\"http://img1.qunarzz.com/sight/p0/1509/54/0e51221629b2934fd87958179a08f452.water.jpg_710x420_363f5de0.jpg\" /></p>\r\n\r\n<p>木雕宫灯</p>\r\n\r\n<p>古典工整的造型，精雕细琢的雕花，让游客感受钢筋水泥城市之外的优雅静谧。</p>\r\n\r\n<p><img src=\"http://img1.qunarzz.com/sight/p0/1509/5b/9427a83ff2ca0f2c6b90c571849b7d4a.water.jpg_710x420_b972cfde.jpg\" /></p>\r\n\r\n<p>石湾陶瓷</p>\r\n\r\n<p>展览销售石湾陶瓷。游客在此可以欣赏购买造型多样，栩栩如生的石湾公仔，活泼生动又不失文化内涵，可以装点家居也可以馈赠亲朋。</p>',
        '5', '47.1', '广东省', '广州市', '番禺区', '外环西路', '0', '1', '/static/home/hot/h8_max.jpg');
INSERT INTO `sight`
VALUES ('10', '1', '2020-06-10 04:05:44.085079', '2020-06-10 04:05:44.085109', '增城白水寨风景名胜区',
        '增城白水寨风景名胜区(AAAA景区)', '/static/home/hot/h9.jpg',
        '<p>景区特色</p>\r\n\r\n<p><img src=\"http://img1.qunarzz.com/sight/p0/201405/29/858ab67cdd9e22f70b2e068ba340ba16.jpg_710x420_20e51097.jpg\" /></p>\r\n\r\n<p>海船木栈道</p>\r\n\r\n<p>全国仅见的精品海船木栈道。在白水寨漫步古朴的海船木栈道登山观瀑，看流水潺潺、听瀑布轰鸣，倍感诗意。</p>\r\n\r\n<p><img src=\"http://img1.qunarzz.com/sight/p0/1411/dd/dcdf8fa407cc42b4169229c1ba3fa1c7.water.jpg_710x420_6fa65f83.jpg\" /></p>\r\n\r\n<p>白水绿道</p>\r\n\r\n<p>广东首条白水绿道！</p>\r\n\r\n<p><img src=\"http://img1.qunarzz.com/sight/p0/201405/16/ed05af293a7b1fcc0a91587e0c18403f.jpg_710x420_067fa8b9.jpg\" /></p>\r\n\r\n<p>竹林吸氧</p>\r\n\r\n<p>登山健身、沐瀑品氧的地方！</p>\r\n\r\n<p><img src=\"http://img1.qunarzz.com/sight/p0/201405/29/f31c2797793fbc34b0ffcc3751ba090a.jpg_710x420_af543daf.jpg\" /></p>\r\n\r\n<p>大瀑布</p>\r\n\r\n<p>其形态优美，彷如仙女下凡，相传乃八仙之中何仙姑的化身。</p>\r\n\r\n<p><img src=\"http://img1.qunarzz.com/sight/p0/201405/29/df585c4f62a64d51d004560e06917ce5.jpg_710x420_97cacdc6.jpg\" /></p>\r\n\r\n<p>9999级登山步径</p>\r\n\r\n<p>远近闻名的9999。</p>\r\n\r\n<p><img src=\"http://img1.qunarzz.com/wugc/p163/201205/30/717053909b493cc893835fbb.png_710x420_a97e9bab.png\" /></p>\r\n\r\n<p>生态资源</p>\r\n\r\n<p>拥有得天独厚的自然生态资源，可谓集天地之灵气，山水之秀美于一体</p>',
        '5', '55', '广东省', '增城市', '派潭镇', '白水寨风景名胜区', '0', '0', '/static/home/hot/h9_max.jpg');

-- ----------------------------