import wntr

def drawnode(inp, node_list):
    wn = wntr.network.WaterNetworkModel(inp)
    nodeatrr = {'10':1 ,'11': 2 ,'12':3 ,'13': 4, '14': 5, '15': 6 ,'16': 7}
    nodeList = ['10','11','12','13','14','15','16']
    ky8node = ['J-1001','J-1037','J-1039','J-1041','J-1049','J-1051','J-1058','J-1074','J-1075','J-1090','J-1115','J-1117','J-1123','J-1138','J-118','J-1193','J-1215','J-1237','J-1243','J-1253','J-1256','J-1270','J-1277','J-1292','J-1314','J-153','J-185','J-205','J-282','J-285','J-316','J-337','J-347','J-360','J-450','J-451','J-569','J-580','J-582','J-594','J-603','J-61','J-65','J-677','J-683','J-727','J-744','J-773','J-816','J-844','J-870','J-874','J-892','J-920','J-936','J-947','J-995']
    cs1 = ['52026', '25886', '52353', '28378', '13852', '14894', '51780', '52968', '10034', '52736', '44885', '45758', '3524', '18699', '28179', '14422', '52667', '29459', '52576', '10087', '21912', '33281', '52378', '7266', '21169', '22689', '32416', '14370', '51666', '52074', '3106', '22848', '57134', '28679', '19856', '52668', '27854', '11810', '131', '55699', '52595', '55680', '31025', '11664', '16887', '36597', '43592', '52518', '52694', '28036', '36931', '41661', '28433', '39320', '47351', '685', '32805', '2629', '13808', '27936', '30809', '43081', '17598', '24781', '1700', '27370', '27469', '18539', '12175', '35702', '52432', '52596', '33150', '21321', '16505', '52824', '10362', '35899', '11458', '59635']
    cs2 = ['46940', '53562', '37175', '45596', '29754', '35748', '56903', '48941', '22977', '37582', '44459', '43888', '43264', '12026', '44004', '33876', '49388', '31316', '54923', '31510', '36938', '20518', '56091', '18275', '41857', '12147', '37304', '53318', '57505', '20868', '35515', '49550', '28499', '24811', '37897', '40553', '32550', '22849', '37554', '45679', '9342', '15339', '41267', '32890', '24865', '41958', '10677', '27607', '56463', '40239', '24074', '8181', '30294', '11267', '37039', '12196', '16170', '9497', '39886', '39797', '36379', '20297', '13101', '4374', '17647', '12756', '17132', '7897', '2621', '828', '7815', '13046', '1502', '3780', '12708', '59000', '839', '1017', '59091', '28288' ]
    cs3 = ['55794', '37533', '42182', '41030', '40511', '25053', '45139', '30169', '40928', '54985', '44384', '49142', '7802', '55898', '52224', '12857', '800', '283', '12103', '3726', '8947', '18662', '6416', '25190', '57032', '3968', '38267', '10446', '33712', '30227', '38535', '23274', '47957', '15151', '1302', '24166', '1019', '14408', '53883', '10490', '1490', '59581', '57207', '15115', '23277', '57429', '27319', '17078', '22824', '23824', '7610', '25803', '587', '1115', '2604', '36610', '31730', '44133', '27167', '53296', '8288', '20484', '2654', '17128', '52543', '31499', '44640', '59815', '24807', '5009', '999', '33663', '49190', '40506', '55375', '11116', '37118', '41888', '32118', '17775']
    cs4 = ["44885","1607", "1742", "2054", "3750", "3887", "37174", "45039", "47480", "47625","47717","47913","52590","52616","52634","52650","52707","52740","52774","52776"]
    cs5 = ["45500-A","45500-B","4779","4782","4790","4791","4793","4816","4825",'4828','4837','4848','4849','4858','4859','4864','4865','4877','4878','4879','4909','4910','4912','4921','4923','4933','4934','4958','4959','4966','4967','4968','4978','4985','4986','5002','5012','5014','5030','5042','5058','5061','5086','5088','5096','5097','5100','5101','5131','5132','5134','5559']
    cs6 = ['25438', '1992', '10395', '10971', '14603', '15151', '15152', '15159', '15338', '17153', '17548', '17669', '17815', '18043', '18329', '18395', '20314', '25789', '28161', '28267', '28633', '28779', '28925', '29001', '32677', '42443', '46766', '47158', '47217', '47422', '48757', '52489', '52795', '52846', '52952', '53119', '53123', '53179', '53195', '53198', '53210', '53266', '53269', '53353', '53402', '53413', '53434', '53450', '53477', '53496', '53527', '53534', '53578', '53638', '53673', '53704', '53789', '53792', '53803', '53813', '53819', '53823', '53837', '53852', '53873', '53889', '53955', '53974', '53983', '54155', '54182', '54212', '54242', '54276', '54399', '54417', '54435', '54481', '54516', '54570', '54581', '54599', '54676', '54717', '54952', '54987', '55066', '55087', '55192', '55239', '55356', '55440', '55498', '55508', '55526', '55530', '55531', '55532', '56419', '58925', '59827', '59835']
    cs7 = ['54284', '53266', '22342', '17190', '15797', '18955', '42204', '42443', '120869', '53520', '48836', '57256', '41986', '57236', '53943', '16482', '49080', '21583', '48860', '55086', '53602', '53490', '19263', '55336', '1811', '54382', '22984', '26705', '31280', '120871', '41063', '57210', '19413', '18003', '32794', '20631', '22507', '16279', '31421', '53803', '21646', '120877', '53540', '21637', '31345', '52771', '53531', '51866', '21546', '53189', '1140', '47486', '1573', '52194', '21661', '13071', '21628', '21580', '59562', '120873', '18014', '55057', '23013', '55515', '38365', '41825', '22627', '19118', '49377', '23426', '57500', '48910', '53496', '55975', '21013', '963', '19361', '55802', '40957', '15158', '49602', '32062', '19412', '18633', '49633', '23410', '15877', '31848', '31962', '49463', '54287', '21541', '53711', '53720', '52937', '19911', '53311', '21647', '31837', '19214', '49584', '54987', '31758', '20381', '58945', '21640', '48692', '49296', '54772', '1564', '24444', '20131', '11862', '47846', '27125', '22567', '37058', '31265', '17043', '21452', '20227', '22571', '49340', '49431', '53008', '120875', '48945', '1694', '21664', '27081', '31234', '21657', '26998', '21276', '360', '54138', '409', '26654', '32597', '54352', '31226', '27109', '54655', '47905', '21482', '26407', '15834', '20136', '16838', '19387', '31366', '31371', '16591', '21616', '832', '18380', '36267', '748', '55512', '21620', '97', '21354', '27259', '39143', '27522', '17297', '52749', '18839', '53369', '59386', '54646', '22931', '55837', '27252', '55445', '42200', '19506', '21609', '42108', '27108', '49284', '16471', '615', '21486', '54953', '32683', '21489', '22502', '54835', '59449', '1178', '21630', '22619', '34064', '9464', '54014', '19882', '668', '47502', '15937', '30538', '21384', '43250', '53423', '25682', '59353', '53622', '34562', '21608', '53239', '22349', '22492', '655', '53561', '56426', '38217', '57006', '21284', '49466', '54951', '55994', '1685', '27410', '57458', '49421', '19204', '25621', '54979', '51895', '22560', '15846', '48974', '2717', '53160', '26753', '22369', '933', '53998', '32419', '825', '49613', '22478', '14777', '45276', '53722', '17819', '53343', '39040', '59902', '57235', '21081', '25422', '31259', '55990', '18333', '48935', '7159', '55065', '59616', '56720', '888', '34250', '15935', '21532', '48889', '42088', '38371', '19895', '21301', '21625', '54000', '53922', '31819', '26151', '59022', '40219', '31383', '49498', '53662', '53237', '31353', '22643', '31293', '31291', '53317', '57377', '54326', '55467', '54851', '22584', '42016', '46182', '15047', '22739', '21629', '49260', '31854', '14003', '21726', '19543', '8948', '54106', '18995', '22727', '47939', '15408', '49217', '1992', '31414', '59637', '21607', '53644', '40793', '35070', '7798', '7707', '42085', '15983', '819', '21634', '19097', '53989', '19232', '8245', '53753', '49144', '31638', '14840', '39278', '53626', '42308', '21765', '52433', '53017', '42089', '54945', '37112', '41726', '55306', '54012', '47112', '45582', '21557', '39300', '44349', '19172', '39677', '26762', '56415', '31284', '37951', '53261', '49610', '52714', '863', '21084', '53122', '49611', '27077', '55527', '21210', '53419', '21852', '21728', '52795', '52502', '21796', '21788', '46806', '21830', '21858', '37898', '19898', '31955', '1845', '16717', '38372', '49042', '39065', '28155', '10189', '47423', '31358', '21083', '19134', '265', '22737', '54020', '53959', '49367', '32861', '34527', '56718', '49612', '49600', '21372', '22459', '48998', '53988', '47111', '40577', '52926', '54288', '31518', '18913', '26716', '1233', '21586', '25776', '20323', '45724', '54619', '28269', '55946', '59113', '26993', '31160', '53431', '56375', '37540', '59085', '57636', '37289', '21297', '49249', '47710', '22382', '21731', '53190', '53162', '22605', '59026', '31960', '42087', '53058', '18578', '21573', '15108', '22901', '22464', '52210', '20316', '59137', '55703', '49564', '59513', '28267', '49408', '40962', '31359', '5740', '53665', '17921', '21342', '48732', '21590', '21052', '46766', '26473', '53731', '32080', '18818', '25707', '32805', '49607', '54151', '49283', '31471', '47996', '34364', '52938', '59270', '15933', '28368', '31878', '22448', '20555', '1665', '53213', '52851', '56063', '40065', '54415', '38163', '42817', '38620', '59792', '857', '52629', '35577', '31841', '31370', '31473', '22622', '16275', '31303', '53095', '21401', '34524', '53342', '51415', '58943', '22489', '54581', '55858', '22394', '26561', '1489', '19167', '48913', '34288', '913', '17419', '49615', '45009', '1399', '32819', '48946', '25072', '40164', '27248', '23111', '27412', '49007', '47295', '17656', '19661', '15397', '28416', '39809', '53492', '51876', '27719', '15953', '54358', '36668', '49484', '27250', '26652', '2325', '25345', '49334', '20684', '7796', '59814', '21326', '17298', '6130', '22578', '12132', '15906', '47826', '21572', '53099', '37238', '53833', '32651', '53522', '48884', '22582', '48897', '22592', '35585', '18502', '52864', '21603', '42450', '16938', '17165', '53405', '54977', '54175', '31341', '47199', '49145', '12114', '48971', '21587', '53287', '57201', '32307', '15366', '42083', '53920', '47760', '39142', '24792', '15168', '39587', '40958', '31354', '55349', '33590', '26150', '22499', '38206', '19400', '1090', '23911', '53071', '57518', '54040', '22618', '21795', '15939', '53130', '54617', '7069', '54455', '31959', '29127', '37949', '49092', '53821', '19201', '57407', '10987', '21631', '59842', '54523', '11305', '23822', '27908', '22474', '20906', '55202', '7726', '27329', '1105', '37033', '17646', '57198', '11640', '31592', '55672', '21506', '59252', '27986', '16826', '35317', '21375', '25373', '26421', '48729', '24630', '28596', '36326', '14879', '15810', '21419', '27127', '53914', '40249', '28096', '21521', '21332', '2863', '20538', '55624', '14198', '49345', '42828', '15785', '28639', '59175', '31589', '31294', '22385', '38952', '38798', '11350', '15804', '27338', '57635', '11372', '3600', '54209', '16077', '21451', '52813', '25453', '54802', '36993', '55812', '16813', '53656', '18152', '22494', '27047', '25737', '18897', '42593', '15549', '53623', '21561', '16845', '41724', '19423', '39336', '52604', '11559', '19774', '52774', '49299', '16874', '38295', '19227', '39209', '59349', '22501', '30115', '34561', '27353', '47822', '47436', '47164', '39270', '46845', '16032', '36873', '22424', '14356', '55058', '56083', '15494', '55821', '44979', '1100', '53473', '53976', '21269', '53133', '28480', '55337', '22574', '21708', '49206', '23414', '27574', '54300', '24714', '39847', '39332', '44684', '42842', '19312', '10853', '54255', '40025', '10323', '49730', '47301', '3867', '19531', '22891', '40270', '54153', '31869', '20650', '57323', '19324', '53428', '24712', '59514', '52171', '34193', '13045', '20848', '594', '19705', '41962', '15451', '54044', '15468', '15870', '21551', '14837', '22729', '21780', '49516', '976', '26824', '56696', '36502', '19664', '49372', '36899', '39446', '19509', '40008', '26706', '59847', '39663', '17031', '37170', '53146', '49660', '14588', '17919', '25123', '22724', '52808', '53863', '39710', '42841', '24640', '17437', '16896', '36563', '55518', '19708', '40186', '46809', '55525', '49581', '29656', '56624', '22327', '17155', '53849', '55299', '47964', '52805', '49008', '7061', '15786', '53655', '26335', '52898', '21605', '7982', '54648', '59806', '17598', '22441', '55741', '35609', '36796', '1467', '28910', '19215', '42081', '31507', '38853', '11069', '17076', '49605', '30482', '27600', '7958', '17640', '27539', '27094', '27312', '26617', '55562', '25014', '41710', '18216', '28325', '14693', '14603', '22653', '32984', '55750', '30372', '53179', '26117', '19899', '25332', '1948', '26338', '28632', '12488', '32753', '53969', '19393', '32343', '28203', '34466', '4436', '36863', '15025', '21549', '48881', '31260', '14838', '13408', '54022', '16652', '22376', '59092', '21645', '20632', '1486', '52457', '49069', '25349', '41229', '19648', '31978', '54715', '15156', '19268', '38537', '10394', '19619', '39356', '24737', '14607', '19335', '39008', '28870', '53879', '14386', '17857', '22693', '22808', '20883', '37651', '33911', '28159', '22430', '56531', '52403', '18061', '12267', '15129', '47264', '54712', '11005', '38209', '56021', '21033', '10962', '55770', '33009', '39786', '31933', '33592', '31048', '39141', '21779', '55621', '48950', '21660', '31639', '6004', '1088', '1999', '53091', '51797', '47187', '37504', '25350', '21431', '47750', '18359', '18894', '53070', '15940', '22636', '28660', '14600', '10530', '19510', '56119', '17516', '23850', '15638', '15236', '31472', '3488', '23421', '42079', '42180', '19340', '14671', '36300', '45844', '55131', '36641', '52862', '53637', '39146', '2910', '15730', '34104', '16175', '54152', '21574', '1888', '53727', '8586', '35189', '21841', '55991', '47369', '36337', '21261', '53798', '39010', '2676', '22987', '53945', '21350', '21145', '19478', '53533', '22435', '17892', '27944', '19566', '39382', '49231', '27084', '17074', '40002', '26432', '30407', '11752', '21675', '37035', '31583', '29452', '3701', '16070', '28595', '52999', '11263', '16191', '19854', '40622', '40448', '32202', '12401', '22565', '59230', '1769', '56252', '3914', '12767', '47922', '22396', '59844', '21286', '15923', '31156', '11360', '19654', '3938', '47947', '17746', '56485', '59205', '36714', '53766', '39951', '10648', '52931', '28371', '49191', '36806', '1537', '36545', '1964', '47318', '42910', '18308', '47186', '32886', '7931', '33558', '59468', '27216', '1949', '36565', '21345', '2889', '35974', '25662', '31752', '12575', '41669', '19238', '10395', '21571', '54894', '24283', '17163', '43661', '22689', '17392', '3794', '28245', '16108', '30234', '57488', '21651', '42528', '31996', '39460', '15202', '39289', '47432', '16177', '36566', '18105', '31575', '24721', '40257', '18065', '9668', '17883', '59789', '31457', '59278', '54917', '26984', '31381', '52487', '52977', '23862', '19562', '21623', '31387', '22725', '23420', '2093', '17932', '16133', '24470', '22475', '44889', '12773', '16688', '25696', '55636', '24297', '54883', '29799', '15398', '49481', '52666', '52674', '52130', '31405', '53378', '21622', '47553', '26778', '20221', '56528', '41844', '31459', '39455', '59207', '28484', '21599', '22871', '38115', '56637', '54406', '47314', '27377', '42571', '18549', '25013', '30397', '1472', '6563', '56749', '19243', '39753', '23417', '7689', '41046', '15198', '49601', '52056', '47786', '27760', '10296', '24682', '56676', '24228', '3817', '17138', '29629', '17465', '30414', '21234', '29627', '27314', '19424', '1720', '29908', '14637', '19427', '30401', '25879', '56246', '22410', '29798', '17073', '5436', '8896', '26914', '12534', '38843', '29645', '29662', '26365', '34804', '25699', '21082', '40899', '48936', '53289', '52906', '53279', '21437', '27480', '30398', '57025', '28328', '31723', '42164', '25467', '17221', '10101', '33594', '16560', '57568', '33581', '31135', '49220', '52971', '54659', '32040', '16072', '53873', '53589', '3487', '13322', '53341', '28661', '21263', '26116', '17519', '30316', '47232', '24493', '21718', '18327', '20241', '31452', '54898', '41602', '52055', '40202', '47480', '56390', '52387', '37251', '6628', '19333', '16265', '3640', '15830', '49091', '10990', '35923', '39675', '58926', '48917', '16090', '31743', '22324', '42555', '15792', '17551', '39689', '17721', '29751', '53424', '28592', '10155', '28193', '52335', '35164', '56460', '483', '47707', '31783', '25293', '16960', '55307', '40770', '31530', '16149', '15993', '52101', '36544', '45598', '31894', '40419', '40134', '43', '53088', '27427', '15951', '19514', '12332', '22336', '18696', '56362', '59680', '27435', '17981', '41029', '56432', '59713', '21300', '47597', '47161', '15701', '11861', '52832', '17550', '37976', '47131', '42306', '58983', '18328', '31374', '44868', '36328', '27320', '31526', '35173', '27448', '53448', '39279', '53382', '31562', '59199', '39288', '17021', '21491', '44920', '44761', '27680', '56213', '15157', '49455', '21006', '52533', '49152', '23854', '22585', '15475', '8106', '31735', '20735', '1559', '30348', '55453', '47373', '13061', '26452', '14479', '19847', '35010', '15938', '59167', '28924', '37763', '22566', '31401', '1548', '18048', '48739']
    # print(len(cs7))
    wntr.graphics.plot_network(wn, node_attribute=node_list, add_colorbar=False)


def indexTonode(nodeIndexList, nodeList):
    nodeResult = []
    for i in nodeIndexList:
        nodeResult.append(nodeList[i])
    return nodeResult


if __name__ == "__main__":
    inpfile = "ky8.inp"
    inpfile2 = "F:\\AWorkSpace\\Python-Learning-Data\\cs11021.inp"
    nodecsv = "F:\\AWorkSpace\\Python-Learning-Data\\simuNodes.csv"
    net3inp = "F:\\AWorkSpace\\Python-Learning-Data\\Net3.inp"
    nodelist = ['259', '231', '131', '209', '206', '184', '15', '151', '10', '217', '204', '601', '161', '239', '105']
    drawnode(net3inp, nodelist)
    '''
    import pandas as pd
    import numpy as np
    p = pd.read_csv("F:\\AWorkSpace\\Python-Learning-Data\\weightsorted.csv")
    print(list(p["nodeName"]))
    p_3628 = list(p["nodeName"])[0: 3628]
    print(len(p_3628))
    drawnode(inpfile2, p_3628)'''
