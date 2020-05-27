<template>
	<view>
		<view class="weui-panel weui-panel_access" style="margin:20px 20px 10px 20px;background-color:transparent;">
			<view class="weui-cell" style="border-radius:4px;margin-bottom:10px;padding:15px 20px;position: relative;background-color: white;">
				<view class="weui-media-box__bd weui-media-box__bd_in-appmsg" style="width: 100%;">
					<view class="weui-media-box__title">
						<span style="font-weight:bold;font-size:18px;margin-right: 9px;">{{productObject['name']}}</span>
						<span style="font-size:16px;color:#909399">ID:{{productObject['product_id']}}</span>
						<span style="float:right;font-size:16px;color:#4584EA;background-color: #ECF5FF;color:#4584EA;padding: 2px 10px; border-radius: 4px;" v-if="productObject['product_id']%10000==0">Main Component</span>
						<span style="float:right;font-size:16px;color:#4584EA;background-color: #F0F9EB;color:#6AC044;padding: 2px 10px; border-radius: 4px;" v-if="productObject['product_id']%10000!=0" v-bind:style="{color:colors[1]}">Sub Component</span>
					</view>
					<view class="weui-media-box__desc" style="margin-top:5px;font-size: 15px;line-height: 19px;">
						<view style="margin-right:10px;">Location：{{productObject['location']}}</view>
						<view style="margin-right:10px;">Dimension：{{productObject['dimension']}}</view>
						<view style="margin-right:10px;">Weight：{{productObject['weight']}}</view>
					</view>
				</view>
			</view>
		</view>
		<view class="weui-panel weui-panel_access" style="margin:10px 20px;background-color:transparent;">
			<view style="border-radius:4px;background-color: white!important;">
				<view class="weui-cell" style="padding:10px 20px;">
					<view class="weui-media-box__bd weui-media-box__bd_in-appmsg" style="width: 100%;">
						<view class="weui-media-box__title" style="display:flex">
							<view style="font-size:16px;margin-right: 9px;" class="weui-cell__bd">
								<span style="margin-right:10px;font-weight:bold;">Images</span>
								<!-- <span style="margin-right:10px;color:#909399;font-size:15px;">近一个月内两次维修</span> -->
							</view>
						</view>
					</view>
				</view>
				<view style="border-radius:4px;display: flex;padding: 0px 15px 10px 20px;background-color: white;">
					<view class="weui-cell__bd">
						<view class="weui-uploader__files" id="uploaderFiles">
							<view v-for="(image,index) in images_urls" :key="index" v-if="productObject['product_id']==10000||index==productObject['product_id']-9999" @click="previewImage">
								<view class="weui-uploader__file" :id="index">
									<image class="weui-uploader__img" :src="image['image_url']" mode="aspectFill" />
								</view>
							</view>
						</view>
					</view>
				</view>
			</view>
		</view>
		<view class="weui-panel weui-panel_access" style="margin:20px 20px;background-color:transparent;">
			<view style="border-radius:4px;background-color: white!important;">
				<view class="weui-cell" @click="allHistory" style="padding:10px 20px;">
					<view class="weui-media-box__bd weui-media-box__bd_in-appmsg" style="width: 100%;">
						<view class="weui-media-box__title" style="display:flex">
							<view style="font-size:16px;margin-right: 9px;" class="weui-cell__bd">
								<span style="margin-right:10px;font-weight:bold;">Test Procedure</span>
								<!-- 								<span style="margin-right:10px;color:#909399;font-size:15px;">近一个月内两次维修</span> -->
							</view>
							<view class="weui-cell__ft weui-cell__ft_in-access" style="transition:transform 0.1s;" v-bind:style="{transform: 'rotate('+checkDetail+'deg)'}"></view>
						</view>
					</view>
				</view>
				<view class="weui-cell" style="color:#606266;margin-left: 5px;">
					<view class="text-wrapper">{{productObject['test_procedure']}}</view>
				</view>
			</view>
		</view>
		<view class="weui-panel weui-panel_access" style="margin:10px 20px;background-color:transparent;">
			<view style="border-radius:4px;background-color: white!important;">
				<view class="weui-cell" style="padding:10px 20px;">
					<view class="weui-media-box__bd weui-media-box__bd_in-appmsg" style="width: 100%;">
						<view class="weui-media-box__title" style="display:flex">
							<view style="font-size:16px;margin-right: 9px;" class="weui-cell__bd">
								<span style="margin-right:10px;font-weight:bold;">Subcomponents</span>
								<!-- <span style="margin-right:10px;color:#909399;font-size:15px;">近一个月内两次维修</span> -->
							</view>
							<!-- <view class="weui-cell__ft weui-cell__ft_in-access" style="transition:transform 0.1s;" v-bind:style="{transform: 'rotate('+checkDetail+'deg)'}"></view> -->
						</view>
					</view>
				</view>
				<view class="weui-cell" style="color:#909399;margin-left: 5px;" v-if="productObject['sub_num']==0">
					No Subcomponents
				</view>
				<navigator :url="'../component/component?product_id='+subcomponent['id']" v-if="productObject['sub_num']>0" class="weui-cell"
				 v-for="(subcomponent,index) in subcomponents" :key="index" style="color:#606266;flex-wrap: wrap;margin-left: 5px;">
					<view>
						<span style="text-transform: Uppercase;margin-right: 5px;color:rgb(69, 132, 234)">{{subcomponent['id']}}</span>
						<span>{{subcomponent.name}}</span>
					</view>
					<!-- <view style="color:#909399">{{maintenance['completion by date']}}</view> -->
				</navigator>
			</view>
		</view>
		<view class="weui-panel weui-panel_access" style="margin:20px 20px;background-color:transparent;">
			<view style="border-radius:4px;background-color: white!important;">
				<view class="weui-cell" style="padding:10px 20px;">
					<view class="weui-media-box__bd weui-media-box__bd_in-appmsg" style="width: 100%;">
						<view class="weui-media-box__title" style="display:flex">
							<view style="font-size:16px;margin-right: 9px;" class="weui-cell__bd">
								<span style="margin-right:10px;font-weight:bold;">Manuals</span>
							</view>
							<!-- <view class="weui-cell__ft weui-cell__ft_in-access" style="transition:transform 0.1s;" v-bind:style="{transform: 'rotate('+checkDetail+'deg)'}"></view> -->
						</view>
					</view>
				</view>
				<navigator url="../manual/manual?fileID=Boeing747_AMM_32_12&page=0" class="weui-cell" v-for="(manual,index) in manuals" :key="index" style="color:#606266;flex-wrap: wrap;margin-left: 5px;">
					<view>
						<span style="text-transform: Uppercase;margin-right: 5px;color:rgb(69, 132, 234)">{{manual.type}}</span>
						<span style="text-transform: Uppercase;margin-right: 10px;color:rgb(69, 132, 234)">{{manual.section}}</span>
						<span v-for="(page,p_index) in manual.pages" :key="p_index" style="margin-right: 10px;">P{{page}}</span>
					</view>
					<!-- <view style="color:#909399">{{maintenance['completion by date']}}</view> -->
				</navigator>
			</view>
		</view>
		<button @click="navOrder" style="margin:20px 20px;border-radius:23px;background-image: linear-gradient(-234deg, #499DF8 0%, #6EC3FC 100%);color:white;">
			New Order
		</button>
		<view style="height:50px;"></view>
	</view>
