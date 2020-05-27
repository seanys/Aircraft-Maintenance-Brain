<template>
	<view>
		<view class="weui-panel weui-panel_access" style="margin:20px 20px 10px 20px;background-color:transparent;">
			<view class="weui-cell" style="border-radius:4px;margin-bottom:10px;padding:15px 20px;position: relative;background-color: white;">
				<view class="weui-media-box__bd weui-media-box__bd_in-appmsg" style="width: 100%;">
					<view class="weui-media-box__title">
						<span style="font-weight:bold;font-size:18px;margin-right: 9px;">HU7962</span>
						<span style="font-size:16px;color:#909399">B1543</span>
						<span style="float:right;font-size:16px;color:#4584EA;">Landing</span>
					</view>
					<view class="weui-media-box__desc" style="margin-top:5px;">
						<span style="margin-right:10px;">Runway：18L</span>
						<span style="margin-right:10px;">Position：269</span>
					</view>
				</view>
			</view>
		</view>
		<view class="weui-panel weui-panel_access" style="margin:10px 20px;background-color:transparent;">
			<view style="border-radius:4px;background-color: white!important;">
				<view class="weui-cell" @click="allHistory" style="padding:10px 20px;">
					<view class="weui-media-box__bd weui-media-box__bd_in-appmsg" style="width: 100%;">
						<view class="weui-media-box__title" style="display:flex">
							<view style="font-size:16px;margin-right: 9px;" class="weui-cell__bd">
								<span style="margin-right:10px;font-weight:bold;">MAINTENANCE HISTORY</span>
								<span style="margin-right:10px;color:#909399;font-size:15px;">Two repairs in the past month</span>
							</view>
							<view class="weui-cell__ft weui-cell__ft_in-access" style="transition:transform 0.1s;" v-bind:style="{transform: 'rotate('+checkDetail+'deg)'}"></view>
						</view>
					</view>
				</view>
				<view class="weui-cell" style="color:#909399" v-if="history.length==0">
					Loading...
				</view>
				<view class="weui-cell" v-for="(maintenance,index) in history" :key="maintenance.id" style="color:#606266;flex-wrap: wrap;"
				 v-if="history.length>0">
					<view>
						<span style="text-transform: Uppercase;margin-right: 5px;color:rgb(69, 132, 234)">{{maintenance['defect type']}}</span>
						<span>{{maintenance.action}}</span>
					</view>
					<view style="color:#909399">{{maintenance['date']}}</view>
				</view>
			</view>
		</view>
		<!--<view class="weui-panel weui-panel_access" style="margin:10px;background-color:transparent;">
			<view class="weui-cell" style="border-radius:4px;margin-bottom:10px;padding:15px;position: relative;background-color: white;">
				<view class="weui-media-box__bd weui-media-box__bd_in-appmsg" style="width: 100%;">
					<view class="weui-media-box__title">
						<span style="font-weight:bold;font-size:16px;margin-right: 9px;">预计问题</span>
					</view>
					<view class="weui-media-box__desc" style="margin-top:5px;">
						<span style="margin-right:10px;">通过数据计算的预计出现的一些问题 工程师4人 共需1h</span>
					</view>
				</view>
				<view class="weui-cell__ft weui-cell__ft_in-access"></view>
			</view>
		</view> -->
		<navigator url="../search/search?search_aircraft=0" class="weui-panel weui-panel_access" style="margin:20px 20px 10px 20px;background-color:transparent;">
			<view class="weui-cell" style="border-radius:4px;margin-bottom:10px;padding:15px;position: relative;background-color: white;">
				<view class="weui-media-box__bd weui-media-box__bd_in-appmsg" style="width: 100%;">
					<view class="weui-media-box__title">
						<span style="font-weight:bold;font-size:16px;margin-right: 9px;">Manual Search</span>
					</view>
					<view class="weui-media-box__desc" style="margin-top:5px;">
						<span style="margin-right:10px;font-size:15px">Quickly find related manual pages after finding problems on the plane</span>
					</view>
				</view>
				<view class="weui-cell__ft weui-cell__ft_in-access"></view>
			</view>
		</navigator>
		<navigator url="../map_html/map_html" class="weui-panel weui-panel_access" style="margin:10px 20px;background-color:transparent;">
			<view class="weui-cell" style="border-radius:4px;margin-bottom:10px;padding:15px;position: relative;background-color: white;">
				<view class="weui-media-box__bd weui-media-box__bd_in-appmsg" style="width: 100%;">
					<view class="weui-media-box__title">
						<span style="font-weight:bold;font-size:16px;margin-right: 9px;">Maintenance Location</span>
					</view>
					<view class="weui-media-box__desc" style="margin-top:5px;">
						<span style="margin-right:10px;">Navigate to the destination</span>
					</view>
				</view>
				<view class="weui-cell__ft weui-cell__ft_in-access"></view>
			</view>
		</navigator>
		<!-- <button open-type="contact" bindcontact="handleContact" style="margin:20px 20px;border-radius:23px;background-image: linear-gradient(-234deg, #499DF8 0%, #6EC3FC 100%);color:white;">
			维修状态
		</button> -->
	</view>
</template>

<script>
	import config from "../../common/config.js"
	export default {
		data() {
			return {
				navigatorTitle: "详情",
				nickname: "羊山",
				headImageUrl: "../../static/arrowLeftTopWhite.png",
				logged: true,
				achieve: false,
				itemImportance: 0,
				timeExit: true,
				widthCheckDetail: true,
				history: []
			}
		},
		components: {

		},
		onLoad(options) {
			var that = this
			// var url = location.search; //获取url中"?"符后的字串
			// var theRequest = new Object();
			// if (url.indexOf("?") != -1) {
			// 	var str = url.substr(1);
			// 	strs = str.split("&");
			// 	for (var i = 0; i < strs.length; i++) {
			// 		theRequest[strs[i].split("=")[0]] = unescape(strs[i].split("=")[1]);
			// 	}
			// }
			//             console.log(theRequest)

			uni.request({
				url: config.service.mock + '/flightlog/',
				data: {
					flightNumber: 861
				},
				success: function(res) {
					console.log(res.data.data)
					that.history = res.data.data.history
				}
			})

			uni.request({
				url: config.service.mock + '/manualproduct/',
				data: {
					productID: 10000
				},
				success: function(res) {
					console.log(res.data)
				}
			})
		},
		computed: {
			checkDetail: function() {
				return this.widthCheckDetail ? 0 : 90
			}
		},
		methods: {
			moreDetailClick: function(e) {
				uni.showActionSheet({
					itemList: ['删除'],
					success: function(res) {
						if (res.tapIndex == 0) {
							console.log("用户点击删除")
							uni.navigateTo({
								url: '../index/index'
							});
						}
					},

				});
			},
			historyCheck: function() {

			},
			allHistory: function() {
				uni.navigateTo({
					url: "../history/history"
				})
				// uni.showModal({
				// 	title: '提示',
				// 	content: '功能开发中',
				// 	showCancel:false,
				// 	success: function(res) {
				// 		
				// 	}
				// });
			},
			backIndex: function() {
				uni.navigateBack({
					delta: 1
				})
			},
		}
	}
</script>

<style>
	@import "../../common/weui.min.css";
	@import "../../common/basic.css";
	@import "../../common/inftime.css";
</style>
