<template>
	<view class="page">
		<view class="page__bd" style="margin: 5px 20px;">
			<view class="weui-panel weui-panel_access" style="margin:10px;background-color:transparent;">
				<view class="weui-panel weui-panel_access" @click="navUserDetail" style="margin-top:20px;border-radius: 4px;">
					<view class="weui-panel__bd">
						<view class="weui-media-box weui-media-box_appmsg">
							<view class="weui-media-box__hd weui-media-box__hd_in-appmsg">
								<image class="weui-media-box__thumb" style="border-radius:3px;" :src="headImageUrl" />
							</view>
							<view class="weui-media-box__bd weui-media-box__bd_in-appmsg">
								<view class="weui-media-box__title">{{logged?nickname:"Click to Login"}}</view>
								<view class="weui-media-box__desc"></view>
							</view>
							<view class="weui-cell__ft weui-cell__ft_in-access"></view>
						</view>
					</view>
				</view>
				<view class="cu-list menu" style="margin-top: 20px;border-radius: 4px;">
					<view class="cu-item" style="padding: 10px 20px;">
						<view class="content">
							<span style="margin-right: 30px;">Level</span>
							<span style="color:#606266;">Engineer</span>
						</view>
					</view>
					<view class="cu-item" style="padding: 10px 20px;">
						<view class="content">
							<span style="margin-right: 30px;">Job</span>
							<span style="color:#606266;">Airline Maintenance</span>
						</view>
					</view>
				</view>
				<view class="cu-list menu" @click="navAbout" style="margin-top: 20px;border-radius: 4px;">
					<view class="cu-item arrow" style="padding: 10px 20px;">
						<view class="content">
							<span style="margin-right: 20px;">About</span>
						</view>
					</view>
				</view>
			</view>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				nickname: "Sean",
				headImageUrl: "https://ww2.sinaimg.cn/large/006tNc79ly1g5tfy9x60mj30u00u2qs6.jpg",
				logged: true,
			};
		},
		methods: {
			arrangeModePickerChange: function(e) {
				var that = this
				that.arrangeModeIndex = e.detail.value
				console.log(e)
			},
			remindModePickerChange: function(e) {
				var that = this
				that.remindModeIndex = e.detail.value
				console.log(e)
			},
			navUserDetail: function() {
				uni.showModal({
					title: '提示',
					content: '功能开发中',
					showCancel: false,
					success: function(res) {

					}
				});
			},
			navAbout: function() {
				uni.showModal({
					title: '提示',
					content: '功能开发中',
					showCancel: false,
					success: function(res) {

					}
				});
			}
		},
		onLoad: function() {

		}
	}
</script>

<style>
	@import "../../common/weui.min.css";
	@import "../../common/basic.css";
	@import "../../common/inftime.css";
</style>
