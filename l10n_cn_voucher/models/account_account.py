# -*- coding: utf-8 -*-
# Copyright 2017 Jarvis (www.odoomod.com)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields, api, SUPERUSER_ID


class AccountAccount(models.Model):
    _inherit = 'account.account'

    balance_direction = fields.Selection([('debit', '借方'), ('credit', '贷方')], '余额方向')

    def init(self, cr):
        account_config = [
            ['1001', '库存现金', '借方', ''],
            ['1002', '银行存款', '借方', ''],
            ['1003', '存放中央银行款项', '借方', ''],
            ['1011', '存放同业', '借方', ''],
            ['1012', '其他货币资金', '借方', ''],
            ['1021', '结算备付金', '借方', ''],
            ['1031', '存出保证金', '借方', ''],
            ['1101', '交易性金融资产', '借方', ''],
            ['1111', '买入返售金融资产', '借方', ''],
            ['1121', '应收票据', '借方', ''],
            ['1122', '应收账款', '借方', ''],
            ['1123', '预付账款', '借方', ''],
            ['1131', '应收股利', '借方', ''],
            ['1132', '应收利息', '借方', ''],
            ['1201', '应收代位追偿款', '借方', ''],
            ['1211', '应收分保账款', '借方', ''],
            ['1212', '应收分保合同准备金', '借方', ''],
            ['1221', '其他应收款', '借方', ''],
            ['1231', '坏账准备', '贷方', ''],
            ['1301', '贴现资产', '借方', ''],
            ['1302', '拆出资金', '借方', ''],
            ['1303', '贷款', '借方', ''],
            ['1304', '贷款损失准备', '贷方', ''],
            ['1311', '代理兑付证券', '借方', ''],
            ['1321', '代理业务资产', '借方', ''],
            ['1401', '材料采购', '借方', ''],
            ['1402', '在途物资', '借方', ''],
            ['1403', '原材料', '借方', ''],
            ['1404', '材料成本差异', '借方', ''],
            ['1405', '库存商品', '借方', ''],
            ['1406', '发出商品', '借方', ''],
            ['1407', '商品进销差价', '借方', ''],
            ['1408', '委托加工物资', '借方', ''],
            ['1411', '周转材料', '借方', ''],
            ['1421', '消耗性生物资产', '借方', ''],
            ['1431', '贵金属', '借方', ''],
            ['1441', '抵债资产', '借方', ''],
            ['1451', '损余物资', '借方', ''],
            ['1461', '融资租赁资产', '借方', ''],
            ['1471', '存货跌价准备', '贷方', ''],
            ['1501', '持有至到期投资', '借方', ''],
            ['1502', '持有至到期投资减值准备', '贷方', ''],
            ['1503', '可供出售金融资产', '借方', ''],
            ['1511', '长期股权投资', '借方', ''],
            ['1512', '长期股权投资减值准备', '贷方', ''],
            ['1521', '投资性房地产', '借方', ''],
            ['1531', '长期应收款', '借方', ''],
            ['1532', '未实现融资收益', '贷方', ''],
            ['1541', '存出资本保证金', '借方', ''],
            ['1601', '固定资产', '借方', ''],
            ['1602', '累计折旧', '贷方', ''],
            ['1603', '固定资产减值准备', '贷方', ''],
            ['1604', '在建工程', '借方', ''],
            ['1605', '工程物资', '借方', ''],
            ['1606', '固定资产清理', '借方', ''],
            ['1611', '未担保余值', '借方', ''],
            ['1621', '生产性生物资产', '借方', ''],
            ['1622', '生产性生物资产累计折旧', '贷方', ''],
            ['1623', '公益性生物资产', '借方', ''],
            ['1631', '油气资产', '借方', ''],
            ['1632', '累计折耗', '贷方', ''],
            ['1701', '无形资产', '借方', ''],
            ['1702', '累计摊销', '贷方', ''],
            ['1703', '无形资产减值准备', '贷方', ''],
            ['1711', '商誉', '借方', ''],
            ['1801', '长期待摊费用', '借方', ''],
            ['1811', '递延所得税资产', '借方', ''],
            ['1821', '独立账户资产', '借方', ''],
            ['1901', '待处理财产损溢', '借方', ''],
            ['2001', '短期借款', '贷方', ''],
            ['2002', '存入保证金', '贷方', ''],
            ['2003', '拆入资金', '贷方', ''],
            ['2004', '向中央银行借款', '贷方', ''],
            ['2011', '吸收存款', '贷方', ''],
            ['2012', '同业存放', '贷方', ''],
            ['2021', '贴现负债', '贷方', ''],
            ['2101', '交易性金融负债', '贷方', ''],
            ['2111', '卖出回购金融资产款', '贷方', ''],
            ['2201', '应付票据', '贷方', ''],
            ['2202', '应付账款', '贷方', ''],
            ['2203', '预收账款', '贷方', ''],
            ['2211', '应付职工薪酬', '贷方', ''],
            ['2221', '应交税费', '贷方', ''],
            ['222101', '应交增值税', '贷方', '应交税费'],
            ['22210101', '进项税额', '贷方', '应交增值税'],
            ['22210102', '销项税额', '贷方', '应交增值税'],
            ['22210103', '出口退税', '贷方', '应交增值税'],
            ['22210104', '进项税额转出', '贷方', '应交增值税'],
            ['22210105', '已交税金', '贷方', '应交增值税'],
            ['222102', '应交城市维护建设税', '贷方', '应交税费'],
            ['222103', '应交教育费附加', '贷方', '应交税费'],
            ['222104', '应交车船税', '贷方', '应交税费'],
            ['222105', '应交房产税', '贷方', '应交税费'],
            ['222106', '应交城镇土地使用税', '贷方', '应交税费'],
            ['222107', '应交资源税', '贷方', '应交税费'],
            ['222108', '应交矿产资源税', '贷方', '应交税费'],
            ['222109', '应交企业所得税', '贷方', '应交税费'],
            ['2231', '应付利息', '贷方', ''],
            ['2232', '应付股利', '贷方', ''],
            ['2241', '其他应付款', '贷方', ''],
            ['2251', '应付保单红利', '贷方', ''],
            ['2261', '应付分保账款', '贷方', ''],
            ['2311', '代理买卖证券款', '贷方', ''],
            ['2312', '代理承销证券款', '贷方', ''],
            ['2313', '代理兑付证券款', '贷方', ''],
            ['2314', '代理业务负债', '贷方', ''],
            ['2401', '递延收益', '贷方', ''],
            ['2501', '长期借款', '贷方', ''],
            ['2502', '应付债券', '贷方', ''],
            ['2601', '未到期责任准备金', '贷方', ''],
            ['2602', '保险责任准备金', '贷方', ''],
            ['2611', '保户储金', '贷方', ''],
            ['2621', '独立账户负债', '贷方', ''],
            ['2701', '长期应付款', '贷方', ''],
            ['2702', '未确认融资费用', '借方', ''],
            ['2711', '专项应付款', '贷方', ''],
            ['2801', '预计负债', '贷方', ''],
            ['2901', '递延所得税负债', '贷方', ''],
            ['3001', '清算资金往来', '借方', ''],
            ['3002', '货币兑换', '借方', ''],
            ['3101', '衍生工具', '借方', ''],
            ['3201', '套期工具', '借方', ''],
            ['3202', '被套期项目', '借方', ''],
            ['4001', '实收资本', '贷方', ''],
            ['4002', '资本公积', '贷方', ''],
            ['4101', '盈余公积', '贷方', ''],
            ['4102', '一般风险准备', '贷方', ''],
            ['4103', '本年利润', '贷方', ''],
            ['4104', '利润分配', '贷方', ''],
            ['4201', '库存股', '贷方', ''],
            ['5001', '生产成本', '借方', ''],
            ['5101', '制造费用', '借方', ''],
            ['5201', '劳务成本', '借方', ''],
            ['5301', '研发支出', '借方', ''],
            ['5401', '工程施工', '借方', ''],
            ['5402', '工程结算', '借方', ''],
            ['5403', '机械作业', '借方', ''],
            ['6001', '主营业务收入', '贷方', ''],
            ['6011', '利息收入', '贷方', ''],
            ['6021', '手续费及佣金收入', '贷方', ''],
            ['6031', '保费收入', '贷方', ''],
            ['6041', '租赁收入', '贷方', ''],
            ['6051', '其他业务收入', '贷方', ''],
            ['6061', '汇兑损益', '贷方', ''],
            ['6101', '公允价值变动损益', '贷方', ''],
            ['6111', '投资收益', '贷方', ''],
            ['6201', '摊回保险责任准备金', '贷方', ''],
            ['6202', '摊回赔付支出', '贷方', ''],
            ['6203', '摊回分保费用', '贷方', ''],
            ['6301', '营业外收入', '贷方', ''],
            ['6401', '主营业务成本', '借方', ''],
            ['6402', '其他业务成本', '借方', ''],
            ['6403', '营业税金及附加', '借方', ''],
            ['6411', '利息支出', '借方', ''],
            ['6421', '手续费及佣金支出', '借方', ''],
            ['6501', '提取未到期责任准备金', '借方', ''],
            ['6502', '提取保险责任准备金', '借方', ''],
            ['6511', '赔付支出', '借方', ''],
            ['6521', '保单红利支出', '借方', ''],
            ['6531', '退保金', '借方', ''],
            ['6541', '分出保费', '借方', ''],
            ['6542', '分保费用', '借方', ''],
            ['6601', '销售费用', '借方', ''],
            ['6602', '管理费用', '借方', ''],
            ['6603', '财务费用', '借方', ''],
            ['6604', '勘探费用', '借方', ''],
            ['6701', '资产减值损失', '借方', ''],
            ['6711', '营业外支出', '借方', ''],
            ['6801', '所得税费用', '借方', ''],
            ['6901', '以前年度损益调整', '借方', ''],
        ]
        account_smb_config = [
            ['0', '会计科目', '', ''],
            ['1001', '库存现金', '借方', ''],
            ['1002', '银行存款', '借方', ''],
            ['1012', '其他货币资金', '借方', ''],
            ['1101', '短期投资', '借方', ''],
            ['110101', '股票', '借方', '短期投资'],
            ['110102', '债券', '借方', '短期投资'],
            ['110103', '基金', '借方', '短期投资'],
            ['110110', '其它', '借方', '短期投资'],
            ['1121', '应收票据', '借方', ''],
            ['1122', '应收账款', '借方', ''],
            ['1123', '预付账款', '借方', ''],
            ['1131', '应收股利', '借方', ''],
            ['1132', '应收利息', '借方', ''],
            ['1221', '其他应收款', '借方', ''],
            ['1401', '材料采购', '借方', ''],
            ['1402', '在途物资', '借方', ''],
            ['1403', '原材料', '借方', ''],
            ['1404', '材料成本差异', '借方', ''],
            ['1405', '库存商品', '借方', ''],
            ['1406', '发出商品', '借方', ''],
            ['1407', '商品进销差价', '借方', ''],
            ['1408', '委托加工物资', '借方', ''],
            ['1411', '周转材料', '借方', ''],
            ['1421', '消耗性生物资产', '借方', ''],
            ['1501', '长期债券投资', '借方', ''],
            ['1511', '长期股权投资', '借方', ''],
            ['1601', '固定资产', '借方', ''],
            ['1602', '累计折旧', '贷方', ''],
            ['1604', '在建工程', '借方', ''],
            ['1605', '工程物资', '借方', ''],
            ['1606', '固定资产清理', '借方', ''],
            ['1621', '生产性生物资产', '借方', ''],
            ['1622', '生产性生物资产累计折旧', '贷方', ''],
            ['1701', '无形资产', '借方', ''],
            ['1702', '累计摊销', '贷方', ''],
            ['1801', '长期待摊费用', '借方', ''],
            ['1901', '待处理财产损溢', '借方', ''],
            ['2001', '短期借款', '贷方', ''],
            ['2201', '应付票据', '贷方', ''],
            ['220102', '应付暂估', '贷方', '应付票据'],
            ['2202', '应付账款', '贷方', ''],
            ['2203', '预收账款', '贷方', ''],
            ['2211', '应付职工薪酬', '贷方', ''],
            ['221101', '应付职工工资', '贷方', '应付职工薪酬'],
            ['221102', '应付奖金、津贴和补贴', '贷方', '应付职工薪酬'],
            ['221103', '应付福利费', '贷方', '应付职工薪酬'],
            ['221104', '应付社会保险费', '贷方', '应付职工薪酬'],
            ['221105', '应付住房公积金', '贷方', '应付职工薪酬'],
            ['221106', '应付工会经费', '贷方', '应付职工薪酬'],
            ['221107', '应付教育经费', '贷方', '应付职工薪酬'],
            ['221108', '非货币性福利', '贷方', '应付职工薪酬'],
            ['221109', '辞退福利', '贷方', '应付职工薪酬'],
            ['221110', '其他应付职工薪酬', '贷方', '应付职工薪酬'],
            ['2221', '应交税费', '贷方', ''],
            ['222101', '应交增值税', '贷方', '应交税费'],
            ['22210101', '进项税额', '贷方', '应交增值税'],
            ['22210102', '已交税金', '贷方', '应交增值税'],
            ['22210103', '转出未交增值税', '贷方', '应交增值税'],
            ['22210104', '减免税款', '贷方', '应交增值税'],
            ['22210105', '销项税额', '贷方', '应交增值税'],
            ['22210106', '出口退税', '贷方', '应交增值税'],
            ['22210107', '进项税额转出', '贷方', '应交增值税'],
            ['22210108', '出口抵减内销产品应纳税额', '贷方', '应交增值税'],
            ['22210109', '转出多交增值税', '贷方', '应交增值税'],
            ['222102', '未交增值税', '贷方', '应交税费'],
            ['222103', '应交营业税', '贷方', '应交税费'],
            ['222104', '应交消费税', '贷方', '应交税费'],
            ['222105', '应交资源税', '贷方', '应交税费'],
            ['222106', '应交所得税', '贷方', '应交税费'],
            ['222107', '应交土地增值税', '贷方', '应交税费'],
            ['222108', '应交城市维护建设税', '贷方', '应交税费'],
            ['222109', '应交房产税', '贷方', '应交税费'],
            ['222110', '应交城镇土地使用税', '贷方', '应交税费'],
            ['222111', '应交车船使用税', '贷方', '应交税费'],
            ['222112', '应交个人所得税', '贷方', '应交税费'],
            ['222113', '教育费附加', '贷方', '应交税费'],
            ['222114', '矿产资源补偿费', '贷方', '应交税费'],
            ['222115', '排污费', '贷方', '应交税费'],
            ['2231', '应付利息', '贷方', ''],
            ['2232', '应付利润', '贷方', ''],
            ['2241', '其他应付款', '贷方', ''],
            ['2401', '递延收益', '贷方', ''],
            ['2501', '长期借款', '贷方', ''],
            ['2701', '长期应付款', '贷方', ''],
            ['3001', '实收资本', '贷方', ''],
            ['3002', '资本公积', '贷方', ''],
            ['3101', '盈余公积', '贷方', ''],
            ['310101', '法定盈余公积', '贷方', '盈余公积'],
            ['310102', '任意盈余公积', '贷方', '盈余公积'],
            ['3103', '本年利润', '贷方', ''],
            ['3104', '利润分配', '贷方', ''],
            ['310401', '其他转入', '贷方', '利润分配'],
            ['310402', '提取法定盈余公积', '贷方', '利润分配'],
            ['310403', '提取法定公益金', '贷方', '利润分配'],
            ['310404', '提取职工奖励及福利基金', '贷方', '利润分配'],
            ['310409', '提取任意盈余公积', '贷方', '利润分配'],
            ['310410', '应付利润', '贷方', '利润分配'],
            ['310415', '未分配利润', '贷方', '利润分配'],
            ['4001', '生产成本', '借方', ''],
            ['4101', '制造费用', '借方', ''],
            ['4301', '研发支出', '借方', ''],
            ['4401', '工程施工', '借方', ''],
            ['4403', '机械作业', '借方', ''],
            ['5001', '主营业务收入', '贷方', ''],
            ['5051', '其他业务收入', '贷方', ''],
            ['5111', '投资收益', '贷方', ''],
            ['5301', '营业外收入', '贷方', ''],
            ['530101', '非流动资产处置净收益', '贷方', '营业外收入'],
            ['530102', '政府补助', '贷方', '营业外收入'],
            ['530103', '捐赠收益', '贷方', '营业外收入'],
            ['530104', '盘盈收益', '贷方', '营业外收入'],
            ['530105', '确实无法偿付的应付账款', '贷方', '营业外收入'],
            ['530106', '已作坏账损失处理后又收回的应收账款', '贷方', '营业外收入'],
            ['530107', '出租包装物和商品的租金收入', '贷方', '营业外收入'],
            ['530108', '逾期未退包装物押金收益', '贷方', '营业外收入'],
            ['530109', '汇兑收益', '贷方', '营业外收入'],
            ['530110', '违约金收益', '贷方', '营业外收入'],
            ['530199', '其他营业外收入', '贷方', '营业外收入'],
            ['5401', '主营业务成本', '借方', ''],
            ['5402', '其他业务成本', '借方', ''],
            ['5403', '营业税金及附加', '借方', ''],
            ['5601', '销售费用', '借方', ''],
            ['560101', '销售人员职工薪酬', '借方', '销售费用'],
            ['560102', '商品维修费', '借方', '销售费用'],
            ['560103', '运输费', '借方', '销售费用'],
            ['560104', '装卸费', '借方', '销售费用'],
            ['560105', '包装费', '借方', '销售费用'],
            ['560106', '保险费', '借方', '销售费用'],
            ['560107', '广告费', '借方', '销售费用'],
            ['560108', '业务宣传费', '借方', '销售费用'],
            ['560109', '展览费', '借方', '销售费用'],
            ['560110', '运输合理损耗', '借方', '销售费用'],
            ['560111', '入库前挑选整理费', '借方', '销售费用'],
            ['560199', '其他销售费用', '借方', '销售费用'],
            ['5602', '管理费用', '借方', ''],
            ['560201', '管理人员职工薪酬', '借方', '管理费用'],
            ['560202', '办公费', '借方', '管理费用'],
            ['560203', '业务招待费', '借方', '管理费用'],
            ['560204', '员工福利', '借方', '管理费用'],
            ['560205', '修理费', '借方', '管理费用'],
            ['560206', '水电费', '借方', '管理费用'],
            ['560207', '差旅费', '借方', '管理费用'],
            ['560208', '周转材料摊销', '借方', '管理费用'],
            ['560209', '固定资产折旧费', '借方', '管理费用'],
            ['560210', '无形资产摊销费', '借方', '管理费用'],
            ['560211', '长期待摊费用摊销', '借方', '管理费用'],
            ['560212', '技术转让费', '借方', '管理费用'],
            ['560213', '财产保险费', '借方', '管理费用'],
            ['560214', '聘请中介机构费', '借方', '管理费用'],
            ['560215', '咨询费', '借方', '管理费用'],
            ['560216', '诉讼费', '借方', '管理费用'],
            ['560217', '研究费用', '借方', '管理费用'],
            ['560299', '其他管理费用', '借方', '管理费用'],
            ['5603', '财务费用', '借方', ''],
            ['560301', '利息费用', '借方', '财务费用'],
            ['560302', '汇兑损失', '借方', '财务费用'],
            ['560303', '银行手续费', '借方', '财务费用'],
            ['560304', '现金折扣', '借方', '财务费用'],
            ['5711', '营业外支出', '借方', ''],
            ['571101', '非流动资产处置净损失', '借方', '营业外支出'],
            ['571102', '赞助支出', '借方', '营业外支出'],
            ['571103', '捐赠支出', '借方', '营业外支出'],
            ['571104', '盘亏损失', '借方', '营业外支出'],
            ['571105', '坏账损失', '借方', '营业外支出'],
            ['571106', '存货毁损报废损失', '借方', '营业外支出'],
            ['571107', '无法收回的长期债券投资损失', '借方', '营业外支出'],
            ['571108', '无法收回的长期股权投资损失', '借方', '营业外支出'],
            ['571109', '自然灾害等不可抗力因素造成的损失', '借方', '营业外支出'],
            ['571110', '税收滞纳金', '借方', '营业外支出'],
            ['571111', '罚没损失', '借方', '营业外支出'],
            ['571199', '其他营业外支出', '借方', '营业外支出'],
            ['5801', '所得税费用', '借方', ''],
        ]
        try:
            account_account_obj = self.pool.get('account.account')
            debit_list, credit_list = [], []
            for c in account_config + account_smb_config:
                direction, value = c[2], c[1]
                if direction == '借方':
                    debit_list.append(value)
                elif direction == '贷方':
                    credit_list.append(value)
            ids = account_account_obj.search(cr, SUPERUSER_ID,
                                             [('name', 'in', debit_list), ('balance_direction', '=', None)])
            account_account_obj.write(cr, SUPERUSER_ID, ids, {'balance_direction': 'debit'})
            ids = account_account_obj.search(cr, SUPERUSER_ID,
                                             [('name', 'in', credit_list), ('balance_direction', '=', None)])
            account_account_obj.write(cr, SUPERUSER_ID, ids, {'balance_direction': 'credit'})
        except:
            pass
