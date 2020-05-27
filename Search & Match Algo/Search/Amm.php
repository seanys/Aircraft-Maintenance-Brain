<?php
defined('BASEPATH') or exit('No direct script access allowed');
// 指定允许其他域名访问  
header('Access-Control-Allow-Origin:*');  
// 响应类型  
header('Access-Control-Allow-Methods:*');  
use QCloud_WeApp_SDK\Mysql\Mysql as DB;//数据库连接，按照config中链接
use QCloud_WeApp_SDK\Mysql\AirMysql as ADB;
class Amm extends CI_Controller
{
    //主函数部分
    public function index()
    {
        if(isset($_GET['keyword'])){ //文字检索
            $sql="`en` LIKE \"%".$_GET['keyword']."%\" or `ch` like '%".$_GET['keyword']."%'";
            $res=ADB::select('amm',['*'],$sql);
            $this->json([
                'code'=>"success",
                'data'=>[
                    "infor"=>$res
                ],
            ]);    
        }
        elseif(isset($_GET['page'])){  //页码检索
            $sql="`intro` LIKE \"%".$_GET['page']."%\"";
            $res=ADB::select('amm_index',['*'],$sql);
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
