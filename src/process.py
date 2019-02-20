import matplotlib.pyplot as plt
import numpy as np

v = [['9873', '298900', '72'],
['1038144355', '166602', '43'],
['1841905473', '166602', '43'],
['1041984154', '155774', '43'],
['2430725435', '630000', '96'],
['95232939', '279000', '85'],
['2432795578', '680000', '96'],
['2430693790', '500000', '70'],
['1037798719', '650000', '84'],
['1352975551', '349000', '60'],
['2430689195', '630000', '96'],
['2428305306', '1990000', '243'],
['1041030650', '830000', '107'],
['2430576511', '640000', '100'],
['2430332883', '688000', '97'],
['2432346104', '3800000', '350'],
['1041858151', '510000', '72'],
['1778305506', '510000', '85'],
['1755025478', '580000', '105'],
['1038322800', '630000', '96'],
['90521997', '660000', '82'],
['2429037829', '575000', '98'],
['1042819631', '1100000', '120'],
['1038538635', '300000', '46'],
['1352725567', '2150000', '243'],
['2431511696', '1100000', '170'],
['64747855', '450000', '72'],
['92376300', '680000', '103'],
['1037235262', '350000', '80'],
['2430966174', '450000', '50'],
['70939842', '550000', '60'],
['91005624', '749900', '91'],
['1367895658', '150000', '30'],
['90986729', '219900', '31'],
['9872', '279000', '57'],
['8878', '355489', '50'],
['9875', '549900', '98'],
['10559', '228000', '41'],
['1791775473', '148025', '41'],
['45964797', '2100000', '243'],
['1038195346', '660000', '86'],
['1040187659', '2550000', '210'],
['1391865475', '1516100', '152'],
['1039654388', '700000', '85'],
['1038556184', '860000', '138'],
['2036035474', '650000', '124'],
['1391865476', '350000', '88'],
['1778685478', '480000', '72'],
['69697817', '650000', '96'],
['1041030824', '610000', '98'],
['1037292310', '2500000', '530'],
['92265470', '2500000', '243'],
['77903333', '2100000', '230'],
['91912275', '493000', '58'],
['2433190625', '285000', '80'],
['2433293096', '720000', '96'],
['82535811', '630000', '97'],
['74780725', '320000', '68'],
['1040416726', '580000', '97'],
['1353065536', '1380000', '48'],
['1953515481', '790000', '125'],
['91634254', '440000', '75'],
['94768427', '125000', '45'],
['1404185485', '650000', '105'],
['2431952077', '470000', '85'],
['84937418', '340000', '40'],
['1837185477', '650000', '90'],
['1037754314', '525000', '72'],
['71147442', '4100000', '523'],
['84418154', '340000', '40'],
['1507775477', '137944', '46'],
['1776545474', '137944', '46'],
['1955305481', '141538', '45'],
['5866', '144185', '42'],
['7834', '146310', '46'],
['68012905', '399000', '72'],
['91714632', '630000', '96'],
['75083201', '1400000', '122'],
['69512917', '850000', '120'],
['81224761', '800000', '100'],
['1039644652', '300000', '53'],
['91057361', '930000', '165'],
['91443098', '1100000', '128'],
['2431951702', '630000', '100'],
['1038357623', '650000', '86'],
['73946568', '2450000', '243'],
['2430309677', '630000', '96'],
['1040957199', '749947', '97'],
['89224209', '950000', '150'],
['1042711273', '800000', '121'],
['1353175481', '1700000', '260'],
['2429300992', '630000', '96'],
['81430094', '330000', '68'],
['48587228', '1600000', '243'],
['88251387', '1300000', '178'],
['1466205479', '450000', '75'],
['68589186', '1100000', '160'],
['2433358968', '680000', '80'],
['2431625393', '1400000', '165'],
['1038599888', '450000', '72'],
['64632021', '275000', '31'],
['45769172', '330000', '68'],
['1801675476', '3300000', '243'],
['2429348003', '880366', '146'],
['1372635482', '580000', '97'],
['2227', '142347', '47'],
['8145', '238872', '43'],
['1824615480', '238872', '43'],
['10716', '200000', '46'],
['1822245482', '200000', '46'],
['1466165478', '630000', '96'],
['1041492839', '400000', '68'],
['1466165479', '580000', '84'],
['53593960', '1250000', '128'],
['1211895474', '680000', '96'],
['1041705499', '380000', '70'],
['88251430', '790000', '127'],
['1042711239', '450000', '71'],
['1964595491', '630000', '93'],
['69140036', '450000', '73'],
['1042711238', '600000', '71'],
['2431951315', '1250000', '220'],
['1818365473', '1800000', '420'],
['1729065482', '650000', '100'],
['1812335482', '350000', '55'],
['1039133952', '750000', '85'],
['1040370845', '500000', '65'],
['67496985', '525000', '73'],
['1381215480', '980000', '119'],
['1879405475', '380000', '70'],
['2431949097', '600000', '73'],
['90618460', '650000', '96'],
['1040290302', '395000', '49'],
['69143162', '720000', '96'],
['2431944951', '399000', '64'],
['2431951320', '800000', '90'],
['1037593801', '525000', '70'],
['1039462819', '1450000', '165'],
['1466165474', '490000', '60'],
['49191177', '650000', '105'],
['1041092800', '470000', '110'],
['10053', '200000', '41'],
['1781585476', '200000', '41'],
['1792535490', '228000', '40'],
['10715', '228000', '40'],
['2428242498', '470000', '72'],
['2428445487', '240000', '40'],
['92724215', '630000', '93'],
['2431949058', '400000', '74'],
['1257065496', '470000', '66'],
['1211685485', '300000', '63'],
['2431949506', '900000', '135'],
['92353578', '370000', '70'],
['2054745492', '150000', '35'],
['1039330084', '620000', '100'],
['1042731154', '580000', '0'],
['1039106804', '780000', '85'],
['2427360408', '650000', '96'],
['1990145474', '199000', '43'],
['1037962520', '350000', '58'],
['1343285499', '850000', '162'],
['88690487', '245000', '32'],
['1516635496', '480000', '75'],
['1880845491', '698000', '89'],
['1038599863', '525000', '72'],
['2431951099', '1100000', '105'],
['1381235488', '329000', '36'],
['1264045474', '500000', '65'],
['1039648061', '1400000', '320'],
['71725456', '650000', '98'],
['2431949521', '310000', '48'],
['2431951976', '375000', '36'],
['1037788703', '1500000', '420'],
['1041626725', '750000', '84'],
['2431949301', '383000', '46'],
['1042275221', '1700000', '220'],
['2431949320', '700000', '57'],
['1037950369', '190000', '35'],
['2431950812', '1400000', '165'],
['78741575', '450000', '75'],
['2431949315', '320000', '37'],
['74254161', '749947', '98'],
['2431952073', '750000', '90'],
['1747295477', '400000', '72'],
['1041097919', '1650000', '160'],
['2431845220', '160000', '30'],
['2431950804', '1400000', '128'],
['84722360', '190000', '27'],
['90213726', '980000', '120'],
['2431951319', '650000', '120'],
['64434303', '790000', '137'],
['90701910', '630000', '93'],
['89989587', '395000', '65'],
['1039042768', '1340000', '152'],
['1037204170', '580000', '99'],
['86600858', '610000', '96'],
['95262147', '449000', '74'],
['1037329965', '260000', '38'],
['2431951314', '290000', '30'],
['1039888111', '580000', '96'],
['1821135474', '550000', '104'],
['1082285477', '640000', '90'],
['1082685482', '640000', '100'],
['1039330282', '120000', '55'],
['1039330112', '455000', '48'],
['1041392133', '2500000', '528'],
['2431952078', '310000', '42'],
['1042883481', '580000', '68'],
['84985723', '35000', '30'],
['2431949298', '340000', '38'],
['85272968', '1650000', '264'],
['95155118', '370000', '65'],
['94644843', '650000', '98'],
['1042883484', '320000', '48'],
['2431949512', '2500000', '243'],
['1042883482', '300000', '48'],
['75738797', '730000', '121'],
['92765282', '400000', '49'],
['1038666082', '690000', '97'],
['1042356705', '580000', '95'],
['85852417', '630000', '96'],
['76668550', '630000', '0'],
['2431947344', '280000', '30'],
['2431657135', '395000', '72'],
['1038599890', '3100000', '348'],
['88727088', '610000', '90'],
['73064036', '280000', '63'],
['2431946559', '230000', '31'],
['1042431873', '950000', '135'],
['1177115476', '1000000', '128'],
['85852850', '620000', '90'],
['1039330166', '295000', '33'],
['1041050031', '450000', '49'],
['1952805492', '749000', '175'],
['85852575', '725000', '85'],
['2430242401', '900000', '115'],
['85577448', '616000', '96'],
['1038601361', '350000', '88'],
['93634540', '495000', '90'],
['1748695473', '470000', '65'],
['82166813', '395000', '49'],
['86204382', '980000', '114'],
['94972997', '770000', '96'],
['1040600226', '600000', '50'],
['1343445489', '600000', '90'],
['89210036', '650000', '100'],
['75879921', '630000', '100'],
['77371417', '1500000', '420'],
['78741648', '1800000', '225'],
['88545112', '650000', '90'],
['2433056207', '950000', '142'],
['78588337', '650000', '85'],
['89209173', '610000', '99'],
['85576336', '480000', '98'],
['47699022', '389000', '72'],
['1203945474', '600000', '68'],
['1037831667', '470000', '65'],
['67936114', '790000', '123'],
['1414005489', '650000', '85'],
['2429148303', '898000', '140'],
['76952222', '646000', '75'],
['91714793', '630000', '110'],
['1037605101', '750000', '130'],
['92988882', '600000', '130'],
['88014927', '770000', '98'],
['1413875482', '770000', '96'],
['77285888', '680000', '84'],
['82180346', '640000', '96'],
['1414035478', '630000', '90'],
['1413965488', '610000', '99'],
['1431545481', '650000', '100'],
['75880618', '750000', '110'],
['92765234', '160000', '33'],
['2431485509', '610000', '96'],
['2431484083', '690000', '100'],
['1039780085', '360000', '40'],
['1042264766', '640000', '90'],
['2431484088', '629000', '98'],
['86001940', '630000', '96'],
['58480984', '4500000', '420'],
['85273223', '1850000', '264'],
['78627766', '500000', '75'],
['2428184913', '1300000', '220'],
['90668469', '650000', '104'],
['69584369', '35000', '20'],
['2086165473', '650000', '84'],
['1225705480', '1990000', '240'],
['94848014', '770000', '96'],
['92246368', '550000', '97'],
['2428187373', '1800000', '274'],
['2431484895', '590000', '96'],
['1414045476', '650000', '90'],
['1413975475', '510000', '75'],
['85577226', '170000', '0'],
['1040509043', '2800000', '245'],
['74614728', '920000', '135'],
['92423430', '1990000', '243'],
['75570089', '280000', '31'],
['90668551', '790000', '124'],
['1880835492', '550000', '76'],
['2428528297', '480000', '74'],
['91839738', '790000', '124'],
['1037835784', '720000', '167'],
['2428482678', '525000', '68'],
['1041095314', '553097', '48'],
['2429149002', '650000', '94'],
['1880845489', '480000', '72'],
['85577750', '275000', '35'],
['92484961', '1845093', '110'],
['1952835474', '660000', '96'],
['75880234', '1900000', '246'],
['2431485512', '480000', '72'],
['85577763', '377615', '33'],
['92988991', '1490000', '280'],
['85576667', '1990000', '243'],
['2428586042', '330000', '33'],
['2432566640', '630000', '96'],
['1038442973', '760000', '135'],
['1528385474', '470000', '65'],
['92422604', '2050000', '243'],
['92421187', '2600000', '243'],
['1041910118', '630000', '89'],
['92421002', '2900000', '243'],
['83489858', '790000', '123'],
['2431670919', '730000', '96'],
['2428586966', '1150000', '96'],
['89210320', '630000', '90'],
['2428236081', '600000', '95'],
['1880925479', '650000', '90'],
['94747603', '599000', '90'],
['1037291389', '685000', '95'],
['75904829', '2200000', '246'],
['1484935478', '650000', '106'],
['1039886686', '1400000', '165'],
['75881288', '1490000', '280'],
['1039498586', '2500000', '243'],
['80271209', '950000', '135'],
['1039488125', '2200000', '450'],
['85576514', '1389401', '120'],
['65573825', '550000', '61'],
['2431485782', '790000', '124'],
['80019739', '600000', '120'],
['74510279', '2400000', '364'],
['93153480', '1650000', '400'],
['90491966', '760000', '135'],
['2431696085', '1800000', '500'],
['78528529', '650000', '85'],
['2428586964', '330000', '61'],
['1039787948', '700000', '84'],
['42819978', '470000', '65'],
['1039498405', '260000', '38'],
['85159040', '680000', '85'],
['90491386', '525000', '68'],
['46998386', '1785000', '246'],
['1037092812', '580000', '105'],
['1438905492', '1600000', '180'],
['80863946', '620000', '84'],
['1792165478', '1950000', '420'],
['1039498627', '580000', '120'],
['65542357', '1690000', '243'],
['65573942', '900000', '98'],
['1042026102', '680000', '96'],
['1880885481', '1500000', '155'],
['2427593803', '630000', '84'],
['2427593136', '1000000', '120'],
['2427596003', '525000', '120'],
['1127385478', '600000', '84'],
['1039498607', '1600000', '180'],
['2432061409', '460000', '100'],
['2432992575', '850000', '140'],
['1039340798', '515000', '89'],
['69601696', '650000', '90'],
['1070785477', '720000', '100'],
['90491810', '650000', '96'],
['94651950', '1790000', '246'],
['1038293980', '900000', '135'],
['71079630', '580000', '120'],
['2430880493', '660000', '86'],
['2429147398', '480000', '72'],
['95211347', '780000', '147'],
['2427597088', '525000', '73'],
['90491529', '1300000', '178'],
['90491463', '2000000', '396'],
['82195578', '850000', '163'],
['2428186288', '1510000', '151'],
['2067195480', '680000', '110'],
['2430393175', '688000', '96'],
['1480755515', '430000', '65'],
['71715025', '615000', '90'],
['70509450', '655000', '98'],
['1039498452', '1100000', '114'],
['2430177792', '1650000', '243'],
['78265517', '630000', '98'],
['1480755522', '1300000', '186'],
['1037970834', '590000', '96'],
['90492050', '2600000', '390'],
['2428186689', '530000', '104'],
['2114665497', '800000', '147'],
['85577335', '195000', '0'],
['76919587', '630000', '96'],
['1253585473', '2600000', '240'],
['1041501759', '1250000', '220'],
['82950993', '440000', '71'],
['2428655525', '1100000', '105'],
['2429147393', '420000', '68'],
['1037970924', '880000', '90'],
['90491356', '880000', '130'],
['67497363', '650000', '92'],
['80798952', '685000', '85'],
['69585179', '435000', '72'],
['68704026', '625000', '98'],
['75879800', '455000', '48'],
['1042026086', '480000', '100'],
['75879543', '295000', '33'],
['93299734', '165000', '40'],
['2431444798', '550000', '68'],
['71673491', '430000', '72'],
['1037970811', '650000', '104'],
['1040853157', '300000', '54'],
['1880845478', '2600000', '243'],
['85470015', '770000', '97'],
['1039340563', '460000', '72'],
['90491401', '2500000', '210'],
['1480735490', '400000', '75'],
['2114565512', '300000', '31'],
['2429145842', '2600000', '250'],
['2427594031', '180000', '23'],
['2427595026', '180000', '23'],
['62964141', '550000', '88'],
['2427596018', '2300000', '243'],
['1037970944', '770000', '96'],
['2427593134', '207000', '15'],
['2427596509', '1990000', '243'],
['2067155481', '650000', '95'],
['90491442', '155000', '29'],
['1480685485', '660000', '95'],
['64165462', '920000', '135'],
['90491301', '440000', '36'],
['2427596505', '2600000', '243'],
['1480965477', '650000', '95'],
['2427592839', '2900000', '243'],
['2427595086', '345000', '37'],
['92834167', '350000', '38'],
['2114695475', '1700000', '190'],
['2427594026', '1510000', '151'],
['1039488145', '2000000', '230'],
['63935264', '720000', '96'],
['2428579112', '290000', '48'],
['1480825495', '1500000', '218'],
['1366745473', '640000', '90'],
['2429147843', '300000', '30'],
['1038293964', '690000', '135'],
['2429145832', '330000', '70'],
['64746873', '850000', '135'],
['1480785521', '430000', '70'],
['1037970946', '1260000', '152'],
['81554472', '280000', '32'],
['1039107035', '190000', '15'],
['1480885501', '870000', '145'],
['93459310', '570000', '90'],
['2429145835', '200000', '32'],
['1038446548', '820000', '124'],
['2429149895', '1950000', '245'],
['1480925497', '900000', '145'],
['1038446554', '790000', '124'],
['1482525487', '500000', '65'],
['86162024', '350000', '36'],
['1037970746', '1990000', '243'],
['2433240691', '1330000', '150'],
['2429149897', '2200000', '300'],
['1037971044', '2600000', '243'],
['90491809', '155000', '32'],
['1037581472', '850000', '136'],
['65725596', '260000', '38'],
['62964117', '950000', '142'],
['49603559', '650000', '96'],
['62964410', '560000', '78'],
['64946672', '1870000', '180'],
['1481035480', '450000', '70'],
['2432990799', '2300000', '444'],
['40691536', '780000', '150'],
['62964163', '950000', '142'],
['1042026082', '295000', '33'],
['1037845987', '170000', '33'],
['62964136', '1800000', '285'],
['1481015480', '370000', '45'],
['88186429', '240000', '30'],
['62526507', '344674', '34'],
['62964313', '1250000', '180'],
['62964416', '550000', '98'],
['1480975489', '270000', '55'],
['1037971077', '650000', '130'],
['2429150680', '650000', '96'],
['1039106776', '520000', '72'],
['2429147156', '300000', '68'],
['1480935473', '1350000', '260'],
['62964191', '1400000', '180'],
['1480875482', '460000', '110'],
['85159336', '295000', '33'],
['1039106817', '2300000', '243'],
['1037970762', '2050000', '243'],
['1041336989', '2500000', '243'],
['1038774882', '540000', '70'],
['1042782153', '2900000', '245'],
['84425773', '2500000', '243'],
['80886785', '790000', '100'],
['89362423', '385000', '37'],
['1039449429', '540000', '150'],
['71681587', '430000', '62'],
['64494206', '2200000', '243'],
['91195315', '790000', '124'],
['62963928', '450000', '71'],
['62964074', '1690000', '243'],
['1480655487', '2500000', '210'],
['1042026138', '455000', '49'],
['63993646', '1100000', '142'],
['2429752174', '270000', '31'],
['1042693729', '698000', '85'],
['62964400', '1150000', '180'],
['2429147145', '480000', '60'],
['62964077', '990000', '142'],
['1037095627', '420000', '67'],
['1037970981', '155000', '29'],
['1037970927', '2000000', '350'],
['86301698', '1250000', '100'],
['62964219', '1300000', '285'],
['62964387', '950000', '142'],
['93234832', '210000', '35'],
['1480685496', '2200000', '420'],
['91195624', '1314000', '143'],
['95250297', '700000', '96'],
['62964325', '1150000', '180'],
['2431033682', '860000', '110'],
['62964081', '2450000', '355'],
['62964379', '450000', '71'],
['1037971007', '250000', '35'],
['71478561', '375000', '65'],
['91195833', '813424', '143'],
['2429150774', '528000', '68'],
['1480655484', '1200000', '200'],
['1480715507', '120000', '21'],
['2427596491', '2500000', '350'],
['1480715531', '120000', '28'],
['85159189', '455000', '50'],
['1480955491', '300000', '60'],
['71696055', '280000', '33'],
['1039107055', '395000', '49'],
['1481025488', '1150000', '220'],
['82983052', '700000', '118'],
['1037971066', '195000', '35'],
['93231645', '600000', '100'],
['95168610', '330000', '50'],
['1037971020', '2600000', '400'],
['79132369', '750000', '110'],
['62964231', '292726', '46'],
['1037971052', '2900000', '243'],
['1480935489', '2600000', '245'],
['2427597074', '680000', '97'],
['2427593419', '350000', '65'],
['62964409', '1400000', '180'],
['2427595926', '650000', '86'],
['2427593141', '600000', '140'],
['2427596591', '450000', '76'],
['2427593152', '630000', '97'],
['91195201', '700000', '96'],
['1042693728', '720000', '96'],
['2432856093', '1400000', '166'],
['1039488124', '2800000', '500'],
['1480905481', '550000', '50'],
['2427596981', '400000', '74'],
['2427592962', '625000', '90'],
['93232429', '475000', '100'],
['2427591745', '3060000', '317'],
['2427591738', '165000', '27'],
['93232044', '610000', '96'],
['78800045', '450000', '85'],
['62964374', '1900000', '600'],
['1480695501', '200000', '21'],
['80507853', '340000', '50'],
['79909771', '380000', '65'],
['2427596883', '640000', '70'],
['93231562', '790000', '128'],
['1038281949', '395000', '48'],
['1480975490', '650000', '50'],
['1480995481', '130000', '24'],
['91195140', '315000', '75'],
['78614303', '3100000', '415'],
['93718709', '1870000', '252'],
['1037644970', '800000', '135'],
['1037970847', '690000', '71'],
['93235055', '160000', '26'],
['2427592823', '165000', '27'],
['89505321', '710000', '58'],
['62526269', '1840000', '243'],
['77996987', '175000', '33'],
['1037718524', '271200', '52'],
['1037416392', '350000', '37'],
['86478131', '353626', '63'],
['1042515046', '395000', '48'],
['91193405', '2000000', '300'],
['1481025475', '5000000', '562'],
['2427596333', '380000', '74'],
['1042782210', '1990000', '167'],
['1037614883', '900000', '178'],
['1039106763', '300000', '47'],
['1037673561', '260000', '38'],
['78609518', '250000', '30'],
['93232394', '250000', '47'],
['82758333', '490000', '50'],
['1037918146', '390000', '42'],
['85123097', '630000', '1116'],
['62526303', '750000', '135'],
['1953545487', '725000', '125']]

colors = np.random.rand(len(v))
x = np.asarray([i[2] for i in v], dtype=np.float64)
y = np.asarray([i[1] for i in v], dtype=np.float64)
dot_area = [6 for i in y]
plt.scatter(x, y, s=dot_area, c=colors)
A = np.vstack([x, np.ones(len(x))]).T
m, c = np.linalg.lstsq(A, y, rcond=None)[0]
print(m, c)
plt.plot(x, m*x + c, 'r', label='Fitted line')
plt.legend()
plt.show()