<template>
	<view>
		<!-- 		<view class="cu-bar search bg-white">
			<view class="search-form round">
				<text class="cuIcon-search"></text>
				<input type="text" style="font-size: 16px;" :placeholder="输入拍照或" confirm-type="search"></input>
			</view>
		</view> -->
		<view style="display: flex;flex-wrap: wrap">
			<navigator url="../component/component" hover-class="none" class="cu-card " style="max-width: 380px;" v-for="(searchRec,index) in searchRecs" :key="index">
				<view class="cu-item shadow" >
					<view style="width:330px;height:300px;background-size:cover;" :style="'background-image:url('+searchRec['image_url']+');'"></view>
					<view class="cu-list menu-avatar">
						<view class="cu-item">
							<view class="content flex-sub">
								<view class="text-grey" style="color: #000000;">{{searchRec['name']}}</view>
								<view class="text-gray text-sm flex justify-between">
									<span style="font-size: bold;">Code:</span>{{searchRec['code']}}  
								</view>
								<view class="text-gray text-sm flex justify-between">
									<span style="font-size: bold;">Price:</span>{{searchRec['price']}} EUR
								</view>
							</view>
						</view>
					</view>
				</view>
			</navigator>
		</view>
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
				array: ['全部', 'AMM', 'IPC', '工卡'],
				index: 0,
				searchTitle: "根据工卡或标题搜索AMM/IPC手册",
				searchRecs: [{
					"name": "MAINT ENTRY DUCT ASSY",
					"type": "Engine Issue",
					"probability": "",
					"intro": "PN: L9871230AZ IPC 36-12-42-01 ITEM 300B CANNIBALIZED TOSERVICE 2Q-QK7."
				}],
				widthCheckDetail: true,
				history: [],
				search_type: "AMM"
			}
		},
		components: {

		},
		onLoad(options) {
			var that = this
			console.log(options)
			that.image_url = options.image_url

			if (options.image_url) {
				that.judgeComponent()
			}
		},
		computed: {
			checkDetail: function() {
				return this.widthCheckDetail ? 0 : 90
			}
		},
		methods: {
			judgeComponent: function() {
				var that = this
				uni.showToast({
					title: 'Loading',
					// duration: 2000,
					icon: "loading"
				});
				uni.request({
					url: config.service.host + '/weapp/image',
					data: {
						image_url: that.image_url
					},
					success: function(res) {
						uni.hideToast();
						console.log(res.data)
						if (res.data.code == 0) {

						} else {
							that.searchRecs = res.data.data.products
						}
					}
				})
			},
			navDetail: function() {
				var that = this
				console.log(that.search_type)
				if (that.search_type == "AMM") {
					uni.openDocument({
						filePath: "https://ly.inftime.cn/Illustrated-parts-catalog.pdf",
						success: function(res) {
							console.log('打开文档成功');
						}
					})
				} else {
					uni.navigateTo({
						url: '../component/component'
					});
				}
			},
			bindPickerChange: function(e) {
				console.log('picker发送选择改变，携带值为', e.target.value)
				this.index = e.target.value
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

	input::placeholder {
		font-size: 13px !important;
	}
</style>
