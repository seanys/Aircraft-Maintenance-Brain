<template>
	<view>
		<view class="weui-panel weui-panel_access" style="margin:20px 20px 10px 20px;background-color:transparent;border-radius: 4px;">
			<view class="cu-form-group">
				<view class="title">Product ID</view>
				<input placeholder="输入ID" value="10000" />
			</view>
			<view class="cu-form-group">
				<view class="title">Product Name</view>
				<input placeholder="Input Name" value="WING GEAR SHOCK STRUT OUTBOARD DOOR" />
			</view>
			<view class="cu-form-group">
				<view class="title">Authentication</view>
				<input placeholder="Engineer" value="Chief Engineer" />
				<button class="cu-btn" style="background-color:#478AE7;color:white;" v-if="!identified" @click="authentication">Identify</button>
				<button class="cu-btn" style="background-color:#478AE7;color:white;" disabled="true" v-if="identified">Identified</button>
			</view>
			<view class="cu-form-group align-start" style="padding-top: 20px;">
				<view class="title">Defect Text</view>
				<textarea maxlength="-1" placeholder="Input Defect Text" value="MAINT ENTRY DUCT ASSY PN: L9871230AZ IPC 36-12-42-01 ITEM 300B CANNIBALIZED TOSERVICE 2Q-QK7."></textarea>
			</view>
		</view>
		<button @click="submitOrder" style="margin:20px 20px;border-radius:23px;background-image: linear-gradient(-234deg, #499DF8 0%, #6EC3FC 100%);color:white;">
			Submit Order
		</button>
		<view style="height:50px;"></view>
	</view>
</template>

<script>
	import config from "../../common/config.js"
	export default {
		data() {
			return {
				widthCheckDetail: true,
				history: [],
				identified: true
			}
		},
		components: {

		},
		onLoad(options) {
			var that = this


		},
		computed: {
			checkDetail: function() {
				return this.widthCheckDetail ? 0 : 90
			}
		},
		methods: {
			navManual: function() {
				uni.showModal({
					title: '提示',
					content: '功能开发中，该处跳转PDF页面',
					showCancel: false,
					success: function(res) {

					}
				});
			},
			authentication: function() {
				var waiting = null;
				var that=this
				// #ifdef APP-PLUS
				plus.fingerprint.authenticate(function() {
					plus.nativeUI.closeWaiting(); //兼容Android平台关闭等待框
					that.identified=true
				}, function(e) {
					switch (e.code) {
						case e.AUTHENTICATE_MISMATCH:
							plus.nativeUI.toast('Fingerprint matching failed');
							break;
						case e.AUTHENTICATE_OVERLIMIT:
							plus.nativeUI.closeWaiting(); //兼容Android平台关闭等待框
							plus.nativeUI.alert('The number of fingerprint recognition failures exceeds the limit.');
							break;
						default:
							plus.nativeUI.closeWaiting(); //兼容Android平台关闭等待框
							plus.nativeUI.alert('Identify failed, please try again');
							break;
					}
				});
				// that.identified=true
				// Android平台弹出等待提示框 
				if ('Android' == plus.os.name) {
					plus.nativeUI.showWaiting('Identifying...');
				}
				// #endif
			},
			submitOrder: function() {
				var that = this
				if (!that.identified) {
					uni.showModal({
						title: 'Attention',
						content: 'You have not authenticated yet',
						showCancel: false,
						success: function(res) {

						}
					});
				} else {
					uni.showToast({
						title: 'Submit Successful',
						duration: 2000,
						icon:"success"
					});
					setTimeout(function() { 
						uni.navigateBack({
							delta:1
						})
					}, 2000); 
				}
			},
			previewImage: function() {
				var that = this;
				uni.previewImage({
					urls: that.images_url,
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