</template>

<script>
	import config from "../../common/config.js"
	export default {
		data() {
			return {
				productObject: {
					amm_section: "32-12-00",
					dimension: "400x200x50mm",
					id: "1",
					images_num: "3",
					ipc_section: "45-11-21",
					location: "Wing Gear Doors",
					name: "WING GEAR SHOCK STRUT DOORS",
					product_id: "10000",
					sub_num: "3",
					test_procedure: "Multiple",
					weight: "55kg",
				},
				colors:["#4584EA","#6AC044"],
				history: [],
				images_urls: [{
						"image_url": "http://ww2.sinaimg.cn/large/006tNc79ly1g5qgh3ikwkj306404r3yg.jpg"
					},
					{
						"image_url": "http://ww2.sinaimg.cn/large/006tNc79ly1g5qgh3db3sj31hc0u0e81.jpg"
					},
					{
						"image_url": "http://ww4.sinaimg.cn/large/006tNc79ly1g5qgh1otw1j31720hjb29.jpg"
					}
				],
				images_urls_array: ["http://ww2.sinaimg.cn/large/006tNc79ly1g5qgh3ikwkj306404r3yg.jpg",
					"http://ww2.sinaimg.cn/large/006tNc79ly1g5qgh3db3sj31hc0u0e81.jpg",
					"http://ww4.sinaimg.cn/large/006tNc79ly1g5qgh1otw1j31720hjb29.jpg"
				],
				subcomponents: [{
					"id": 10001,
					"name": "WING GEAR SHOCK STRUT OUTBOARD DOOR"
				}, {
					"id": 10002,
					"name": "WING GEAR SHOCK STRUT INBOARD DOOR"
				}, {
					"id": 10003,
					"name": "WING GEAR SHOCK STRUT DOOR FAIRING"
				}],
				manuals: [{
						"type": "AMM",
						"section": "32-12-00",
						"pages": [508, 514, 535]
					},
					{
						"type": "ICP",
						"section": "45-11-21",
						"pages": [220, 235, 246]
					}
				],
				guide: "1. General\nA. This procedure has two tasks:\n(1)  The adjustment of the doors for the body landing gear.\n(2)  The adjustment of the doors for the body landing gear after the door actuator replacement.\nB.  When you replace the door for the body landing gear, you must adjust the door.  It is necessary to close the door to check the actuator for the fully locked position or for rig pin installation of the sequence valve. If the actuator cannot be locked fully or the rig pin cannot be put in freely, you must adjust the door.\nC.  When you close the doors, make sure the landing gear control handle is in the off position.  This will port the hydraulic pressure in the door actuator to return and ensure the door is mechanically locked.\nD.  You can adjust the forward doors for the body landing gear with the airplane on the ground.  You must lift the airplane clear of the ground to adjust the shock strut door.  If you do not have jacks, you can do a temporary door adjustment with the steps that follow.\nE.  This task is applicable to the left body landing gear doors and the right body landing gear doors."
			}
		},
		components: {

		},
		onLoad(options) {
			var that = this
			console.log(options)
			//请求ID内容
			if (parseInt(options.product_id) > 0) {
				uni.request({
					url: config.service.host + '/weapp/component',
					data: {
						product_id: parseInt(options.product_id)
					},
					success: function(res) {
						console.log(res.data.data)
						that.productObject = res.data.data.product
						that.images_urls = res.data.data.product_image
					}
				})
			}

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
			navOrder: function() {
				uni.navigateTo({
					url: '../order/order'
				});
			},
			navManual: function() {
				uni.showModal({
					title: '提示',
					content: '功能开发中，该处跳转PDF页面',
					showCancel: false,
					success: function(res) {

					}
				});
			},
			previewImage: function() {
				var that = this;
				uni.previewImage({
					urls: that.images_urls_array,
					current: that.images_urls_array[0],
					longPressActions: {
						success: function(data) {
							console.log('选中了第' + (data.tapIndex + 1) + '个按钮,第' + (data.index + 1) + '张图片');
						},
						fail: function(err) {
							console.log(err.errMsg);
						}
					}
				});
			},
			historyCheck: function() {

			},
			allHistory: function() {
				uni.showModal({
					title: '提示',
					content: '功能开发中',
					showCancel: false,
					success: function(res) {

					}
				});
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

	.text-wrapper {
		white-space: pre-wrap;
	}
</style>
