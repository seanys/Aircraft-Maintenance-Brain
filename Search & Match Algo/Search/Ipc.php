<?php
defined('BASEPATH') or exit('No direct script access allowed');
// 指定允许其他域名访问  
header('Access-Control-Allow-Origin:*');  
// 响应类型  
header('Access-Control-Allow-Methods:*');  
use QCloud_WeApp_SDK\Mysql\Mysql as DB;//数据库连接，按照config中链接
use QCloud_WeApp_SDK\Mysql\AirMysql as ADB;
class Ipc extends CI_Controller
{
    //输入keyword返回所有相关数据
    //主函数部分
    public function index()
    {
        if(isset($_GET['keyword'])){
        $sql="`intro` LIKE \"%".$_GET['keyword']."%\" or `cat_no` like '%".$_GET['keyword']."%'";
        $res=ADB::select('ipc_pdf',['*'],$sql);
        $this->json([
            'code'=>"success",
            'data'=>[
                "infor"=>$res
            ],
        ]);
    } 
    else{
        $this->json([
            'code'=>"failed",
        ]);
    }
    }
}
