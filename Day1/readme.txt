作业1、登录接口
	输入用户名密码
	认证成功后显示欢迎信息
	输错三次后锁定
脚本名：
	login.py
数据文件：
	user.log
	格式如下所示，一共就两个用户分别名为Thomas和Rogan：
		＃用户名，密码，状态
		Thomas,123456,unlock
		Rogan,123,unlock
说明：
	# 本段代码假设用户名输入是正确的,密码可能不正确
	# 本段代码假设连续多次输入的姓名是相同的,直到登录成功或者被锁住为止
测试例子：
	input your name:Rogan
	input your password:123
	Welcome, Rogan
	input your name:Thomas
	input your password:123456
	Welcome, Thomas
	input your name:Rogan
	input your password:12
	your passwd is incorrect
	input your name:Rogan
	input your password:12
	your passwd is incorrect
	input your name:Rogan
	input your password:12
	sorry, you input wrong password 3 times, you'll be locked!
	input your name:Rogan
	input your password:123
	sorry, you're locked
	input your name:Thomas
	input your password:123
	your passwd is incorrect
	input your name:Thomas
	input your password:123456
	Welcome, Thomas
	input your name:

作业2、多级菜单
	三级菜单
	可依次选择进入各子菜单
	所需要新知识点：列表、字典
脚本名：
	three_level_menu.py
说明：
	# 本段代码不需要使用复杂的循环就可以实现三级菜单的功能呢
	# state保存一种状态,[0,1,None]表示选择了第一家公司的第二个部门时的状态
	# [None, None, None]表示尚未选择公司的状态
	# [1,None,None]表示选择了第二家公司时的状态
测试例子：
	0 companyA
	1 companyB
	q quit
	please choose!: 0
	0 技术部
	1 产品部
	2 支持部
	b back
	q quit
	please choose!: 1
	A产甲 A产乙 A产丙 
	b back
	q quit
	please choose!: b
	0 技术部
	1 产品部
	2 支持部
	b back
	q quit
	please choose!: 2
	A支甲 A支乙 A支丙 
	b back
	q quit
	please choose!: b
	0 技术部
	1 产品部
	2 支持部
	b back
	q quit
	please choose!: b
	0 companyA
	1 companyB
	q quit
	please choose!: 1
	0 市场部
	1 销售部
	b back
	q quit
	please choose!: 1
	B销甲 B销乙 B销丙 
	b back
	q quit
	please choose!: b
	0 市场部
	1 销售部
	b back
	q quit
	please choose!: b
	0 companyA
	1 companyB
	q quit
	please choose!: 0
	0 技术部
	1 产品部
	2 支持部
	b back
	q quit
	please choose!: 0
	A技甲 A技乙 A技丙 
	b back
	q quit
	please choose!: q

	Process finished with exit code 0




	