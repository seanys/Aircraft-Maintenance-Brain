/**
 * 配置文件
 */

// 此处主机域名修改成腾讯云解决方案分配的域名
// var host = 'https://666132810.inftime.com.cn';
// var host ='https://d7n9906g.qcloud.la';
// var host ='https://produce.inftime.com.cn';

const host ='https://ly.inftime.cn';

const mock= 'https://dac2b96e-149a-4935-afac-ff04612a62b6.mock.pstmn.io'

var config = {

    // 下面的地址配合云端 Demo 工作
    service: {
        host,
		
		mock,

        // 登录地址，用于建立会话
        loginUrl: `${host}/weapp/login`,

        // 测试的请求地址，用于测试会话
        requestUrl: `${host}/weapp/user`,
		
        // 测试的信道服务地址
        tunnelUrl: `${host}/weapp/tunnel`,

        // 上传图片接口
        uploadUrl: `${host}/weapp/upload`
    }
};

module.exports = config;