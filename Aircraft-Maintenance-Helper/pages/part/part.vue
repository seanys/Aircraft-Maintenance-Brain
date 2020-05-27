<template>
	<view>
		<view style="margin:10px;">
			<!-- <view class="weui-flex" style="margin-bottom:20px;">
				<view @click="navSearch" class="weui-flex__item weui-cell" style="background-color:white;border-radius:5px;margin:10px;">
					<view class="weui-cell__bd" style="font-weight:bold;">Search Directly</view>
					<view class="weui-cell__ft weui-cell__ft_in-access"></view>
				</view>
				<view class="weui-flex__item weui-cell" @click="checkByPhoto" style="background-color:white;border-radius:5px;margin:10px;">
					<view class="weui-cell__bd" style="font-weight:bold;">
						Search By Photo
					</view>
					<view class="weui-cell__ft weui-cell__ft_in-access"></view>
				</view>
			</view> -->
			<view class="weui-panel weui-panel_access" style="margin:25px 20px;background-color:transparent;">
				<view @click="navSearch" class="weui-cell bg-white" style="border-radius:4px;margin-bottom:10px;padding:15px;position: relative;">
					<view class="weui-media-box__bd weui-media-box__bd_in-appmsg" style="width: 100%;">
						<view class="weui-media-box__title">
							<span style="font-size:18px;margin-right: 9px;color:#303133">Search Directly</span>
						</view>
						<view class="weui-media-box__desc" style="margin-top:5px;">
							<span style="margin-right:10px;font-size:14px">You can search IPC/AMM/Job Card directly</span>
						</view>
					</view>
					<view class="weui-cell__ft weui-cell__ft_in-access"></view>
				</view>

				<view @click="checkByPhoto" class="weui-cell bg-white" style="border-radius:4px;margin-bottom:10px;padding:15px;position: relative;">
					<view class="weui-media-box__bd weui-media-box__bd_in-appmsg weui-cell__bd" style="width: 100%;">
						<view class="weui-media-box__title">
							<span style="font-size:18px;margin-right: 9px;color:#303133">Search By Photo</span>
						</view>
						<view class="weui-media-box__desc" style="margin-top:5px;">
							<span style="margin-right:10px;14px">You can search components just use few photos (More than one)</span>
						</view>
					</view>
					<view class="weui-cell__ft weui-cell__ft_in-access"></view>
				</view>

				<navigator url="../image_history/image_history" class="weui-cell bg-white" style="border-radius:4px;margin-bottom:10px;padding:15px;position: relative;">
					<view class="weui-media-box__bd weui-media-box__bd_in-appmsg weui-cell__bd" style="width: 100%;">
						<view class="weui-media-box__title">
							<span style="font-size:18px;margin-right: 9px;color:#303133;">Search History</span>
						</view>
					</view>
					<view class="weui-cell__ft weui-cell__ft_in-access"></view>
				</navigator>
			</view>
			<button @click="navOrder" style="margin:0px 20px;border-radius:23px;background-image: linear-gradient(-234deg, #499DF8 0%, #6EC3FC 100%);color:white;">
				Submit Order
			</button>
		</view>
	</view>
</template>

<script>
	import config from "../../common/config.js"
	export default {
		data() {
			return {
				navigatorTitle: '航班维修',
				navigatorBarColor: '#40485B',
				navigatorTitleColor: 'white',
				myCreate: "",
				array: ['选择相片', '拍照'],
				index: 0,
				border_array: ['normal_border_color', 'middle_border_color', 'important_border_color'],
				text_array: ['normal_color', 'middle_color', 'important_color'],
			}
		},
		components: {

		},
		onLoad() {
			this.loadBasic()
		},
		computed: {

		},
		methods: {
			loadBasic: function() {
				var that = this
			},
			checkByPhoto: function() {
				var that = this
				uni.showModal({
					title: 'Attention',
					content: 'You are required to take photo of aim component and choose pictures',
					confirmText: 'OK',
					cancelText: 'Cancel',
					success: function(res) {
						if (res.confirm) {
							uni.chooseImage({
								count: 1, //默认9
								sourceType: ['album'],
								sizeType: ['compressed'], //可以指定是原图还是压缩图，默认二者都有
								success: function(res) {
									console.log(JSON.stringify(res.tempFilePaths));
									console.log(res.tempFilePaths)
									that.uploadFile(res.tempFilePaths)
								},
							});
						} else if (res.cancel) {
							console.log('用户点击取消');
						}
					}
				});

			},
			uploadFile: function(attachment) {
				var that = this
				var img_key = []
				uni.showToast({
					title: 'Uploading',
					icon: "loading"
				});
				uni.request({
					url: config.service.host + '/weapp/uploadfile',
					success: (result) => {
						console.log(result.data)
						var token = {
							'token': result.data
						}
						for (var i in attachment) {
							uni.uploadFile({
								url: 'https://upload.qiniup.com',
								name: 'file',
								filePath: attachment[i],
								formData: {
									token: result.data
								},
								success: (res) => {
									var data = JSON.parse(res.data)
									img_key.push(data.key)
									console.log(data)
									console.log(attachment[i])
									if (attachment.length == img_key.length) {
										uni.request({
											url: config.service.host + '/weapp/insert',
											data: {
												img_key: JSON.stringify(img_key)
											}
										})
									}
									that.image_urls = ['http://pw5w2wzrm.bkt.clouddn.com/' + data.key]
									uni.hideToast();
									uni.navigateTo({
										url: '../search_by_photo/search_by_photo?image_url=http://pw5w2wzrm.bkt.clouddn.com/' + data.key
									})
								}
							})
						}
					}
				})
			},
			navOrder: function() {
				uni.navigateTo({
					url: '../order/order',
				});
			},
			navSearch: function() {
				uni.navigateTo({
					url: '../search/search',
				});
			}
		}
	}
</script>

<style>
	@import "../../common/weui.min.css";
	@import "../../common/basic.css";
	@import "../../common/inftime.css";
</style>
